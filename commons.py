from datetime import datetime
import inspect
import os
from openpyxl import Workbook


def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")


def format_in_currency(data):
    return f"${data:,.0f}"


def validate_id(id):
    if isinstance(id, int):
        return id
    else:
        raise ValueError("Invalid user ID, it must be int")


def search_client(client_id, clients_list):
    return list(filter(lambda client: client.get_client_id == client_id, clients_list))


def separator_string(aditional_info=None):
    print()
    print(
        f"#-------------------------- {aditional_info if aditional_info is not None else "- "}"
        f"----------------------------#"
    )
    print()


users_list = []


def save_user(users, class_type):
    if isinstance(users, class_type):
        users_list.append(users)
    elif isinstance(users, list):
        for user in users:
            users_list.append(user)


def options_input(m_error):
    while True:
        try:
            entrada = input("Enter your selection: ")
            option_input = int(entrada)
            return option_input  # Salir del bucle si la conversión fue exitosa
        except ValueError:
            print(m_error)


def convert_value(value, expected_type):
    if value == "None":
        return None
    elif expected_type == "int":
        return int(value)
    elif expected_type == "float":
        return float(value)
    elif expected_type == "bool":
        return bool(value)
    else:
        return value


def get_params_peer_class(object_class, membership_list=[]):
    separator_string(f"Create a {object_class.__name__} ")
    params = inspect.signature(object_class.__init__).parameters
    attr_values = {}
    for param_name, param in params.items():
        expected_type = param.annotation if param.annotation != inspect._empty else str
        if param_name == "membership_data":
            if membership_list:
                for index, membership in enumerate(membership_list):
                    print(f"{index+1}. Membership: {membership.get_membership_type}")

        if param_name == "locker_data":
            attr_values[param_name] = None
            continue
        elif param_name == "created_at":
            attr_values[param_name] = ""
            continue
        elif param_name == "date_last_payment":
            attr_values[param_name] = ""
            continue
        if param_name == "self":
            continue
        if param_name == "phone_number":
            print("The phone number must be 10 digits.")
        if expected_type.__name__ == "bool":
            print("Write '0' for Unavailable, '1' for Available.")

        value = input(
            f"Enter the value for '{param_name}', "
            f"(expected type: {param.annotation.__name__}): "
        )
        separator_string()
        try:
            if param_name == "membership_data":
                attr_values[param_name] = membership_list[
                    convert_value(value, "int") - 1
                ]
            else:
                attr_values[param_name] = convert_value(value, expected_type.__name__)
        except ValueError as e:
            print(
                f"Error converting {param_name}: {e}, please write the correct value..."
            )
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            break

    class_created = object_class(**attr_values)
    return class_created


def validate_object_class(object, _class):
    if not isinstance(object, _class):
        raise TypeError("{object} must be an instance of the {_class} class.")


# validar que los atributos ingresados si los tenga la clase
def validate_atributes_class(object, properties_list):
    for prop in properties_list:
        if not hasattr(object, prop):
            raise AttributeError("{object} object does not support ")


def validate_a_directory(directory, subdirectory):
    try:
        if not os.path.isdir(directory):
            os.makedirs(directory, exist_ok=True)
            os.makedirs(subdirectory, exist_ok=True)
            return True
        elif not os.path.isdir(subdirectory):
            os.makedirs(subdirectory, exist_ok=True)
            return True
        else:
            separator_string()
            print("The directory and subdirectory already exists.")
            return False
    except Exception as e:
        print(f"Error creating the directory: {e}")
        return False


def create_a_file(file_name, headers, data, gym_name, date_time=""):
    try:
        wb = Workbook()
        ws = wb.active
        ws.append(headers)
        for row in data:
            ws.append(row)

        date_to_file = ""
        report_type = file_name.split(".")[0]
        gym_name_snake = convert_to_snake_case(gym_name)
        current_directory = os.getcwd()
        dir_report = os.path.join("reports")
        dir_gym = os.path.join(dir_report, gym_name_snake)
        directory_to_save = os.path.join(current_directory, dir_gym)
        reports_dir = os.path.join(directory_to_save, report_type)
        if date_time != "":
            date_without_underscore = date_time.replace("-", "")
            date_to_file = (
                f"{date_without_underscore}{datetime.now().strftime('%H%M%S')}"
            )
        else:
            date_to_file = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name_with_date = report_type + f"_{date_to_file}.xlsx"
        file_path = os.path.join(reports_dir, file_name_with_date)
        if validate_a_directory(directory_to_save, reports_dir):
            separator_string("Creating the directory...")
            print(f"The directory '{dir_report}' and '{report_type}' was created.")

        else:
            separator_string(f"{dir_report} already exists.")
            print()

        separator_string("Creating the file...")
        """ wb.save(file_path) """
        print(f"The file '{file_name_with_date}' was created.")
        separator_string()
    except Exception as e:
        print(f"Error creating the file: {e}")


def get_headers(class_type):
    headers = []
    params = inspect.signature(class_type.__init__).parameters
    for param_name, param in params.items():
        if (
            param_name == "self"
            or param_name == "locker_data"
            or param_name == "membership_data"
        ):
            continue

        headers.append(param_name.upper())
    return headers


def convert_to_snake_case(gym_name):
    name = gym_name.lower()
    name = name.replace(" ", "_")
    return name


def valid_id(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a valid ID: ")
