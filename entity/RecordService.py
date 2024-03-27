class FinancialRecord:
    def __init__(self, record_id=None, employee_id=None, record_date=None, description=None, amount=None, record_type=None):
        self._record_id = record_id
        self._employee_id = employee_id
        self._record_date = record_date
        self._description = description
        self._amount = amount
        self._record_type = record_type

    # Getter methods
    def get_record_id(self):
        return self._record_id

    def get_employee_id(self):
        return self._employee_id

    def get_record_date(self):
        return self._record_date

    def get_description(self):
        return self._description

    def get_amount(self):
        return self._amount

    def get_record_type(self):
        return self._record_type

    # Setter methods
    def set_record_id(self, record_id):
        self._record_id = record_id

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def set_record_date(self, record_date):
        self._record_date = record_date

    def set_description(self, description):
        self._description = description

    def set_amount(self, amount):
        self._amount = amount

    def set_record_type(self, record_type):
        self._record_type = record_type
