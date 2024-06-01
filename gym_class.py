from user_class_gym import Client
from commons import (
    get_current_date,
    format_in_currency,
    separator_string,
    search_client,
    convert_value,
    get_params_peer_class,
)
from membership_class import Membership
import inspect
from datetime import date, timedelta


class Gym:
    def __init__(self, nit: int, name: str, adress: str):
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
        return self.__locker_list

    @get_locker_list.setter
    def set_locker_list(self, locker_list):
        self.__locker_list = locker_list

    @property
    def get_membership_list(self):
        return self.__membership_list

    @get_membership_list.setter
    def set_membership_list(self, membership_list):
        self.__membership_list = membership_list

    def print_all_lockers(self, to_print=False):
        if to_print:
            for locker in self.__locker_list:
                print(
                    f"Locker: #{locker.get_locker_id},\n"
                    f"Assigned to: {locker.get_client_id},\n"
                    f"Locker price: {format_in_currency(locker.get_locker_price)}\n"
                )
                separator_string()
        else:
            return self.__locker_list

    def get_empty_lockers(self, to_print=False):
        empty_lockers = []

        if self.get_locker_list:
            empty_lockers = list(
                filter(
                    lambda locker: locker.get_is_assigned is False, self.get_locker_list
                )
            )
        else:
            empty_lockers = []

        if not empty_lockers:
            print("No empty lockers available")
            separator_string()

        if to_print and empty_lockers:
            for locker in empty_lockers:
                print(
                    f"Locker: #{locker.get_locker_id},\n"
                    f"Assigned to: {locker.get_client_id},\n"
                    f"Locker price: {format_in_currency(locker.get_locker_price)}\n"
                )
                separator_string()
        elif not empty_lockers:
            return []
        else:
            return empty_lockers

    def assign_lockers(self, client_id, name):
        """To assign locker"""

        self.get_empty_lockers()[0].set_client_id = client_id
        print(
            f"Locker #{self.get_empty_lockers()[0].get_locker_id}"
            f" assigned to: {name}"
        )
        separator_string()
        print()
        value = input("Do you want to print all lockers? (y/n): ")
        if value.lower() == "y":
            self.print_all_lockers(True)
        elif value.lower() == "n":
            pass
        print()
        return self.get_empty_lockers()[0]

    def get_client(self, client_id=None):
        client_found = False

        if client_id:
            for client in self.__clients_list:
                if client.get_client_id == client_id:
                    client_found = True
                    return client
            if not client_found:
                print(f"Client {client_id} not found.")
        else:
            for index, client in enumerate(self.__clients_list):
                separator_string(index)
                print(
                    f"ID: {client.get_client_id},\n"
                    f"Name: {client.get_name} {client.get_last_name},\n"
                    f"Age: {client.get_age},\n"
                    f"Phone number: +(57) {client.get_phone_number},\n"
                    f"Membership active: {'Active' if client.get_membership_active else 'Inactive'},\n"
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
        print(
            f"Client {name} has been added to the gym {self.get_name.capitalize()} successfully..."
        )
        separator_string()

    def update_client(self, object_class):
        options = {}
        selected_key = None
        expected_type = {}
        separator_string()
        client_id = input("Write the client ID: ")
        client_id_converted = convert_value(client_id, "int")
        separator_string()
        client_found = self.get_client(client_id_converted)
        if client_id and client_found:
            params = inspect.signature(object_class.__init__).parameters
            for index, (param_name, param) in enumerate(params.items(), start=0):
                expected_type = (
                    param.annotation if param.annotation != inspect._empty else str
                )
                if param_name == "self":
                    continue
                options[index] = param_name
            print(
                "What field do you want to change? Write the number you  want to change: "
            )
            print()
            for key, option in options.items():
                print(f"Write '{key}' for '{option}'.")
            print()
            value_selected = input("Write the number of your choice: ")
            if int(value_selected) in options:
                selected_key = options[int(value_selected)]

            new_value = input(f"Write the new value for {selected_key}: ")

            if client_found:
                client_instance = client_found

                separator_string("Before update:")
                print(self.get_client(client_id_converted))

                setter_name = f"set_{selected_key}"
                if hasattr(client_instance, setter_name):
                    setattr(
                        client_instance,
                        setter_name,
                        convert_value(new_value, expected_type.__name__),
                    )
                    separator_string("After update:")
                    print(self.get_client(client_id_converted))
                else:
                    print(f"No setter found for {selected_key}")
            else:
                separator_string()
                print(f"Client {client_id} not found...")

    def delete_client(self, client_id):
        client_found = search_client(client_id, self.__clients_list)
        if client_found:
            self.__clients_list.remove(client_found[0])
            separator_string()
            print(f"Client {client_id} has been deleted successfully...")
            to_print = input("Do you want to print the clients list? (y/n): ")
            if to_print.lower() == "y":
                self.get_client()
            separator_string()
        else:
            separator_string()
            print(f"Client {client_id} not found...")
            separator_string()

    def create_membership(self):
        try:
            membership = get_params_peer_class(Membership)

            # Validate that the membership has been created correctly
            if not membership:
                print("Error: Unable to obtain the parameters for the membership.")
                return

            # Check essential properties of the membership
            required_properties = [
                "get_membership_type",
                "get_membership_active",
                "get_membership_cost",
            ]
            for prop in required_properties:
                if not hasattr(membership, prop):
                    print(f"Error: The property {prop} is missing in the membership.")
                    return

            self.__membership_list.append(membership)

            print(
                f"Membership successfully created with type: {membership.get_membership_type}."
            )  # Assuming 'membership' has a 'get_membership_type' property
        except AttributeError as ae:
            print(f"Attribute error: {str(ae)}")

    def assign_client_membership(self, client_id: int, membership: Membership):
        client = self.get_client(client_id)
        client.set_membership_data(self, membership)

    def handle_change_client_training(self, client_id):
        client_found = self.get_client(client_id)
        if client_found:
            if client_found.get_is_training:
                client_found.set_is_training = False
            else:
                client_found.set_is_training = True
            separator_string()
            print(
                f"Training status for client: {client_found.get_name} has been updated...\n"
            )
            print(
                f"New status: {'Training' if client_found.get_is_training else 'Not training'}"
            )
            separator_string()
        else:
            separator_string()
            print(f"Client {client_id} not found...")
            separator_string()

    def handle_client_status(self, client_id):
        client_found = self.get_client(client_id)
        if client_found:
            if client_found.get_is_active:
                client_found.set_is_active = False
            else:
                client_found.set_is_active = True
            separator_string()
            print(f"Status for client: {client_found.get_name} has been updated...\n")
            print(
                f"New status: {'Active' if client_found.get_is_active else 'Inactive'}"
            )
            separator_string()
        else:
            separator_string()
            print(f"Client {client_id} not found...")
            separator_string()

    def update_client_membership(self, client_id, membership_type):
        client_found = self.get_client(client_id)
        if client_found:
            for membership in self.__membership_list:
                if membership.get_membership_type == membership_type:
                    client_found.set_membership_data = membership
                    separator_string()
                    print(
                        f"Membership for client: {client_found.get_name} has been updated...\n"
                    )
                    print(
                        f"New membership: {client_found.get_membership_data.get_membership_type}"
                    )
                    separator_string()
        else:
            separator_string()
            print(f"Client {client_id} not found...")
            separator_string()

    def remaining_days_for_membership(self, client_id):
        client_found = self.get_client(client_id)
        if client_found:
            print(client_found.get_date_last_payment)
            print(date.fromisoformat(client_found.get_date_last_payment))
            rest_days = timedelta(
                days=client_found.get_membership_data.get_membership_duration
            )
            print(date.fromisoformat(client_found.get_date_last_payment) - rest_days)
            print(client_found.get_membership_data.get_membership_duration)

        else:
            separator_string()
            print(f"Client {client_id} not found...")
            separator_string()

    def print_membership_list(self):
        for i, membership in enumerate(self.__membership_list):
            separator_string(i)
            print(
                f"Membership {i+1}: Type: {membership.get_membership_type()}, Active: {membership.get_membership_active()}"
            )
            print(f"Cost: {membership.get_membership_cost()}")

    def __str__(self):
        return (
            f"Gym(nit={self.nit}, name={self.name}, address={self.get_adress}, "
            f"clients={self.__clients_list}, lockers={self.__locker_list}, memberships={self.__membership_list})"
        )

    def __repr__(self):
        return self.__str__()

    #         """ client_instance = client_finded[0]

    #             separator_string("Before the update:")
    #             self.get_client_info(client_id) """

    #             """ setter_name = f"set_{selected_key}"
    #             if hasattr(client_instance, setter_name):
    #                 setattr(client_instance, setter_name, convert_value(new_value, expected_type.__name__))
    #             else:
    #                 print(f"No setter found for {selected_key}")

    #             separator_string("After the update:")
    #             self.get_client_info(client_id) """

    # """ def update_membership_date(self, client_id, membership_data, new_membership_date):
    #     print(client_id, membership_data.get_date_last_payment, new_membership_date)
    #     for client in self.clients_list:
    #         if client.get_id == client_id:
    #             membership_data.set_date_last_payment = new_membership_date
    #             print(client.get_name, membership_data.get_date_last_payment)
    #             return print(
    #                 f"Membership updated successfully for client: {client.get_name},"
    #                 f" with ID: {client.get_id}"
    #             ) """
