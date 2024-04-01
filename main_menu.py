import general_report
import user_class_gym

#---------- Manejo de excepciones en el input ----------#
def Num_input(m_error):
    while True:
        try:
            entrada = input("Ingresa un número entero: ")
            num = int(entrada)
            return num # Salir del bucle si la conversión fue exitosa
        except ValueError:
            print(m_error)
    
while True:
    print("----------- Bienvenido -----------")
    print("seleccione una opción ingresando el numero índice")
    print("1. Gestión clientes")
    print("2. Gestión membresías")
    print("3. Reportes")
    print("4. Ingreso al gimnasio")
    print("5. exit")
    print("-----------------------------------------")

    m_error = "Error: Debes ingresar un número entero válido. Intenta nuevamente."
    op = Num_input(m_error)

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
            op1 = Num_input(m_error)
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
            op2 = Num_input(m_error)
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
            m_error = "Error: Debes ingresar un número entero válido. Intenta nuevamente."
            op3 = Num_input(m_error)
            if op3 == 3:
                while True:
                    print("----------- Reporte de clientes activos/inactivos -----------")
                    print("seleccione una opción ingresando el numero índice")
                    print("1. Activos")
                    print("2. Inactivos")
                    print("3. Volver al menú anterior")
                    print("-----------------------------------------")
                    op3_1 = Num_input(m_error)
                    if op3_1 == 3:
                        break
            if op3 == 7:
                break
    if op == 4:
        while True:
            print("----------- Ingreso al gimnasio -----------")
            print("ingrese el documento del usuario que desea verificar")
            print("-----------------------------------------")
            m_error = "Error: Debes ingresar un documento de indentidad valido, no uses puntos ni espacios."
            op_id = Num_input(m_error)
            break
    if op == 5:
        break

    

            
