from user_class_gym import Client
from commons import get_current_date,format_in_currency, separator_string, search_client, convert_value, get_params_peer_class, validate_id, validate_atributes_class, validate_object_class
from membership_class import Membership
import inspect

class Gym:
    def __init__(self, nit:int, name:str, adress:str):
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

    def print_all_lockers(self, to_print = False):
        if to_print :
            for locker in self.__locker_list:
                print(
                    f"Locker: #{locker.get_locker_id},\n"
                    f"Assigned to: {locker.get_client_id},\n"
                    f"Locker price: {format_in_currency(locker.get_locker_price)}\n"
                )
                separator_string()
        else:
            return self.__locker_list

    def get_empty_lockers(self, to_print = False):
        empty_lockers = []
        
        if self.get_locker_list:
            empty_lockers = list(
                filter(lambda locker: locker.get_is_assigned is False, self.get_locker_list)
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
        print(f"Locker #{self.get_empty_lockers()[0].get_locker_id}" f" assigned to: {name}")
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
        if client_id: 
            for client in self.__clients_list:
                if client.get_client_id == client_id:
                    return client
            print("Client not found, please check the ID and try again.")
            return None
        else:
            for index, client in enumerate(self.__clients_list):
                separator_string(index)
                # Create a better structure for this print
                print(
                    f"ID: {client.get_client_id},\n"
                    f"Name: {client.get_name} {client.get_last_name},\n"
                    f"Age: {client.get_age},\nPhone number: +(57) {client.get_phone_number},\n"
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
        print(f"Client {name} has been added to the gym {self.get_name.capitalize()} successfully...")
        separator_string()

    def get_client_info(self, client_id):
        if client_id:
            client_found = search_client(client_id, self.__clients_list)
            if client_found:
                client_info = {}
                client_class_methods = inspect.getmembers(Client)
                getters = [(name, member) for name, member in client_class_methods if name.startswith("get_")]
                for getter_name, _ in getters:
                    if getter_name.startswith("get_"):
                        attr_name = getter_name[4:]  # Remove "get_" prefix to get attribute name
                        attr_value = getattr(client_found[0], getter_name)  # Llamar al getter del cliente
                        client_info[attr_name] = attr_value

                print(f"Client info: {client_info}")
    def update_client(self, object_class):
        options = {}
        selected_key = None
        expected_type = {}
        expected_type_selected = None
        separator_string()
        """ client_id = input("Write the client ID: ") """
        client_id = 12312321
        separator_string()
        if client_id:
            client_finded = search_client(client_id, self.__clients_list)
            params = inspect.signature(object_class.__init__).parameters
            for index, (param_name, param) in enumerate(params.items(), start=0):
                expected_type = param.annotation if param.annotation != inspect._empty else str
                if param_name == "self":
                    continue
                options[index] = param_name
            for key, option in options.items():
                print(f"Write '{key}' for '{option}'.")
            
            """ for param_name in expected_type:
                print(f"Param: {param_name}") """
            print()
            value_selected = input("Write the number of your choice: ")
            if int(value_selected) in options:
                selected_key = options[int(value_selected)]


            new_value = input(f"Write the new value for {selected_key}: ")
            print()
            print("What field do you want to change? Write the number you  want to change: ")

            #if client_finded:


    def create_membership(self):
        try:
            membership = get_params_peer_class(Membership)

            # Validate that the membership has been created correctly
            if not membership:
                print("Error: Unable to obtain the parameters for the membership.")
                return
            
            # Check essential properties of the membership
            required_properties = ['get_membership_type', 'get_membership_active', 'get_membership_cost']
            validate_atributes_class(membership, required_properties)   
            self.__membership_list.append(membership)    
            
            print(f"Membership successfully created with type: {membership.get_membership_type}.")  # Assuming 'membership' has a 'get_membership_type' property
        except AttributeError as ae:
            print(f"Attribute error: {str(ae)}")

    def assign_client_membership(self, client_id:int, membership: Membership):
        validate_id(client_id)
        client =  self.get_client(client_id)
        validate_object_class(membership, Membership)
        client.set_membership_data = membership
        #se necesita actualizar el tiempo de mebresia en esta funcion
        print(f"Membership assigned to client {client_id} successfully.")

    def print_membership_list(self):
        for i, membership in enumerate(self.__membership_list):
            separator_string(i)
            print(f"Membership {i+1}: Type: {membership.get_membership_type}, Active: {membership.get_membership_active}")
            print(f"Cost: {membership.get_membership_cost}")

    def update_client_membership(self, client_id, new_membership_data):
        validate_id(client_id)
        client =  self.get_client(client_id)
        validate_object_class(new_membership_data, Membership)
        client.set_membership_data = new_membership_data
        print(f"Membership assigned to client {client_id} successfully.")
        #Se necestia actualizar el tiemp ode membresia en esta funcion
    
    # def delete_client_membership(self, client_id):
    #     validate_id(client_id)
    #     client =  self.get_client(client_id)
    #     del client.set_membership_data = None
        
    #     print(f"Membership data for client {client_id} has been deleted.")
    def delete_client_membership(self, client_id):
        client = self.get_client(client_id)
        if client is not None:
            client.delete_membership_data()
            print(f"Membership data for client {client_id} has been deleted.")

         






    # def __str__(self):
    #     return (f"Gym(nit={self.nit}, name={self.name}, address={self.get_adress}, "
    #             f"clients={self.__clients_list}, lockers={self.__locker_list}, memberships={self.__membership_list})")
    
    # def __repr__(self):
    #     return self.__str__()
      
    
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

michael_gym = Gym(3221231, "Michael Gym", "Calle 123")