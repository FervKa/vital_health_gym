from datetime import datetime
import inspect


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
            entrada = input("Ingresa un número entero: ")
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


def get_params_peer_class(object_class):
    separator_string(f"Create a {object_class.__name__}")
    params = inspect.signature(object_class.__init__).parameters
    attr_values = {}
    for param_name, param in params.items():
        expected_type = param.annotation if param.annotation != inspect._empty else str
        if param_name == "self":  # Skip the 'self' parameter
            continue
        if expected_type.__name__ == "bool":
            print("Write '0' for Unavailable, '1' for Available.")
        value = input(
            f"Enter the value for '{param_name}', "
            f"(expected type: {param.annotation.__name__}): "
        )
        separator_string()
        try:
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
