class DatabaseContext:
    def __init__(self, host=None, port=None, username=None, password=None, database_name=None):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._database_name = database_name

    # Getter methods
    def get_host(self):
        return self._host

    def get_port(self):
        return self._port

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_database_name(self):
        return self._database_name

    # Setter methods
    def set_host(self, host):
        self._host = host

    def set_port(self, port):
        self._port = port

    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password

    def set_database_name(self, database_name):
        self._database_name = database_name


