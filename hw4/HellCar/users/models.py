from django.db import models

dict_of_users = dict()


class User:

    def __init__(self, idx: int, login: str, mail: str):
        self.id = idx
        self.login = login
        self.mail = mail
