class SystemUser:
    def __init__(self,
                 id: int,
                 name: str,
                 login: str,
                 password: str,
                 function: str):
                 
        self.user_id = id
        self.username = name
        self.login = login
        self.password = password
        self.user_function = function