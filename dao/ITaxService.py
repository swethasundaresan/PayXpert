from entity import Tax
from exception import EmployeeNotFoundException
from typing import List


class ITaxService:
    def calculate_tax(self, employee_id: int, tax_year: int) -> Tax:
        pass

    def get_tax_by_id(self, tax_id: int) -> Tax:
        pass

    def get_taxes_for_employee(self, employee_id: int) -> List[Tax]:

        raise EmployeeNotFoundException

    def get_taxes_for_year(self, tax_year: int) -> List[Tax]:
        pass
