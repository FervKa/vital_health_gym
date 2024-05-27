def validate_id(id):
    if isinstance(id, int):
        return id
    else:
        raise ValueError("Invalid user ID, it must be int")


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
