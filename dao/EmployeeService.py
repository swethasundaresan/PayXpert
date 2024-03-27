from entity.Employee import Employee
from exception.EmployeeNotFoundException import EmployeeNotFoundException
from util.DBPropertyUtil import DBPropertyUtil


class EmployeeService:
    def __init__(self):
        self.connection = DBPropertyUtil.getDBConn()

    def get_employee_by_id(self, EmployeeID):
        try:
            query = "SELECT * FROM employee WHERE EmployeeID = ?"
            with self.connection.cursor() as cursor:
                cursor.execute(query, (EmployeeID,))
                result = cursor.fetchone()
                if result:
                    employee = Employee(employee_id=result[0],
                                        first_name=result[1],
                                        last_name=result[2],
                                        date_of_birth=result[3],
                                        gender=result[4],
                                        email=result[5],
                                        phone_number=result[6],
                                        address=result[7],
                                        position=result[8],
                                        joining_date=result[9],
                                        termination_date=result[10])
                    self.get_details(employee)
                else:
                    raise EmployeeNotFoundException(f"Employee with ID {EmployeeID} not found")
        except EmployeeNotFoundException as e:
            print(e)
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_all_employees(self):
        try:
            query = "SELECT * FROM employee"
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                results = cursor.fetchall()
                for result in results:
                    employee = Employee(result[0], result[1], result[2], result[3], result[4], result[5], result[6],
                                        result[7], result[8], result[9], result[10])
                    self.get_details(employee)
        except Exception as e:
            print(f"An error occurred: {e}")


    def add_employee(self, employee_data):
        try:
            query = "INSERT INTO employee (EmplOyeeID,FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            with self.connection.cursor() as cursor:
                cursor.execute(query, (
                employee_data.get_employee_id(),employee_data.get_first_name(), employee_data.get_last_name(), employee_data.get_date_of_birth(),
                employee_data.get_gender(), employee_data.get_email(), employee_data.get_phone_number(),
                employee_data.get_address(), employee_data.get_position(), employee_data.get_joining_date(),
                employee_data.get_termination_date()))
            self.connection.commit()
            print("Employee added successfully.")
        except Exception as e:
            print(f"Failed to add employee: {e}")

    def update_employee(self, employee_id, updated_employee_data):
        try:
            query = "UPDATE employee SET FirstName=?, LastName=?, DateOfBirth=?, Gender=?, Email=?, PhoneNumber=?, Address=?, Position=?, JoiningDate=?, TerminationDate=? WHERE EmployeeID=?"
            with self.connection.cursor() as cursor:
                cursor.execute(query, (updated_employee_data['first_name'], updated_employee_data['last_name'],
                                       updated_employee_data['date_of_birth'],
                                       updated_employee_data['gender'], updated_employee_data['email'],
                                       updated_employee_data['phone_number'],
                                       updated_employee_data['address'], updated_employee_data['position'],
                                       updated_employee_data['joining_date'],
                                       updated_employee_data['termination_date'], employee_id))
            self.connection.commit()
            print("Employee updated successfully.")
        except Exception as e:
            print(f"Failed to update employee: {e}")

    def remove_employee(self, employee_id):
        try:
            query = "DELETE FROM employee WHERE EmployeeID = ?"
            with self.connection.cursor() as cursor:
                cursor.execute(query, (employee_id,))
            self.connection.commit()
            print("Employee removed successfully.")
        except Exception as e:
            print(f"Failed to remove employee: {e}")

    def get_details(self, employee):
        print("------------------------------------")
        print("EmployeeID:", employee.get_employee_id())
        print("FirstName:", employee.get_first_name())
        print("LastName:", employee.get_last_name())
        print("DateOfBirth:", employee.get_date_of_birth())
        print("Gender:", employee.get_gender())
        print("Email:", employee.get_email())
        print("PhoneNumber:", employee.get_phone_number())
        print("Address:", employee.get_address())
        print("Position:", employee.get_position())
        print("JoiningDate:", employee.get_joining_date())
        print("TerminationDate:", employee.get_termination_date())
