class Gym:
    def __init__(self, nit, name, adress, clients_list, locker_list):
        self.nit = nit
        self.name = name
        self.adress = adress
        self.clients_list = clients_list
        self.locker_list = locker_list

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
        return self.clients_list

    @get_clients_list.setter
    def set_clients_list(self, clients_list):
        self.clients_list = clients_list

    @property
    def get_locker_list(self):
        return self.locker_list

    @get_locker_list.setter
    def set_locker_list(self, locker_list):
        self.locker_list = locker_list
