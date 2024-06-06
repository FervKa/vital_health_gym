from datetime import datetime
from gym_class import Gym
from commons import (
    options_input,
    get_current_date,
    separator_string,
    get_params_peer_class,
    valid_id,
)
from initial_data import (
    dummy_gyms,
)


GYM_SELECTED = None

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
        while True:
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

            GYM_OP_OPTION = int(options_input(ERROR_MESSAGE))

            if 1 <= GYM_OP_OPTION <= len(dummy_gyms):
                GYM_SELECTED = dummy_gyms[GYM_OP_OPTION - 1]
                print(f"Gym selected: {GYM_SELECTED.get_name}")
                break
            else:
                separator_string()
                print("Error: Selection out of range. Please select a valid number.")

        while True:
            separator_string(f"Welcome to {GYM_SELECTED.get_name} ")
            print("Select an option by entering the index number: ")
            print()
            print("1. User Management.")
            print("2. Membership Management.")
            print("3. Reports.")
            print("4. Gym Access.")
            print("5. Lockers Management.")
            print("6. Back to previous menu..")
            separator_string()

            op = options_input(ERROR_MESSAGE)

            if op == 1:
                while True:
                    separator_string("User management ")
                    print("Select an option by entering the index number: ")
                    print()
                    print("1. Add user.")
                    print("2. Verify user exist.")
                    print("3. Delete user.")
                    print("4. Update user data.")
                    print("5. Show all users.")
                    print("6. Disable user membership.")
                    print("7. Handle client status.")
                    print("8. Back to previous menu.")
                    separator_string()
                    op1 = options_input(ERROR_MESSAGE)
                    if op1 == 1:
                        GYM_SELECTED.save_user()
                    if op1 == 2:
                        separator_string("Verify user")
                        client_id = valid_id("Enter the user's identity document: ")
                        GYM_SELECTED.get_client_info(client_id)
                    if op1 == 3:
                        cliend_id = valid_id("Enter the customer's identity document: ")
                        GYM_SELECTED.delete_client(cliend_id)

                    if op1 == 4:
                        separator_string("Update customer data")
                        GYM_SELECTED.update_client()

                    if op1 == 5:
                        separator_string("Clients list ")
                        GYM_SELECTED.get_client()

                    if op1 == 6:
                        separator_string("Disable membership")
                        id_customer = valid_id(
                            "Enter the customer's identity document: "
                        )
                        GYM_SELECTED.delete_client_membership(id_customer)
                        client = GYM_SELECTED.get_client(id_customer)
                        client.print_membership_info()
                        print(
                            f"The membership of the client with id: {id_customer}\n"
                            f" was disabled succefully"
                        )
                    if op1 == 7:
                        cliend_id = valid_id("Enter the customer's identity document: ")
                        GYM_SELECTED.handle_client_status(cliend_id)

                    if op1 == 8:
                        break

            if op == 2:
                while True:
                    separator_string("Membership Management ")
                    print("select an option by entering the index number")
                    print("1. Update client membership.")
                    print("2. Create a new gym membership.")
                    print("3. Show all memberships.")
                    print("5. Back to previous menu")
                    separator_string()
                    op2 = options_input(ERROR_MESSAGE)
                    if op2 == 1:
                        separator_string("Update membership")
                        id_customer = valid_id(
                            "Enter the customer's identity document: "
                        )
                        print("Select the type of membership the client wants")
                        GYM_SELECTED.update_client_membership(id_customer)
                        client = GYM_SELECTED.get_client(id_customer)
                        print(client.print_membership_info)
                        print(
                            f"The membership of the client with id: {id_customer} was updated succefully"
                        )
                    if op2 == 2:
                        GYM_SELECTED.create_membership()
                        print("The new membership was added succefully")

                    if op2 == 3:
                        GYM_SELECTED.print_membership_list()
                    if op2 == 5:
                        break
            if op == 3:
                while True:
                    separator_string("Reports ")
                    print("Select an option by entering the index number")
                    print("1. Daily profit report.")
                    print("2. Current users report.")
                    print("3. Attended users peer day.")
                    print("4. Back to previous menu.")
                    separator_string()
                    ERROR_MESSAGE = "Error: You must enter a valid integer number. Please try again."
                    op3 = options_input(ERROR_MESSAGE)
                    if op3 == 1:
                        while True:
                            print()
                            print("1. To enter a date. ")
                            print("2. For today's report.  ")
                            report_selected = options_input(ERROR_MESSAGE)
                            if report_selected == 1:
                                try:
                                    date_selected = input(
                                        "Enter the date of the desired report (YYYY-MM-DD): "
                                    )
                                except ValueError:
                                    print(
                                        "Error: Invalid date format. Please enter the date in YYYY-MM-DD format."
                                    )
                                    continue
                                GYM_SELECTED.calculate_earning_peer_day(date_selected)
                                break
                            if report_selected == 2:
                                GYM_SELECTED.calculate_earning_peer_day(
                                    get_current_date()
                                )
                                break

                    if op3 == 2:
                        GYM_SELECTED.generate_report_current_clients()
                        print(
                            "Excel file created succesfully for current customers report"
                        )
                    if op3 == 3:
                        date_to_search = input("Enter the desired date: ")
                        try:
                            GYM_SELECTED.generate_report_day(
                                datetime.strptime(date_to_search, "%Y-%m-%d")
                            )
                        except ValueError:
                            print(
                                "Error: Invalid date format. Please enter the date in YYYY-MM-DD format."
                            )

                    if op3 == 4:
                        break
            if op == 4:
                while True:
                    print("1. User access to the gym")
                    print("2. Back to previous menu")
                    op4 = options_input(ERROR_MESSAGE)
                    if op4 == 1:
                        separator_string("Gym Access")
                        print("enter the user's docume2nt you want to verify")
                        id_customer = valid_id(
                            "Enter the customer's identity document: "
                        )
                        GYM_SELECTED.handle_change_client_training(id_customer)
                    ERROR_MESSAGE = "Error: You must enter a valid identification document, do not use periods or spaces."
                    if op4 == 2:
                        break
            if op == 5:
                separator_string("Lockers Management ")
                print("Select an option by entering the index number: ")
                print("1. Assign locker.")
                print("2. Create locker.")
                print("3. Show all lockers.")
                print("4. Show empty lockers.")
                print("5. Back to previous menu.")
                separator_string()

                lockers_option = options_input(ERROR_MESSAGE)
                if lockers_option == 1:
                    separator_string("Assign locker")
                    client_id = valid_id("Enter the customer's identity document: ")
                    print()
                    cliend_found = GYM_SELECTED.get_client(client_id)
                    GYM_SELECTED.assign_lockers(client_id, cliend_found.get_name)

                if lockers_option == 2:
                    GYM_SELECTED.create_locker()

                if lockers_option == 3:
                    GYM_SELECTED.print_all_lockers(True)

                if lockers_option == 4:
                    GYM_SELECTED.get_empty_lockers(True)

                if lockers_option == 5:
                    break
            if op == 6:
                break
    if gym_option == 2:
        print("Create a gym")
        created_gym = get_params_peer_class(Gym)

        dummy_gyms.append(created_gym)
        print(f"The gym {created_gym.get_name} was created succesfully")

    if gym_option == 3:
        separator_string("See ya!")
        break
