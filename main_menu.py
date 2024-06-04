from gym_class import Gym
from commons import (
    options_input,
    get_current_date,
    convert_value,
    separator_string,
    get_params_peer_class,
)
from initial_data import dummy_users, dummy_lockers, dummy_memberships, michael_gym
from membership_class import Membership
import inspect
from lockers_class import Locker
from user_class_gym import Client

michael_gym.delete_client_membership(3332213)
client = michael_gym.get_client(3332213)
print(client.get_membership_data)

""" for membership in self.membership_list:
            print("#------------Membership data-----------#")
            print(
                f"Membership type: {membership.get_membership_type},\n"
                f"Membership cost:  {"${:,.0f}".format(membership.get_membership_cost)}"
            ) 
"""
""" test_gym = get_params_peer_class(Gym) """

""" ENTER_DATA_INPUT = 1
list_lockers_by_input = [] """

""" for data in range(ENTER_DATA_INPUT):
    locker = get_params_peer_class(Locker)
    list_lockers_by_input.append(locker) """

""" test_gym.set_locker_list = dummy_lockers
test_gym.set_membership_list = dummy_memberships """
""" test_gym.add_client(
    999999,
    "Julian",
    "Caribe",
    19,
    "1212121212",
    True,
    "daily",
    True,
    get_current_date(),
    True,
) """


""" for param in get_params_peer_class(Gym):
    print(f"Write the value for: {param.name}")
    setattr(test_gym, param.name, input())
    print(param.name)
    print(test_gym.get_adress)   """

# ---------- Manejo de excepciones en el input ----------#
while True:
    print("----------- Welcome -----------")
    print("select an option by entering the index number")
    print("1. Customer Management")
    print("2. Membership Management")
    print("3. Reports")
    print("4. Gym Access")
    print("5. exit")
    print("-----------------------------------------")

    ERROR_MESSAGE = "Error: You must enter a valid integer number. Please try again."
    op = options_input(ERROR_MESSAGE)

    if op == 1:
        while True:
            print("----------- Customer management -----------")
            print("select an option by entering the index number")
            print("1. Add customer")
            print("2. Verify customer")
            print("3. Disable customer")
            print("4. Update customer data.")
            print("5. Back to previous menu")
            print("-----------------------------------------")
            op1 = options_input(ERROR_MESSAGE)
            if op1 == 1:
                separator_string("Enter the following data")
                id_client = str(input("Client id"))
                michael_gym.add_client()
            if op1 == 5:
                break

    if op == 2:
        while True:
            print("----------- Membership Management -----------")
            print("select an option by entering the index number")
            print("1. Update membership")
            print("2. Add new membership")
            print("3. Disable membership")
            print("4. Back to previous menu")
            print("-----------------------------------------")
            op2 = options_input(ERROR_MESSAGE)
            if op2 == 4:
                break
    if op == 3:
        while True:
            print("----------- Reports -----------")
            print("select an option by entering the index number")
            print("1. Daily profit report")
            print("2. Current customers report")
            print("3. Active/inactive customers report")
            print("4. New customers report (joined less than a month ago)")
            print("5. Users who entered the gym on the day report")
            print("6. Daily general report")
            print("7. Back to previous menu")
            print("-----------------------------------------")
            ERROR_MESSAGE = (
                "Error: You must enter a valid integer number. Please try again."
            )
            op3 = options_input(ERROR_MESSAGE)
            if op3 == 3:
                while True:
                    print(
                        "----------- Active/Inactive customers report -----------"
                    )
                    print("select an option by entering the index number")
                    print("1. Active")
                    print("2. Inactive")
                    print("3. Back to previous menu")
                    print("-----------------------------------------")
                    op3_1 = options_input(ERROR_MESSAGE)
                    if op3_1 == 3:
                        break
            if op3 == 7:
                break
    if op == 4:
        while True:
            print("----------- Gym Access -----------")
            print("enter the user's document you want to verify")
            print("-----------------------------------------")
            ERROR_MESSAGE = "Error: You must enter a valid identification document, do not use periods or spaces."
            op_id = options_input(ERROR_MESSAGE)
            break
    if op == 5:
        break
