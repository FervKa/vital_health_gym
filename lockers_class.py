class Locker:
    def __init__(self, locker_id:int, locker_state:bool, color:str, locker_type:str, client_id:int):
        self.locker_id = locker_id
        self.locker_state = locker_state
        self.color = color
        self.locker_type = locker_type
        if client_id is not None:
            self.client_id = client_id
            self.is_assigned = True
        else:
            self.client_id = None
            self.is_assigned = False
        if locker_type.lower() == "simple":
            self.locker_price = 5000
        elif locker_type.lower() == "double":
            self.locker_price = 10000
        else:
            self.locker_price = 2000

    @property
    def get_locker_id(self):
        return self.locker_id

    @get_locker_id.setter
    def set_locker_id(self, locker_id):
        self.locker_id = locker_id

    @property
    def get_locker_state(self):
        return self.locker_state

    @get_locker_state.setter
    def set_locker_state(self, new_locker_state):
        self.locker_state = new_locker_state

    @property
    def get_color(self):
        return self.color

    @get_color.setter
    def set_color(self, color):
        self.color = color

    @property
    def get_locker_type(self):
        return self.locker_type

    @get_locker_type.setter
    def set_locker_type(self, locker_type):
        self.locker_type = locker_type

    @property
    def get_locker_price(self):
        return self.locker_price

    @get_locker_price.setter
    def set_locker_price(self, price):
        self.locker_price = price

    @property
    def get_is_assigned(self):
        return self.is_assigned

    @get_is_assigned.setter
    def set_is_assigned(self, is_assigned):
        self.is_assigned = is_assigned

    @property
    def get_client_id(self):
        return self.client_id

    @get_client_id.setter
    def set_client_id(self, client_id):
        if client_id is not None:
            self.is_assigned = True
            self.client_id = client_id
