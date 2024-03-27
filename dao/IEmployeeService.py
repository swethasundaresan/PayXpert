from abc import ABC, abstractmethod
from entity import Employee
from exception import EmployeeNotFoundException, InvalidInputException
import typing


class IEmployeeService(ABC):
    @abstractmethod
    def get_employee_by_id(self, employee_id: int) -> typing.Optional:
        raise EmployeeNotFoundException
        pass


    @abstractmethod
    def get_all_employees(self) -> None:
        pass



    @abstractmethod
    def add_employee(self, employee: Employee) -> None:
        raise InvalidInputException
        pass

    @abstractmethod
    def update_employee(self, employee: Employee) -> None:
        raise InvalidInputException
        pass

    @abstractmethod
    def remove_employee(self, employee_id: int) -> None:
        raise InvalidInputException
        pass
