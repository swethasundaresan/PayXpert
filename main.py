from dao.EmployeeService import EmployeeService
from dao.PayrollService import PayrollService
from dao.TaxService import TaxService
from dao.FinancialRecordService import FinancialRecordService
from entity.Employee import Employee


def print_menu():
    print("1. Add Employee")
    print("2. Get Employee by ID")
    print("3. Get All Employees")
    print("4. Update Employee")
    print("5. Remove Employee")
    print("6. Get Payroll by ID")
    print("7. Add Payroll")
    print("8. Get Payrolls for Employee")
    print("9. Get Payrolls for Period")
    print("10. Calculate Tax")
    print("11. Get Financial Record by ID")
    print("12. Add Financial Record")
    print("13. Get Financial Records for Employee")
    print("14. Get Financial Records for Date")
    print("15. Exit")

def main():
    employee_service = EmployeeService()
    payroll_service = PayrollService()
    tax_service = TaxService()
    financial_record_service = FinancialRecordService()

    while True:
        print("\nEmployee and Financial Record Management System")
        print_menu()
        choice = input("Enter your choice (1-15): ")
        if choice == "1":
            # Add employee functionality
            employee_id = input("Enter Employee ID: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
            gender = input("Enter gender: ")
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")
            address = input("Enter address: ")
            position = input("Enter position: ")
            joining_date = input("Enter joining date (YYYY-MM-DD): ")
            termination_date = input("Enter termination date (YYYY-MM-DD): ")

            employee_data = Employee(employee_id=employee_id,first_name=first_name, last_name=last_name, date_of_birth=date_of_birth,
                                     gender=gender,
                                     email=email, phone_number=phone_number, address=address, position=position,
                                     joining_date=joining_date, termination_date=termination_date)

            employee_service.add_employee(employee_data)

        elif choice == "2":

            employee_id = input("Enter employee ID: ")

            employee_service.get_employee_by_id(employee_id)

        elif choice == "3":
            # Get all employees functionality
            employee_service.get_all_employees()




        elif choice == "4":

            try:
                employee_id = int(input("Enter employee ID to update: "))
                updated_employee_data = {}  # Initialize an empty dictionary
                print("Enter updated data for the employee:")
                updated_employee_data['first_name'] = input("First Name: ")
                updated_employee_data['last_name'] = input("Last Name: ")
                updated_employee_data['date_of_birth'] = input("Date of Birth (YYYY-MM-DD): ")
                updated_employee_data['gender'] = input("Gender: ")
                updated_employee_data['email'] = input("Email: ")
                updated_employee_data['phone_number'] = input("Phone Number: ")
                updated_employee_data['address'] = input("Address: ")
                updated_employee_data['position'] = input("Position: ")
                updated_employee_data['joining_date'] = input("Joining Date (YYYY-MM-DD): ")
                updated_employee_data['termination_date'] = input("Termination Date (YYYY-MM-DD): ")
                employee_service.update_employee(employee_id, updated_employee_data)

            except ValueError:

                print("Invalid input. Please enter a valid employee ID.")




        elif choice == "5":
            # Remove employee functionality
            employee_id = int(input("Enter employee ID to remove: "))
            employee_service.remove_employee(employee_id)


        elif choice == "6":

            payroll_id = int(input("Enter payroll ID: "))
            payroll = payroll_service.get_payroll_by_id(payroll_id)
            if payroll:
                print("Payroll information:")
                print("Payroll ID:", payroll.get_payroll_id())
                print("Employee ID:", payroll.get_employee_id())
                print("Pay Period Start Date:", payroll.get_pay_period_start_date())
                print("Pay Period End Date:", payroll.get_pay_period_end_date())
                print("Basic Salary:", payroll.get_basic_salary())
                print("Overtime Pay:", payroll.get_overtime_pay())
                print("Deductions:", payroll.get_deductions())
                print("Net Salary:", payroll.get_net_salary())
            else:
                print("No payroll found with ID", payroll_id)


        elif choice == "7":
            # Add payroll functionality
            payroll_data = {
                'payrollID': input("Enter Payroll ID: "),
                'employeeID': int(input("Enter employee ID: ")),
                'payPeriodStartDate': input("Enter pay period start date (YYYY-MM-DD): "),
                'payPeriodEndDate': input("Enter pay period end date (YYYY-MM-DD): "),
                'basicSalary': float(input("Enter basic salary: ")),
                'overtimePay': float(input("Enter overtime pay: ")),
                'deductions': float(input("Enter deductions: ")),
                'netSalary': float(input("Enter net salary: "))
            }
            payroll_service.addPayroll(payroll_data)


        elif choice == "8":

            employee_id = int(input("Enter employee ID: "))
            payroll_service = PayrollService()
            payrolls = payroll_service.get_payrolls_for_employee(employee_id)
            if payrolls:
                for payroll in payrolls:
                    print("Payroll ID:", payroll.get_payroll_id())
                    print("Pay Period Start Date:", payroll.get_pay_period_start_date())
                    print("Pay Period End Date:", payroll.get_pay_period_end_date())
                    print("Basic Salary:", payroll.get_basic_salary())
                    print("Overtime Pay:", payroll.get_overtime_pay())
                    print("Deductions:", payroll.get_deductions())
                    print("Net Salary:", payroll.get_net_salary())
                    print("------------------------------------")
            else:
                print("No payrolls found for Employee ID", employee_id)


        elif choice == "9":
            # Get payrolls for a specific period
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            payrolls = payroll_service.getPayrollsforPeriod(start_date, end_date)
            if payrolls:
                for payroll in payrolls:
                    print("Payroll ID:", payroll.get_payroll_id())
                    print("Employee ID:", payroll.get_employee_id())
                    print("Pay Period Start Date:", payroll.get_pay_period_start_date())
                    print("Pay Period End Date:", payroll.get_pay_period_end_date())
                    print("Basic Salary:", payroll.get_basic_salary())
                    print("Overtime Pay:", payroll.get_overtime_pay())
                    print("Deductions:", payroll.get_deductions())
                    print("Net Salary:", payroll.get_net_salary())
                    print("------------------------------------")
            else:
                print("No payrolls found for the specified period.")


        elif choice == "10":
            # Calculate tax for a specific employee and year
            employee_id = int(input("Enter employee ID: "))
            tax_year = int(input("Enter tax year: "))
            tax_service.calculateTax(employee_id, tax_year)


        elif choice == "11":
            # Get financial record by ID functionality
            record_id = int(input("Enter record ID: "))
            financial_record_service.get_financial_record_by_id(record_id)


        elif choice == "12":
            # Add financial record functionality
            financial_record_data = {
                # Provide fields required for adding a financial record
                "record_id": int(input("Enter record id: ")),
                "employee_id": int(input("Enter employee ID: ")),
                "record_date": input("Enter record date (YYYY-MM-DD): "),
                "description": input("Enter description: "),
                "amount": int(input("Enter the amount: " )),
                "record_type": input("Enter record type: ")
            }
            financial_record_service.add_financial_record(**financial_record_data)

        elif choice == "13":
            # Get financial records for employee functionality
            employee_id = int(input("Enter employee ID: "))
            financial_record_service.get_financial_records_for_employee(employee_id)

        elif choice == "14":
            # Get financial records for date functionality
            record_date = input("Enter record date (YYYY-MM-DD): ")
            financial_record_service.get_financial_records_for_date(record_date)

        elif choice == "15":
            print("Exiting Employee and Financial Record Management System.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 15.")

if __name__ == "__main__":
            main()