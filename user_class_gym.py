from datetime import datetime, date
from commons import validate_id, users_list


class Client:
    def __init__(self, id: int, name: str, last_name: str, age: int, phone_number = int):
        self.__id = validate_id(id)
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self.__phone_number = phone_number
        self.__created_at = datetime
        self.__membership_data = []
        self.__is_training = False
        self.__assigned_locker = 0
        """self.__membership_active = False"""
        """ self.membership_date = membership_date """

    @property
    def get_id(self):
        return self.__id

    @get_id.setter
    def set_id(self, _id):
        if isinstance(_id, int) and _id >= 0:
            self.__id = _id
        else:
            raise ValueError("Invalid user ID")

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def set_name(self, _name):
        self.__name = _name

    @property
    def get_last_name(self):
        return self.__last_name
    
    @get_last_name.setter
    def set_last_name(self, _last_name):
        self.__last_name = _last_name

    @property
    def get_age(self):
        return self.__age
    
    @get_age.setter
    def set_age(self, _age):
        if isinstance(_age, int) and _age >= 0:
            self.__age = _age
        else:
            raise ValueError("Invalid user age")
        
    @property
    def get_phone_number(self):
        return self.__phone_number
    
    @get_phone_number.setter
    def set_phone_number(self, _phone_number):
        if isinstance(_phone_number, int):
            self.__phone_number = _phone_number
        else:
            raise ValueError("Invalid phone number")
        
    @property
    def get_created_at(self):
        return self.__created_at
    
    @get_created_at.setter
    def set_created_at(self, _created_at):
        self.__created_at = _created_at


    @property
    def get_membership_data(self):
        return self.__membership_data
    
    @get_membership_data.setter
    def set_membership_data(self, _membership_data):
        if isinstance(_membership_data, dict):
            self.__membership_data = _membership_data
        else:
            raise ValueError("Invalid membership data")
        
    @property
    def get_is_training(self):
        return self.__is_training
    
    @get_is_training.setter
    def set_is_training(self, _is_training):
        if isinstance(_is_training, bool):
            self.__is_training = _is_training
        else:
            raise ValueError("Invalid is_training value")

    @property
    def get_assigned_locker(self):
        return self.__assigned_locker
    
    @get_assigned_locker.setter
    def set_assigned_locker(self, _get_assigned_locker):
        if isinstance(_get_assigned_locker, int):
            self.__assigned_locker = _get_assigned_locker
        else:
            raise ValueError("Invalid locker number")
        


# Crear una lista de objetos Client
clients = [
    Client(1, "John", "Doe", 30, 1234567890),
    Client(2, "Jane", "Smith", 25, 2345678901),
    Client(3, "Jim", "Beam", 35, 3456789012),
    Client(4, "Jack", "Daniels", 40, 4567890123),
    Client(5, "Jose", "Cuervo", 28, 5678901234)
]

# Probar los atributos y setters/getters
for client in clients:
    print(f"ID: {client.get_id}, Name: {client.get_name}, Last Name: {client.get_last_name}, Age: {client.get_age}, Phone Number: {client.get_phone_number}")
    
    # Modificar algunos atributos usando setters
    client.set_age = client.get_age + 1  # Incrementar la edad en 1
    client.set_phone_number = client.get_phone_number + 1  # Incrementar el número de teléfono en 1

    print(f"Updated Age: {client.get_age}, Updated Phone Number: {client.get_phone_number}")


    """ @property
    def get_membership_date(self):
        return self.membership_date

    @get_membership_date.setter
    def set_membership_date(self, _date):
        self.membership_date = _date

    @property
    def get_membership_active(self):
        return self.membership_active

    @get_membership_active.setter
    def set_membership_active(self, status):
        self.get_membership_active = status """

    """ def handle_traning(self):
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
third_user = Client(2322012, "Santiago", "Molina", 33, "2019-05-24")
"""" save_user([firts_user, second_user])"
# printing_users() """
# """ print(firts_user.get_membership_active)
# firts_user.handle_active()
# print(firts_user.get_membership_active) """
