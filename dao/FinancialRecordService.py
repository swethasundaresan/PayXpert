from entity.FinancialRecord import FinancialRecord

from datetime import datetime

from exception.FinancialRecordException import FinancialRecordException
from util.DBPropertyUtil import DBPropertyUtil


class FinancialRecordService:
    def __init__(self):
        self.connection = DBPropertyUtil.getDBConn()
        self.financial_record_list = []

    def add_financial_record(self, record_id, employee_id, record_date, description, amount, record_type):
        try:
            if record_type == "income" or record_type == "deductions":
                self.insert_record(record_id, employee_id, record_date, description, amount, record_type)
                print(
                    f"RecordID: {record_id}, EmployeeId: {employee_id}, Record date: {record_date}, Description: {description}, Amount: {amount}, Record type: {record_type}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def insert_record(self, record_id, employee_id, record_date, description, amount, record_type):
        try:
            query = "INSERT INTO financialrecord (RecordID, EmployeeID, RecordDate, Description, Amount, RecordType) VALUES (?, ?, ?, ?, ?, ?)"
            with self.connection.cursor() as cursor:
                cursor.execute(query, (record_id, employee_id, record_date, description, amount, record_type))
            self.connection.commit()
            print("Row inserted successfully")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_financial_record_by_id(self, record_id):
        try:
            query = "SELECT RecordID,EmployeeID, RecordDate, Description, Amount, RecordType FROM financialrecord WHERE RecordID = ?"
            with self.connection.cursor() as cursor:
                cursor.execute(query, (record_id,))
                result = cursor.fetchone()
                if result:
                    financial_record = FinancialRecord(result[0],result[1], result[2], result[3], result[4],
                                                       result[5])
                    self.record_by_id(financial_record)
                    return financial_record
                else:
                    raise FinancialRecordException(f"Financial record with ID {record_id} not found")
        except Exception as e:
            print(f"An error occurred: {e}")

    def record_by_id(self, financial_record):
        print(f"RecordID: {financial_record.get_record_id()}, EmployeeID: {financial_record.get_employee_id()}, Record date: {financial_record.get_record_date()}, "
              f"Description: {financial_record.get_description()}, Amount: {financial_record.get_amount()}, "
              f"Record type: {financial_record.get_record_type()}")

    def get_financial_records_for_employee(self, employee_id):
        try:
            financial_for_employee_list = []
            query = "SELECT * FROM financialrecord WHERE EmployeeID = ?"
            with self.connection.cursor() as cursor:
                cursor.execute(query, (employee_id,))
                results = cursor.fetchall()
                for result in results:
                    financial_record = FinancialRecord(result[0], result[1], result[2], result[3], result[4], result[5])
                    financial_for_employee_list.append(financial_record)
            self.financial_for_employee(financial_for_employee_list)
            return financial_for_employee_list
        except Exception as e:
            print(f"An error occurred: {e}")

    def financial_for_employee(self, financial_record_list):
        for financial_record in financial_record_list:
            print(f"Record ID: {financial_record.get_record_id()}, EmployeeID: {financial_record.get_employee_id()}, "
                  f"Record date: {financial_record.get_record_date()}, Description: {financial_record.get_description()}, "
                  f"Amount: {financial_record.get_amount()}, Record type: {financial_record.get_record_type()}")

    def get_financial_records_for_date(self, record_date):
        try:
            financial_records_list = []
            query = "SELECT * FROM financialrecord WHERE RecordDate >= ?"
            with self.connection.cursor() as cursor:
                cursor.execute(query, (record_date,))
                results = cursor.fetchall()
                for result in results:
                    # Pass all relevant attributes to the FinancialRecord constructor
                    financial_record = FinancialRecord(result[0], result[1], result[2], result[3], result[4], result[5])
                    financial_records_list.append(financial_record)
            self.financial_for_employee(financial_records_list)
            return financial_records_list
        except Exception as e:
            print(f"An error occurred: {e}")

