from dao.TaxService import TaxService
from entity.Employee import Employee
from entity.PayrollService import Payroll
from exception import EmployeeNotFoundException, InvalidInputException, PayrollGenerationException
from datetime import datetime
from util.DBPropertyUtil import DBPropertyUtil


class PayrollService:
    def __init__(self,):
        self.connection = DBPropertyUtil.getDBConn()
        self.payrollList = []
        self.tax_service = TaxService

    def generatePayroll(self, employeeID, startDate, endDate):
        self.tax_service.helpTax(employeeID, startDate, endDate)
        deduction = 0.0

        query = "SELECT e.FirstName, e.LastName, p.PayrollID, p.BasicSalary, p.OvertimePay, p.Deductions, p.NetSalary FROM Employee e INNER JOIN Payroll p ON e.EmployeeID = p.EmployeeID WHERE e.EmployeeID = ? AND p.PayPeriodStartDate >= ? AND p.PayPeriodEndDate <= ?"
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query, (employeeID, startDate, endDate))
            results = cursor.fetchall()
            for result in results:
                payrollId, firstName, lastName, basic, overtime, deduction, _ = result
                netSalary = basic + overtime - deduction
                query1 = "UPDATE Payroll SET NetSalary = ? WHERE EmployeeId = ? AND PayPeriodStartDate = ? AND PayPeriodEndDate = ?"
                cursor.execute(query1, (netSalary, employeeID, startDate, endDate))
                print("PayrollId:", payrollId, ", FirstName:", firstName, ", LastName:", lastName, ", BasicSalary:",
                      basic, ", OvertimePay:", overtime, ", NetSalary:", netSalary)

    def get_payroll_by_id(self, payrollId):
        query = "SELECT * FROM payroll WHERE PayrollID = ?"
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query, (payrollId,))
            result = cursor.fetchone()
            if result:
                return Payroll(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
        return None

    def addPayroll(self, payroll_data):
        try:
            query = "INSERT INTO Payroll (PayrollID, EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimePay, Deductions, NetSalary) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            with self.connection.cursor() as cursor:
                cursor.execute(query, (
                payroll_data['payrollID'], payroll_data['employeeID'], payroll_data['payPeriodStartDate'],
                payroll_data['payPeriodEndDate'], payroll_data['basicSalary'], payroll_data['overtimePay'],
                payroll_data['deductions'], payroll_data['netSalary']))
            self.connection.commit()
            print("Payroll added successfully.")
        except Exception as e:
            print(f"Failed to add payroll: {e}")

    def taxHelp(self, employeeID, start, end):
        year = datetime.now().year
        taxService = TaxService()
        tax = taxService.helpTax(employeeID, year)
        taxAmount = tax.taxAmount
        pf = tax.deductions
        deductions = 0.0

        query = "SELECT COUNT(EmployeeID) AS NumberofRecords FROM Payroll WHERE EmployeeID = ? AND YEAR(PayPeriodEndDate) = ?"
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query, (employeeID, year))
            result = cursor.fetchone()
            if result:
                months = result[0]
                deductions = (taxAmount / months) + (pf / months)

        self.deduction(employeeID, deductions)

    def deduction(self, employeeID, deductions):
        query = "UPDATE Payroll SET Deductions = ? WHERE EmployeeID = ?"
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query, (deductions, employeeID))

    def get_payrolls_for_employee(self, employee_id):
        payroll_list = []
        try:
            query = "SELECT e.FirstName, e.LastName, p.PayrollID, p.PayPeriodStartDate, p.PayPeriodEndDate, " \
                    "p.BasicSalary, p.OvertimePay, p.Deductions, p.NetSalary " \
                    "FROM Employee e INNER JOIN Payroll p ON e.EmployeeID = p.EmployeeID " \
                    "WHERE e.EmployeeID = ?"
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute(query, (employee_id,))
                results = cursor.fetchall()
                for result in results:
                    # Create a Payroll object using the fetched data
                    payroll = Payroll(result[2], employee_id, result[3], result[4], result[5], result[6], result[7],
                                      result[8])
                    payroll_list.append(payroll)
            if not payroll_list:
                print(f"No payrolls found for Employee ID {employee_id}")
        except Exception as e:
            # Handle exceptions gracefully
            print(f"Error occurred while fetching payrolls for employee {employee_id}: {e}")
            return None  # Return None to indicate failure
        return payroll_list

    def getPayrollsforPeriod(self, startDate, endDate):
        payrollList = []
        query = "SELECT e.FirstName, e.LastName, p.PayrollID, p.BasicSalary, p.OvertimePay, p.Deductions, p.NetSalary FROM Employee e INNER JOIN Payroll p ON e.EmployeeID = p.EmployeeID WHERE p.PayPeriodStartDate >= ? AND p.PayPeriodEndDate <= ?"
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query, (startDate, endDate))
            results = cursor.fetchall()
            for result in results:
                payroll = Payroll(
                    payroll_id=result[2],
                    employee_id=result[0],
                    pay_period_start_date=startDate,
                    pay_period_end_date=endDate,
                    basic_salary=result[3],
                    overtime_pay=result[4],
                    deductions=result[5],
                    net_salary=result[6]
                )
                payrollList.append(payroll)
        return payrollList
