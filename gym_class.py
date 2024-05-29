from user_class_gym import Client
import locale

locale.setlocale(locale.LC_ALL, "es_CO.UTF-8")


class Gym:
    def __init__(self, nit, name, adress, clients_list, locker_list, membership_list):
        self.nit = nit
        self.name = name
        self.adress = adress
        self.__clients_list = clients_list
        self.locker_list = locker_list
        self.membership_list = membership_list

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
        for membership in self.membership_list:
            print("#------------Membership data-----------#")
            print(
                f"Membership type: {membership.get_membership_type},\n"
                f"Membership cost:  {locale.currency(membership.get_membership_cost, grouping=True)},\n"
            )

    @get_membership_list.setter
    def set_membership_list(self, membership_list):
        self.membership_list = membership_list

    """ id: int,
        name: str,
        last_name: str,
        age: int,
        phone_number=int,
        membership_active=False,
        __membership_data=object,
        is_active=False, """

    def get_client(self, client_id=None):
        if client_id:
            for client in self.__clients_list:
                if client.get_id == client_id:
                    return client
                else:
                    return print("Client not found, please check the ID and try again.")
        else:
            for index, client in enumerate(self.__clients_list):
                print(
                    f"#--------------------------------{index}------------------------------#"
                )
                # Create a bether structure for this print
                print(
                    f"ID: {client.get_id},\nName: {client.get_name} {client.get_last_name},\n"
                    f"Age: {client.get_age},\n Phone number: {client.get_phone_number},"
                    f"Membership active: {client.get_membership_active},"
                    f"Membership data: {client.get_membership_data.get_date_last_payment},"
                    f"Is active: {client.get_is_active}, Created at: {client.get_created_at},"
                    f"Membership data: {client.get_membership_data.get_membership_type}"
                )

    def add_client(
        self,
        client_id,
        name,
        last_name,
        age,
        phone_number,
        membership_active,
        membership_data,
        is_active,
        created_at=None,
    ):
        self.__clients_list.append(
            Client(
                client_id,
                name,
                last_name,
                age,
                phone_number,
                membership_active,
                membership_data,
                is_active,
                created_at,
            )
        )
        return print(f"Client {name} added successfully")

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
