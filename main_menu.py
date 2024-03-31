import general_report
import user_class_gym
while True:
    print("----------- Bienvenido -----------")
    print("seleccione una opción ingresando el numero índice")
    print("1. Gestión clientes")
    print("2. Gestión membresías")
    print("3. Reportes")
    print("4. Ingreso al gimnasio")
    print("5. exit")
    print("-----------------------------------------")
    print("ingrese un número: ")
    op = int(input())
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
            op1 = int(input("Ingrese un número: "))
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
            op2 = int(input("Ingrese un número: "))
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
            op3 = int(input("Ingrese un número: "))
            if op3 == 3:
                while True:
                    print("----------- Reporte de clientes activos/inactivos -----------")
                    print("seleccione una opción ingresando el numero índice")
                    print("1. Activos")
                    print("2. Inactivos")
                    print("3. Volver al menú anterior")
                    print("-----------------------------------------")
                    op3_1 = int(input("Ingrese un número: "))
                    if op3_1 == 3:
                        break
            if op3 == 7:
                break
    if op == 4:
        while True:
            print("----------- Ingreso al gimnasio -----------")
            print("ingrese el documento del usuario que desea verificar")
            print("-----------------------------------------")
            op_id = int(input("cc "))
            break
    if op == 5:
        break

    

            
