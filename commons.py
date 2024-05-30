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

def separator_string(aditional_info = None):
    return print(f"#---------------- {aditional_info if aditional_info is not None else "-"} ------------------#")
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
    if expected_type == int:
        return int(value)
    elif expected_type == float:
        return float(value)
    elif expected_type == bool:
        return value.lower() in ["true", "1", "yes"]
    else:
        return value
