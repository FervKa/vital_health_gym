class Membership:
    def __init__(
        self,
        membership_type: str,
        membership_active: bool,
        membership_cost: int,
        membership_duration: int,
    ):
        self.__membership_type = membership_type
        self.__membership_active = membership_active or False
        self.__membership_cost = membership_cost
        self.__membership_duration = membership_duration

    @property
    def get_membership_type(self):
        return self.__membership_type

    @get_membership_type.setter
    def set_membership_type(self, membership_type):
        self.__membership_type = membership_type

    @property
    def get_membership_active(self):
        return self.__membership_active

    @get_membership_active.setter
    def set_membership_active(self, membership_active):
        self.__membership_active = membership_active

    @property
    def get_membership_cost(self):
        return self.__membership_cost

    @get_membership_cost.setter
    def set_membership_cost(self, membership_cost):
        self.__membership_cost = membership_cost

    @property
    def get_membership_duration(self):
        return self.__membership_duration

    @get_membership_duration.setter
    def set_membership_duration(self, membership_duration):
        self.__membership_duration = membership_duration
