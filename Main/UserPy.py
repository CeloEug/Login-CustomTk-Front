class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def get_login(self):
        return self.login

    def get_password(self):
        return self.password

    def set_login(self, login):
        self.login = login

    def set_password(self, password):
        self.password = password

    def get_credentials(self):
        return f"{self.login}\n{self.password}\n"