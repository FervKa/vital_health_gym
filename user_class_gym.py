from datetime import datetime, date
from commons import validate_id

users_list = []


class Client:
    def __init__(self, id: int, name: str, last_name: str, age: int, membership_date):
        self.id = validate_id(id)
        self.name = name
        self.last_name = last_name
        self.age = age
        self.is_training = False
        self.membership_active = False
        self.membership_date = membership_date

    @property
    def get_id(self):
        return self.id

    @get_id.setter
    def set_id(self, _id):
        if isinstance(_id, int) and _id >= 0:
            self.id = _id
        else:
            raise ValueError("Invalid user ID")

    @property
    def get_name(self):
        return self.name

    @get_name.setter
    def set_name(self, _name):
        self.name = _name

    @property
    def get_membership_date(self):
        return self.membership_date

    @get_membership_date.setter
    def set_membership_date(self, date):
        self.membership_date = date

    @property
    def get_membership_active(self):
        return self.membership_active

    @get_membership_active.setter
    def set_membership_active(self, status):
        self.get_membership_active = status

    def handle_traning(self):
        if not self.is_training:
            print(f"User {self.name} {self.last_name} joined the gym")
        else:
            print(f"User {self.name} {self.last_name} left the gym")
        self.is_training = not self.is_training

    def handle_active(self):
        print(
            f"User {self.name} {self.last_name} is { 'Active' if self.membership_active else 'Inactive'}"
        )
        self.membership_active = not self.membership_active
        print(
            f"Now, {self.name} {self.last_name} is { 'Active' if self.membership_active else 'Inactive'}"
        )

    def create_instance(self):
        return Client(
            self.id, self.name, self.last_name, self.age, self.membership_date
        )


def printing_users():
    for user in users_list:
        print(f"User ID: {user.get_id}, Name: {user.get_name}")


def save_user(users):
    if isinstance(users, Client):
        users_list.append(users)
    elif isinstance(users, list):
        for user in users:
            users_list.append(user)


firts_user = Client(3291121, "Oscar", "Murillo", 23, "2020-01-30")
second_user = Client(3123223, "Carlos", "Jaramillo", 32, "2021-03-20")
""" firts_user.handle_traning() """
save_user([firts_user, second_user])
printing_users()
print(firts_user.get_membership_active)
firts_user.handle_active()
print(firts_user.get_membership_active)
