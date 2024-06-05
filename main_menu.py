from gym_class import Gym
from commons import (
    options_input,
    get_current_date,
    convert_value,
    separator_string,
    get_params_peer_class,
)
from initial_data import (
    dummy_users,
    dummy_lockers,
    dummy_memberships,
    michael_gym,
    dummy_gyms,
)
from membership_class import Membership
import inspect
from lockers_class import Locker
from user_class_gym import Client
from datetime import datetime

""" client = get_params_peer_class(Client)

gym_selected = michael_gym

print(client.get_name) """

""" for membership in self.membership_list:
            print("#------------Membership data-----------#")
            print(
                f"Membership type: {membership.get_membership_type},\n"
                f"Membership cost:  {"${:,.0f}".format(membership.get_membership_cost)}"
            ) 
"""

gym_selected = None

while True:
    separator_string("Gym administration ")
    print("Select your option: ")
    print()
    print("1. Select a gym.")
    print("2. Create a gym.")
    print("3. Exit.")
    print()

    ERROR_MESSAGE = "Error: You must enter a valid integer number. Please try again."
    gym_option = options_input(ERROR_MESSAGE)

    if gym_option == 1:
        for index, gym in enumerate(dummy_gyms):
            separator_string(f"{index + 1} ")
            print(
                f"NIT: {gym.get_nit},\n"
                f"Name: {gym.get_name},\n"
                f"Address: {gym.get_adress},\n"
            )
        separator_string()
        print("Select your gym: ")
        print()
        gym_op_selected = options_input(ERROR_MESSAGE)
        gym_selected = dummy_gyms[gym_op_selected -1]
        
        while True:
            separator_string(f"Welcome to {gym_selected.get_name} ")
            print("Select an option by entering the index number: ")
            print()
            print("1. User Management.")
            print("2. Membership Management.")
            print("3. Reports.")
            print("4. Gym Access.")
            print("5. Exit.")
            separator_string()

            op = options_input(ERROR_MESSAGE)

            if op == 1:
                while True:
                    separator_string("user management ")
                    print("Select an option by entering the index number: ")
                    print()
                    print("1. Add user.")
                    print("2. Verify user.")
                    print("3. Delete user.")
                    print("4. Update user data.")
                    print("5. Show all users.")
                    print("6. Back to previous menu.")
                    separator_string()
                    op1 = options_input(ERROR_MESSAGE)
                    if op1 == 1:
                        new_client = get_params_peer_class(Client, gym_selected.get_membership_list)
                        print(f"Client '{new_client.get_name}' was created successfully...'")
                    if op1 == 2:
                        separator_string("Verify user")
                        client_id = int(input("Enter the user's identity document: "))
                        client = gym_selected.get_client_info(client_id)
                    if op1 == 3:
                        cliend_id = int(input("Enter the customer's identity document: "))
                        """ separator_string("Disable customer")
                        gym_selected.delete_client_membership(id_customer)
                        client = gym_selected.get_client(id_customer)
                        client.set_membership_active = False
                        client.set_is_active = False
                        separator_string(f"Customer with id: {id_customer} data")
                        print(client)
                        print(f"The user with id: {id_customer} was disabled succefully") """
                        
                        gym_selected.delete_client(cliend_id)

                    if op1 == 4:
                        separator_string("Update customer data")
                        gym_selected.update_client(Client)
                    if op1 == 5:
                        gym_selected.get_client()
                    if op1 == 6:
                        break

            if op == 2:
                while True:
                    print("----------- Membership Management -----------")
                    print("select an option by entering the index number")
                    print("1. Update membership")
                    print("2. Add new type membership to the Gym")
                    print("3. Disable type membership")
                    print("4. Disable membership client membership")
                    print("5. Back to previous menu")
                    print("-----------------------------------------")
                    op2 = options_input(ERROR_MESSAGE)
                    if op2 == 1:
                        separator_string("Update membership")
                        id_customer = int(input("Enter the customer's identity document: "))
                        print("Select the type of membership the client wants")
                        gym_selected.update_client_membership(id_customer)
                        client = gym_selected.get_client(id_customer)
                        print(client.print_membership_info)
                        print(
                            f"The membership of the client with id: {id_customer} was updated succefully"
                        )
                    if op2 == 2:
                        gym_selected.create_membership()
                        print("The new membership was added succefully")
                        print("Now current memberships are: ")
                        gym_selected.print_membership_list()

                    if op2 == 3:
                        separator_string("Disable membership")
                        id_customer = int(input("Enter the customer's identity document: "))
                        gym_selected.delete_client_membership(id_customer)
                        client = gym_selected.get_client(id_customer)
                        client.print_membership_info()
                        print(
                            f"The membership of the client with id: {id_customer} was disabled succefully"
                        )

                    if op2 == 4:
                        break
            if op == 3:
                while True:
                    print("----------- Reports -----------")
                    print("select an option by entering the index number")
                    print("1. Daily profit report")
                    print("2. Current users report")
                    print("3. New users report (joined less than a month ago)")
                    print("4. Users who entered the gym on the day report")
                    print("5. Daily general report")
                    print("6. Back to previous menu")
                    print("-----------------------------------------")
                    ERROR_MESSAGE = (
                        "Error: You must enter a valid integer number. Please try again."
                    )
                    op3 = options_input(ERROR_MESSAGE)
                    if op3 == 1:
                        date_to_search = input("Enter the desired date")
                        gym_selected.calculate_earning_peer_day(date_to_search)
                        print(
                            f"Excel file created succesfully for daily profit report of the date {date_to_search}"
                        )
                    if op3 == 2:
                        gym_selected.generate_report_current_clients()
                        print("Excel file created succesfully for current customers report")

                    if op3 == 3:
                        date_to_search = input("Enter the desired date")
                        gym_selected.generate_report_day(date_to_search)

                    if op3 == 7:
                        break
            if op == 4:
                while True:
                    print("1. User access to the gym")
                    print("2. Back to previous menu")
                    op4 = options_input(ERROR_MESSAGE)
                    if op4 == 1:

                        separator_string("Gym Acces")
                        print("enter the user's docume2nt you want to verify")
                        id_customer = int(input("Enter the customer's identity document: "))
                        gym_selected.handle_change_client_training(id_customer)
                    ERROR_MESSAGE = "Error: You must enter a valid identification document, do not use periods or spaces."
                    if op4 == 2:
                        break
                    # op_id = options_input(ERROR_MESSAGE)
            if op == 5:
                break
    if gym_option == 2:
        print("Create a gym")
        created_gym = get_params_peer_class(Gym)
        
        dummy_gyms.append(created_gym)
        print(f"The gym {created_gym.get_name} was created succesfully")
    
    if gym_option == 3:
        separator_string("See ya!")
        break

