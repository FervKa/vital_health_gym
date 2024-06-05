from user_class_gym import Client
from commons import (
    get_current_date,
    format_in_currency,
    separator_string,
    search_client,
    convert_value,
    get_params_peer_class,
    validate_id,
    create_a_file,
    validate_object_class,
    get_headers,
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
        self.__earnings = []

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

    @property
    def get_earnings(self):
        return self.__earnings

    @get_earnings.setter
    def set_earnings(self, earnings):
        self.__earnings = earnings

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
                    print()
                    return client
            if not client_found:
                print(f"Client {client_id} not found.")
        else:
            for index, client in enumerate(self.__clients_list):
                separator_string(f"{index} ")
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
        if client_id:
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
        else:
            print("Client id not provided...")

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

    def assign_client_membership(self, client_id, membership):
        validate_id(client_id)
        client = self.get_client(client_id)
        validate_object_class(membership, Membership)
        client.set_membership_data = membership
        print(f"Membership assigned to client {client_id} successfully.")

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

    def update_client_membership(self, client_id):
        for i, memb in enumerate(self.__membership_list, start=1):
            name = memb.get_membership_type
            print(f"{i}. {name}")
        print("Choose a option to update")
        option = int(input("Please enter an number of option: "))
        for i, memb in enumerate(self.__membership_list, start=1):
            if option == i:
                membership_type = memb.get_membership_type
                print(f"The membership type is: {membership_type}")
                break
            else:
                print("Invalid option.")
        # update membership with membership_type choosed
        client_found = self.get_client(client_id)
        if client_found:
            membership_found = False
            for membership in self.__membership_list:
                print(f"Checking membership type: {membership.get_membership_type}")
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
                    membership_found = True
                    break

            if not membership_found:
                print("Membership type not found in the list.")
        else:
            separator_string()
            print(f"Client {client_id} not found...")
            separator_string()

    def remaining_days_for_membership(self, client_id):
        client_found = self.get_client(client_id)
        if client_found:
            formated_last_payment = date.fromisoformat(
                client_found.get_date_last_payment
            )
            duration_membership = (
                client_found.get_membership_data.get_membership_duration
            )
            duration_membership_days = timedelta(days=duration_membership)
            if formated_last_payment >= date.today():
                separator_string()
                print(f"The user has paid the membership, but, is not active...")
                separator_string()
            elif (
                formated_last_payment
                + duration_membership_days
                - date.fromisoformat(get_current_date())
            ).days <= 0:
                separator_string()
                print(f"Membership for client {client_id} has expired...")
                separator_string()
            else:
                separator_string("Remaining days for the membership")
                print(
                    f"Client {client_found.get_name} has {(formated_last_payment
                + duration_membership_days
                - date.fromisoformat(get_current_date())).days} days left until the membership ends..."
                )
                separator_string()
        else:
            separator_string()
            print(f"Client {client_id} not found...")
            separator_string()

    def print_membership_list(self):
        for i, membership in enumerate(self.__membership_list):
            separator_string(i)
            print(f"Membership {i+1}: Type: {membership.get_membership_type}")
            print(f"Active: {membership.get_membership_active}")
            print(f"Cost: {membership.get_membership_cost}")

    def generate_report_current_clients(self):
        data_to_save = []
        headers = get_headers(Client)
        for user in self.__clients_list:
            aux = []
            for header in headers:
                aux.append(getattr(user, f"get_{header.lower()}"))

            data_to_save.append(aux)
        create_a_file("current_clients.xlsx", headers, data_to_save)

        return (
            f"Gym(nit={self.nit}, name={self.name}, address={self.get_adress}, "
            f"clients={self.__clients_list}, lockers={self.__locker_list}, memberships={self.__membership_list})"
        )

    """ def __repr__(self):
        return self.__str__() """

    def update_assigned_client_locker(self, client_id, locker_id=None):
        """Assign a locker to a client. If locker_id is provided, it will assign that locker if available. Otherwise, it assigns the first available locker."""

        empty_lockers = self.get_empty_lockers()

        if locker_id is not None:
            # Buscar el locker por ID
            locker_to_assign = next(
                (
                    locker
                    for locker in empty_lockers
                    if locker.get_locker_id == locker_id
                ),
                None,
            )
            if locker_to_assign is not None:
                locker_to_assign.set_client_id = client_id
                print(
                    f"Locker #{locker_to_assign.get_locker_id} assigned to client ID: {client_id}"
                )
            else:
                print(
                    f"Locker #{locker_id} is not available. Assigning the first available locker."
                )
                # Asignar el primer locker disponible
                if empty_lockers:
                    empty_lockers[0].set_client_id = client_id
                    print(
                        f"Locker #{empty_lockers[0].get_locker_id} assigned to client ID: {client_id}"
                    )
                else:
                    print("No empty lockers available.")
        else:  # Asignar el primer locker disponible cuando no le paso ningun locker_id
            if empty_lockers:
                empty_lockers[0].set_client_id = client_id
                print(
                    f"Locker #{empty_lockers[0].get_locker_id} assigned to client ID: {client_id}"
                )
            else:
                print("No empty lockers available.")

        separator_string()
        value = input("Do you want to print all lockers? (y/n): ")
        if value.lower() == "y":
            self.print_all_lockers(True)
        elif value.lower() == "n":
            pass
        print()

    def delete_client_assigned_locker(self, client_id):
        """Delete the assigned locker for a client."""
        client = self.get_client(client_id)
        if client:
            if client.get_assigned_locker:
                old_locker = client.get_assigned_locker
                client.set_assigned_locker = None
                print(
                    f"Assigned locker {old_locker} for client {client_id} has been deleted."
                )
            else:
                print(f"No assigned locker found for client {client_id}.")
        else:
            print(f"Client {client_id} not found.")

    def delete_client_membership(self, client_id):
        """Delete a client membership."""
        client = self.get_client(client_id)
        dummy_membership = Membership(
            membership_type="None",
            membership_active=False,
            membership_cost=0,
            membership_duration=30,
        )
        client.set_membership_data = dummy_membership
        client.set_membership_active = False
        print("Membership data deleted. New None membership assigned.")

    def generate_report_day(self, date_to_search):
        attended_clients_today = []
        headers = get_headers(Client)
        for user in self.__clients_list:
            if user.get_created_at == date_to_search:
                aux = []
                for header in headers:
                    aux.append(getattr(user, f"get_{header.lower()}"))
                attended_clients_today.append(aux)
        create_a_file("attended_clients_today.xlsx", headers, attended_clients_today)

    def calculate_earning_peer_day(self, date_to_search):
        regards = 0
        users_list = []
        headers = []
        params = inspect.signature(Client.__init__).parameters
        for param_name, param in params.items():
            if param_name == "self" or param_name == "locker_data" or param_name == "membership_data":
                continue

            headers.append(param_name.upper())
        headers.append("MEMBERSHIP_COST")

        for user in self.__clients_list:
            if user.get_created_at == date_to_search:
                user_aux = []
                for index, header in enumerate(headers):
                    if header.lower() != "membership_cost" and header.lower() != "membership_data":
                        user_aux.append(getattr(user, f"get_{header.lower()}"))
                    else:
                        regards += user.get_membership_data.get_membership_cost
                user_aux.append(format_in_currency(user.get_membership_data.get_membership_cost))
                users_list.append(user_aux)
        users_list.append(["TOTAL_EARNED:", format_in_currency(regards)])
        create_a_file("earning_peer_day.xlsx", headers, users_list)

    def get_client_info(self, client_id):
        if client_id:
            client_selected = self.get_client(client_id)
            separator_string(f"Cliend found: {client_selected.get_name} ")
            print(
                    f"ID: {client_selected.get_client_id},\n"
                    f"Name: {client_selected.get_name} {client_selected.get_last_name},\n"
                    f"Age: {client_selected.get_age},\n"
                    f"Phone number: +(57) {client_selected.get_phone_number},\n"
                    f"Membership active: {'Active' if client_selected.get_membership_active else 'Inactive'},\n"
                    f"Membership data: {client_selected.get_date_last_payment},\n"
                    f"Is active: {client_selected.get_is_active}, Created at: {client_selected.get_created_at},\n"
                    f"Membership data: {client_selected.get_membership_data.get_membership_type},\n"
                    f"Assigned locker: {client_selected.get_assigned_locker},\n"
                    f"Locker price: {format_in_currency(client_selected.get_locker_data.get_locker_price) if client_selected.get_locker_data is not None else format_in_currency(0)}"
                )
        else:
            print("No client id selected")
    