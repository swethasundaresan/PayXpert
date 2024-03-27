from entity import Payroll
from exception import EmployeeNotFoundException, InvalidInputException, PayrollGenerationException
from typing import List
import datetime


class IPayrollService:
    def generate_payroll(self, employee_id: int, start_date: datetime.date, end_date: datetime.date) -> None:
        raise EmployeeNotFoundException

    def get_payroll_by_id(self, payroll_id: int) -> Payroll:
        raise InvalidInputException

    def get_payrolls_for_employee(self, employee_id: int) -> List[Payroll]:
        raise EmployeeNotFoundException

    def get_payrolls_for_period(self, start_date: datetime.date, end_date: datetime.date) -> List[Payroll]:
        pass
