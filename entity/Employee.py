import datetime

class Employee:
    def __init__(self, employee_id=None, first_name=None, last_name=None, date_of_birth=None,
                 gender=None, email=None, phone_number=None, address=None, position=None,
                 joining_date=None, termination_date=None):
        self._employee_id = employee_id
        self._first_name = first_name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._gender = gender
        self._email = email
        self._phone_number = phone_number
        self._address = address
        self._position = position
        self._joining_date = joining_date
        self._termination_date = termination_date

    def calculate_age(self):
        today = datetime.date.today()
        dob = self._date_of_birth
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age

    # Getter methods
    def get_employee_id(self):
        return self._employee_id

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_date_of_birth(self):
        return self._date_of_birth

    def get_gender(self):
        return self._gender

    def get_email(self):
        return self._email

    def get_phone_number(self):
        return self._phone_number

    def get_address(self):
        return self._address

    def get_position(self):
        return self._position

    def get_joining_date(self):
        return self._joining_date

    def get_termination_date(self):
        return self._termination_date

    # Setter methods
    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def set_date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    def set_gender(self, gender):
        self._gender = gender

    def set_email(self, email):
        self._email = email

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def set_address(self, address):
        self._address = address

    def set_position(self, position):
        self._position = position

    def set_joining_date(self, joining_date):
        self._joining_date = joining_date

    def set_termination_date(self, termination_date):
        self._termination_date = termination_date
