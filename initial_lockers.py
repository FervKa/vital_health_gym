class Locker:
    def __init__(
        self, locker_id, state, color, locker_type, price, is_assigned, client_id
    ):
        self.locker_id = locker_id
        self.state = state
        self.color = color
        self.locker_type = locker_type
        self.price = price
        self.is_assigned = is_assigned
        if is_assigned:
            self.client_id = client_id
        else:
            self.client_id = None

    @property
    def get_locker_id(self):
        return self.locker_id

    @get_locker_id.setter
    def set_locker_id(self, locker_id):
        self.locker_id = locker_id

    @property
    def get_state(self):
        return self.state

    @get_state.setter
    def set_state(self, state):
        self.state = state

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
    def get_price(self):
        return self.price

    @get_price.setter
    def set_price(self, price):
        self.price = price

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
        self.client_id = client_id
