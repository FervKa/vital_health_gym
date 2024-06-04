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


""" for membership in self.membership_list:
            print("#------------Membership data-----------#")
            print(
                f"Membership type: {membership.get_membership_type},\n"
                f"Membership cost:  {"${:,.0f}".format(membership.get_membership_cost)}"
            ) 
"""

""" michael_gym.update_client(Client) """
""" michael_gym.delete_client(5151213)
michael_gym.handle_client_status(6634234) """
# michael_gym.generate_report_current_clients()
memb = dummy_memberships[2]
michael_gym.assign_client_membership(5151213, memb)
michael_gym.update_client_membership(5151213, "Weekend")
client1 = michael_gym.get_client(5151213)
# michael_gym.update_assigned_client_locker(5151213)
michael_gym.delete_client_assigned_locker(5151213)

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
