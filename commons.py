def validate_id(id):
    if isinstance(id, int):
        return id
    else:
        raise ValueError("Invalid user ID, it must be int")

def Num_input(m_error):
    while True:
        try:
            entrada = input("Ingresa un número entero: ")
            num = int(entrada)
            return num # Salir del bucle si la conversión fue exitosa
        except ValueError:
            print(m_error)