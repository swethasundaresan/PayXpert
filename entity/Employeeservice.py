from abc import ABC, abstractmethod

class IEmployeeService(ABC):
    @abstractmethod
    def get_employee_by_id(self, employee_id):
        pass
    
    @abstractmethod
    def get_all_employees(self):
        pass
    
    @abstractmethod
    def add_employee(self, employee):
        pass
    
    @abstractmethod
    def update_employee(self, employee):
        pass
    
    @abstractmethod
    def remove_employee(self, employee_id):
        pass

class EmployeeService(IEmployeeService):
    def __init__(self):
        # Assuming you might have some data storage mechanism or API calls here
        self._employees = {}

    def get_employee_by_id(self, employee_id):
        return self._employees.get(employee_id)

    def get_all_employees(self):
        return list(self._employees.values())

    def add_employee(self, employee):
        if employee.get_employee_id() not in self._employees:
            self._employees[employee.get_employee_id()] = employee
            return True
        return False

    def update_employee(self, employee):
        if employee.get_employee_id() in self._employees:
            self._employees[employee.get_employee_id()] = employee
            return True
        return False

    def remove_employee(self, employee_id):
        if employee_id in self._employees:
            del self._employees[employee_id]
            return True
        return False
