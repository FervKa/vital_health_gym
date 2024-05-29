from gym_class import Gym
from commons import options_input
from initial_data import dummy_users, dummy_lockers, dummy_memberships
from membership_class import Membership

# ------------ Creating the initial memberships ------------#

# ------------ Creating the initial lockers ------------#


# ------------ Creating the initial gym ------------#
michael_gym = Gym(
    3221231, "Michael Gym", "Calle 123", dummy_users, dummy_lockers, dummy_memberships
)
# ------------ Creating the initial users ------------#
""" michael_gym.add_client(
    999999,
    "Julian",
    "Caribe",
    19,
    "1212121212",
    True,
    three_months_membershipership,
    False,
) """
michael_gym.get_membership_list
""" michael_gym.update_membership_date(999999, three_months_membershipership, "2023-05-27") """
""" for user in michael_gym.get_clients_list:
    print(
        f"Name: {user.get_name}, Membership: {user.get_membership_data.get_date_last_payment}"
    ) """


# ---------- Manejo de excepciones en el input ----------#

""" while True:
    print("----------- Bienvenido -----------")
    print("seleccione una opción ingresando el numero índice")
    print("1. Gestión clientes")
    print("2. Gestión membresías")
    print("3. Reportes")
    print("4. Ingreso al gimnasio")
    print("5. exit")
    print("-----------------------------------------")

    ERROR_MESSAGE = "Error: Debes ingresar un número entero válido. Intenta nuevamente."
    op = options_input(ERROR_MESSAGE)

    if op == 1:
        while True:
            print("----------- Gestión clientes -----------")
            print("seleccione una opción ingresando el numero índice")
            print("1. Ingresar cliente")
            print("2. Verificar cliente")
            print("3. Deshabilitar cliente")
            print("4. Actualizar datos del cliente.")
            print("5. Volver al menú anterior")
            print("-----------------------------------------")
            op1 = options_input(ERROR_MESSAGE)
            if op1 == 5:
                break

    if op == 2:
        while True:
            print("----------- Gestión membresías -----------")
            print("seleccione una opción ingresando el numero índice")
            print("1. Actualizar membresía")
            print("2. Ingresar nueva membresía")
            print("3. Deshabilitar membresía")
            print("4. Volver al menú anterior")
            print("-----------------------------------------")
            op2 = options_input(ERROR_MESSAGE)
            if op2 == 4:
                break
    if op == 3:
        while True:
            print("----------- Reportes -----------")
            print("seleccione una opción ingresando el numero índice")
            print("1. Reporte de ganancias del día")
            print("2. Reporte de clientes actuales")
            print("3. Reporte de clientes activos/inactivos")
            print("4. Reporte de clientes nuevos (fecha de ingreso menor a un mes)")
            print("5. Reporte usuarios que ingresaron en el día al gimnasio")
            print("6. Reporte general diario")
            print("7. Volver al menú anterior")
            print("-----------------------------------------")
            ERROR_MESSAGE = (
                "Error: Debes ingresar un número entero válido. Intenta nuevamente."
            )
            op3 = options_input(ERROR_MESSAGE)
            if op3 == 3:
                while True:
                    print(
                        "----------- Reporte de clientes activos/inactivos -----------"
                    )
                    print("seleccione una opción ingresando el numero índice")
                    print("1. Activos")
                    print("2. Inactivos")
                    print("3. Volver al menú anterior")
                    print("-----------------------------------------")
                    op3_1 = options_input(ERROR_MESSAGE)
                    if op3_1 == 3:
                        break
            if op3 == 7:
                break
    if op == 4:
        while True:
            print("----------- Ingreso al gimnasio -----------")
            print("ingrese el documento del usuario que desea verificar")
            print("-----------------------------------------")
            ERROR_MESSAGE = "Error: Debes ingresar un documento de indentidad valido, no uses puntos ni espacios."
            op_id = options_input(ERROR_MESSAGE)
            break
    if op == 5:
        break
 """
