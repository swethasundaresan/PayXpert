import unittest


class PayXpertTestCase(unittest.TestCase):
    def test_calculate_gross_salary_for_employee(self):
        employee_data = {
            'name': 'John Doe',
            'salary': '5000',
            'bonus': '500'
        }
        gross_salary = self.calculate_gross_salary(employee_data['salary'], employee_data['bonus'])
        self.assertEqual(gross_salary, 5500)

    def test_calculate_net_salary_after_deuctions(self):
        gross_salary = 5500
        deductions = 750
        net_salary = self.calculate_net_salary(gross_salary, deductions)
        self.assertEqual(net_salary, 4750)

    def test_verify_tax_calculation_for_high_income_employee(self):
        gross_salary = 10000
        tax = self.calculate_tax(gross_salary)
        self.assertEqual(tax, 7500)

    def test_process_payroll_for_multiple_employees(self):
        employees = [
            {'name': 'John Doe', 'salary': '5000', 'bonus': '500'},
            {'name': 'Jane Smith', 'salary': '6000', 'bonus': '800'}
        ]
        total_payroll = self.process_payroll(employees)
        self.assertEqual(total_payroll, 12300)

    def test_verify_error_handling_for_invalid_employee_data(self):
        invalid_employee_data = {
            'name': 'John Doe',
            'salary': 'Invalid',
            'bonus': 200
        }
        error_message = self.handle_invalid_employee_data(invalid_employee_data)
        self.assertEqual(error_message, "Invalid Salary Data for Employee: John Doe")

    def calculate_gross_salary(self, salary, bonus):
        return int(salary) + int(bonus)

    def calculate_net_salary(self, gross_salary, deductions):
        return gross_salary - deductions

    def calculate_tax(self, gross_salary):
        return gross_salary * 0.75

    def process_payroll(self, employees):
        total_payroll = 0
        for employee in employees:
            total_payroll = total_payroll + int(employee['salary']) + int(employee['bonus'])
        return total_payroll

    def handle_invalid_employee_data(self, employee_data):
        if not isinstance(employee_data['salary'], int):
            return f"Invalid Salary Data for Employee: {employee_data['name']}"


if __name__ == '__main__':
    unittest.main()
