from datetime import date
from commons import validate_id, get_current_date
from membership_class import Membership


class Client:
    def __init__(
        self,
        client_id: int,
        name: str,
        last_name: str,
        age: int,
        phone_number: str,
        membership_data: object,
        membership_active: bool,
        is_active: bool,
        created_at: date,
        date_last_payment: date,
        locker_data: object,
    ):
        self.__client_id = validate_id(client_id)
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        if len(phone_number) == 10:
            self.__phone_number = phone_number
        else:
            raise ValueError(f"Error: Number must have 10 numbers, in user: {name}")
        self.__membership_data = membership_data
        self.__is_training = False
        self.__assigned_locker = None
        self.__membership_active = membership_active
        self.__is_active = is_active
        """ self.membership_date = membership_date """
        if created_at:
            self.__created_at = created_at
        else:
            self.__created_at = get_current_date()
        if date_last_payment:
            self.__date_last_payment = date_last_payment
        else:
            self.__date_last_payment = ""

        self.__remaining_days = membership_data.get_membership_duration

        if locker_data is not None:
            self.__assigned_locker = locker_data.get_locker_id
            self.__locker_data = locker_data
            """ print(f"Locker assigned: {self.__assigned_locker}") """
            """ self.__is_training = locker_data.get("is_training") """
        else:
            self.__assigned_locker = None
            self.__locker_data = None
            """ print(f"Assigned locker: {self.__assigned_locker}") """

        """ if is_training and (locker_data is not None):
            print(f"Locker state: {locker_data.get_locker_state}")
            locker_data.set_locker_state = True
            print(f"From training {is_training}: {locker_data.get_locker_id}")
        else:
            locker_data.set_state(False)
            print(locker_data)
            print(f"From training: {is_training}") """

    @property
    def get_client_id(self):
        return self.__client_id

    @get_client_id.setter
    def set_id(self, _id):
        if isinstance(_id, int) and _id >= 0:
            self.__client_id = _id
        else:
            raise ValueError("Invalid user ID")

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def set_name(self, _name):
        self.__name = _name.capitalize()

    @property
    def get_last_name(self):
        return self.__last_name

    @get_last_name.setter
    def set_last_name(self, _last_name):
        print(f"Estoy entrando: {_last_name}")
        self.__last_name = _last_name.capitalize()

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
        self.__phone_number = _phone_number

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
        if isinstance(_membership_data, Membership) or _membership_data is None:
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
        if isinstance(_get_assigned_locker, int) or _get_assigned_locker is None:
            self.__assigned_locker = _get_assigned_locker
        else:
            raise ValueError("Invalid locker number")

    @property
    def get_membership_active(self):
        return self.__membership_active

    @get_membership_active.setter
    def set_membership_active(self, status):
        self.__membership_active = status

    @property
    def get_is_active(self):
        return self.__is_active

    @get_is_active.setter
    def set_is_active(self, _is_active):
        if isinstance(_is_active, bool):
            self.__is_active = _is_active
        else:
            raise ValueError("Invalid is_active value")

    @property
    def get_date_last_payment(self):
        return self.__date_last_payment

    @get_date_last_payment.setter
    def set_date_last_payment(self, new_date_last_payment):
        self.__date_last_payment = new_date_last_payment

    @property
    def get_locker_data(self):
        return self.__locker_data

    @get_locker_data.setter
    def set_locker_data(self, data):
        self.__locker_data = data

    @property
    def get_remaining_days(self):
        return self.__remaining_days

    @get_remaining_days.setter
    def set_remaining_days(self, days):
        self.__remaining_days = days
