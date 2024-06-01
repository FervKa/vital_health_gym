class Membership:
    def __init__(self, membership_type="daily", membership_active=False, cost = int):
        self.__membership_type = membership_type
        

        """ self.__date_last_payment = "2024-05-25" """
        """ if date_last_payment:
            self.__date_last_payment = date_last_payment
        else:
            self.__date_last_payment = "2024-05-25" """
        self.__membership_active = membership_active or False
        self.__cost = cost
        """ if membership_active:
            self.__membership_active = True
        else:
            self.__membership_active = False """

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
    def get_cost(self):
        return self.__cost
    
    @get_cost.setter
    def set_cost(self, cost):
        self.__cost = cost

""" 

membership1 = Membership(3291121, "Month", 10000, "2024-05-25", True)


print(
    f"The client ID is: {membership1.get_client_id},\n"
    f"the membership type is: {membership1.get_membership_type.lower()},\n"
    f"the cost is: {membership1.get_cost},\n"
    f"the date of the last payment is: {membership1.get_date_last_payment},\n"
    f"and the membership is active: {membership1.get_membership_active}"
)
 """
