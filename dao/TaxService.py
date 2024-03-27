import sqlite3
from decimal import Decimal
from typing import List

from entity.Employee import Employee
from entity.Tax import Tax
from util.DBPropertyUtil import DBPropertyUtil

class TaxService:
    def __init__(self):
        self.connection = DBPropertyUtil.getDBConn()
        self.taxList = []
        taxAmount = 0.0

    def calculateTax(self, employeeID: int, taxYear: int) -> Tax:
        tax = self.getTaxableIncomeForEmployeeAndYear(employeeID, taxYear)
        if tax is not None:
            taxableIncome = tax.get_taxable_income()
            if taxableIncome is not None:  # Check if taxableIncome is not None
                taxAmount = 0.0
                if 100000 <= taxableIncome < 250000:
                    taxAmount = taxableIncome * Decimal('0.03')
                elif 250000 <= taxableIncome < 500000:
                    taxAmount = taxableIncome * Decimal('0.05')
                elif 500000 <= taxableIncome < 1000000:
                    taxAmount = taxableIncome * Decimal('0.1')
                elif 1000000 <= taxableIncome < 1500000:
                    taxAmount = taxableIncome * Decimal('0.15')
                else:
                    taxAmount = taxableIncome * Decimal('0.18')
                print("Employee ID:", employeeID)
                print("Tax year:", taxYear)
                print("Taxable income:", taxableIncome)
                print("Tax Amount:", taxAmount)

                query = "INSERT INTO tax (EmployeeID, TaxYear, TaxableIncome, TaxAmount) VALUES (?, ?, ?, ?)"
                with self.connection.cursor() as cursor:
                    cursor.execute(query, (employeeID, taxYear, taxableIncome, taxAmount))
                return tax
            else:
                print("Error: Taxable income is None.")
                return None
        else:
            print("Error: Tax is None.")
            return None


    def helpTax(self, employeeID: int, TaxYear) -> Tax:
        tax = self.getTaxableIncomeForEmployeeAndYear(employeeID, TaxYear)
        return tax

    from decimal import Decimal

    def getTaxableIncomeForEmployeeAndYear(self, employeeID: int, taxYear: int) -> Tax:
        query = "SELECT PayrollID, sum(BasicSalary) as TotalBasicSalary, " \
                "sum(OvertimePay) as TotalOvertimePay " \
                "FROM payroll " \
                "WHERE EmployeeID = ? AND YEAR(PayPeriodEndDate) = ? " \
                "GROUP BY PayrollID"
        cursor = self.connection.cursor()
        cursor.execute(query, (employeeID, taxYear))
        results = cursor.fetchall()

        for result in results:
            basicSalary = float(result[1])
            overtime = float(result[2])
            deductions = (basicSalary * 0.12)
            taxableIncome = (basicSalary + overtime) - deductions
            tax = Tax(taxableIncome, deductions)
            return tax

        return None

    def extractYear(self, date):
        return date.year

    def getTaxById(self, taxID: int) -> Tax:
        query = "SELECT t.TaxID, t.EmployeeID, t.TaxYear, t.TaxableIncome, t.TaxAmount, e.FirstName, e.LastName " \
                "FROM tax t INNER JOIN employee e ON t.EmployeeID = e.EmployeeID WHERE TaxID = ?"
        preparedStatement = sqlite3.prepareStatement(query)
        preparedStatement.setInt(1, taxID)
        resultSet = preparedStatement.executeQuery()
        while resultSet.next():
            tax = Tax(taxID,
                      resultSet.getInt("EmployeeID"),
                      Employee(
                          resultSet.getString("FirstName"),
                          resultSet.getString("LastName")),
                      resultSet.getInt("TaxYear"),
                      resultSet.getDouble("TaxableIncome"),
                      resultSet.getDouble("TaxAmount"))
            self.taxDetails(tax)
            return tax
        return None

    def getTaxesforEmployee(self, employeeID: int) -> List[Tax]:
        taxEmployee = []
        query = "SELECT t.TaxID, t.TaxYear, t.TaxableIncome, t.TaxAmount, e.FirstName, e.LastName " \
                "FROM tax t INNER JOIN employee e on e.EmployeeID = t.EmployeeID where e.EmployeeID = ?"
        preparedStatement = self.connection.prepareStatement(query)
        preparedStatement.setInt(1, employeeID)
        resultSet = preparedStatement.executeQuery()
        while resultSet.next():
            tax = Tax(resultSet.getInt("TaxID"),
                      employeeID,
                      Employee(
                          resultSet.getString("FirstName"),
                          resultSet.getString("LastName")),
                      resultSet.getInt("TaxYear"),
                      resultSet.getDouble("TaxableIncome"),
                      resultSet.getDouble("TaxAmount"))
            taxEmployee.append(tax)
        self.taxListofEmployee(taxEmployee)
        return taxEmployee

    def getTaxesforYear(self, taxYear: int) -> List[Tax]:
        taxforYear = []
        query = "SELECT t.TaxID, t.EmployeeID, t.TaxYear, t.TaxableIncome, t.TaxAmount, e.FirstName, e.LastName " \
                "FROM tax t INNER JOIN employee e on e.EmployeeID = t.EmployeeID  where t.TaxYear = ?"
        preparedStatement = self.connection.prepareStatement(query)
        preparedStatement.setInt(1, taxYear)
        resultSet = preparedStatement.executeQuery()
        while resultSet.next():
            tax = Tax(resultSet.getInt("TaxID"),
                      resultSet.getInt("EmployeeID"),
                      Employee(resultSet.getString("FirstName"),
                               resultSet.getString("LastName")),
                      taxYear,
                      resultSet.getDouble("TaxableIncome"),
                      resultSet.getDouble("TaxAmount"))
            taxforYear.append(tax)
        self.taxListofEmployee(taxforYear)
        return taxforYear

    def taxDetails(self, tax: Tax):
        print("------------------------------------")
        print("Tax id: " + str(tax.getTaxID()))
        print("EmployeeId: " + str(tax.getEmployeeID()))
        print("First Name: " + tax.getFirstName())
        print("Last Name: " + tax.getLastName())
        print("tax year: " + str(tax.getTaxYear()))
        print("Taxable Income: " + str(tax.getTaxableIncom()))
        print("Tax Amount: " + str(tax.getTaxAmount()))

    def taxListofEmployee(self, taxList):
        for tax in taxList:
            print("------------------------------------")
            print("Tax id: " + str(tax.getTaxID()))
            print("EmployeeId: " + str(tax.getEmployeeID()))
            print("First Name: " + tax.getFirstName())
            print("Last Name: " + tax.getLastName())
            print("tax year: " + str(tax.getTaxYear()))
            print("Taxable Income: " + str(tax.getTaxableIncom()))
            print("Tax Amount: " + str(tax.getTaxAmount()))
