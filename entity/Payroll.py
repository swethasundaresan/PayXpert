class Payroll:
    def __init__(self, payroll_id=None, employee_id=None, pay_period_start_date=None,
                 pay_period_end_date=None, basic_salary=None, overtime_pay=None,
                 deductions=None, net_salary=None):
        self._payroll_id = payroll_id
        self._employee_id = employee_id
        self._pay_period_start_date = pay_period_start_date
        self._pay_period_end_date = pay_period_end_date
        self._basic_salary = basic_salary
        self._overtime_pay = overtime_pay
        self._deductions = deductions
        self._net_salary = net_salary

    # Getter methods
    def get_payroll_id(self):
        return self._payroll_id

    def get_employee_id(self):
        return self._employee_id

    def get_pay_period_start_date(self):
        return self._pay_period_start_date

    def get_pay_period_end_date(self):
        return self._pay_period_end_date

    def get_basic_salary(self):
        return self._basic_salary

    def get_overtime_pay(self):
        return self._overtime_pay

    def get_deductions(self):
        return self._deductions

    def get_net_salary(self):
        return self._net_salary

    # Setter methods
    def set_payroll_id(self, payroll_id):
        self._payroll_id = payroll_id

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def set_pay_period_start_date(self, pay_period_start_date):
        self._pay_period_start_date = pay_period_start_date

    def set_pay_period_end_date(self, pay_period_end_date):
        self._pay_period_end_date = pay_period_end_date

    def set_basic_salary(self, basic_salary):
        self._basic_salary = basic_salary

    def set_overtime_pay(self, overtime_pay):
        self._overtime_pay = overtime_pay

    def set_deductions(self, deductions):
        self._deductions = deductions

    def set_net_salary(self, net_salary):
        self._net_salary = net_salary
