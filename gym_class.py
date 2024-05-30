from user_class_gym import Client
from commons import get_current_date,format_in_currency, separator_string


class Gym:
    def __init__(self, nit, name, adress):
        self.nit = nit
        self.name = name
        self.adress = adress
        self.__clients_list = []
        self.__locker_list = []
        self.__membership_list = []

    @property
    def get_nit(self):
        return self.nit

    @get_nit.setter
    def set_nit(self, nit):
        self.nit = nit

    @property
    def get_name(self):
        return self.name

    @get_name.setter
    def set_name(self, name):
        self.name = name

    @property
    def get_adress(self):
        return self.adress

    @get_adress.setter
    def set_adress(self, adress):
        self.adress = adress

    @property
    def get_clients_list(self):
        return self.__clients_list

    @get_clients_list.setter
    def set_clients_list(self, clients_list):
        self.__clients_list = clients_list

    @property
    def get_locker_list(self):
        return self.locker_list

    @get_locker_list.setter
    def set_locker_list(self, locker_list):
        self.locker_list = locker_list

    @property
    def get_membership_list(self):
        return self.__membership_list

    @get_membership_list.setter
    def set_membership_list(self, membership_list):
        self.__membership_list = membership_list

    def get_empty_lockers(self, to_print = False):
        empty_lockers = list(
            filter(lambda locker: locker.get_is_assigned is False, self.get_locker_list)
        )

        if not empty_lockers:
            print("No empty lockers available")
        
        if to_print:
            for locker in empty_lockers:
                print(
                    f"Locker: #{locker.get_locker_id},\n"
                    f"Assigned to: {locker.get_client_id},\n"
                    f"Locker price: {format_in_currency(locker.get_locker_price)}\n"
                )
                separator_string()
        else:
            return empty_lockers

    def assign_lockers(self, client_id, name):
        """To assign locker"""

        self.get_empty_lockers()[0].set_client_id = client_id
        separator_string()
        print()
        print(f"Locker #{self.get_empty_lockers()[0].get_locker_id}" f" assigned to: {name}")
        print()
        return self.get_empty_lockers()[0]

    def get_client(self, client_id=None):
        if client_id:
            for client in self.__clients_list:
                if client.get_client_id == client_id:
                    return client
                else:
                    return print("Client not found, please check the ID and try again.")
        else:
            for index, client in enumerate(self.__clients_list):
                separator_string(index)
                # Create a better structure for this print
                print(
                    f"ID: {client.get_client_id},\n"
                    f"Name: {client.get_name} {client.get_last_name},\n"
                    f"Age: {client.get_age},\nPhone number: +(57) {client.get_phone_number},\n"
                    f"Membership active: {"Active" if client.get_membership_active else "Inactive"},\n"
                    f"Membership data: {client.get_date_last_payment},\n"
                    f"Is active: {client.get_is_active}, Created at: {client.get_created_at},\n"
                    f"Membership data: {client.get_membership_data.get_membership_type},\n"
                    f"Assigned locker: {client.get_assigned_locker},\n"
                    f"Locker price: {format_in_currency(client.get_locker_data.get_locker_price) if client.get_locker_data is not None else format_in_currency(0)}"
                )

    def add_client(
        self,
        client_id,
        name,
        last_name,
        age,
        phone_number,
        membership_active,
        membership_type,
        is_active,
        created_at=None,
        is_training=None,
    ):
        membership_data = []
        locker_info = None
        date_last_payment = None
        for membership in self.__membership_list:
            if membership.get_membership_type.lower() == membership_type:
                membership_data.append(membership)

        if is_training:
            locker_info = self.assign_lockers(client_id, f"{name + " " + last_name}")

        if created_at == get_current_date():
            date_last_payment = created_at

        user_data = Client(
            client_id,
            name,
            last_name,
            age,
            phone_number,
            membership_active,
            membership_data[0],
            is_active,
            created_at,
            date_last_payment,
            is_training,
            locker_info,
        )

        self.__clients_list.append(user_data)
        separator_string()
        print()
        print(f"Client {name} added successfully...")
        print()
        separator_string()

    """ def update_membership_date(self, client_id, membership_data, new_membership_date):
        print(client_id, membership_data.get_date_last_payment, new_membership_date)
        for client in self.clients_list:
            if client.get_id == client_id:
                membership_data.set_date_last_payment = new_membership_date
                print(client.get_name, membership_data.get_date_last_payment)
                return print(
                    f"Membership updated successfully for client: {client.get_name},"
                    f" with ID: {client.get_id}"
                ) """
