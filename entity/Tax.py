class Tax:
    def __init__(self, tax_id=None, employee_id=None, tax_year=None, taxable_income=None, tax_amount=None):
        self._tax_id = tax_id
        self._employee_id = employee_id
        self._tax_year = tax_year
        self._taxable_income = taxable_income
        self._tax_amount = tax_amount


    # Getter methods
    def get_tax_id(self):
        return self._tax_id

    def get_employee_id(self):
        return self._employee_id

    def get_tax_year(self):
        return self._tax_year

    def get_taxable_income(self):
        return self._taxable_income

    def get_tax_amount(self):
        return self._tax_amount

    # Setter methods
    def set_tax_id(self, tax_id):
        self._tax_id = tax_id

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def set_tax_year(self, tax_year):
        self._tax_year = tax_year

    def set_taxable_income(self, taxable_income):
        self._taxable_income = taxable_income

    def set_tax_amount(self, tax_amount):
        self._tax_amount = tax_amount

