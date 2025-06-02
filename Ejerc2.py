'''
Desarrollar un programa para el control de stock de una ferretería para sus artículos
de tornillos y tarugos. Los mismos se encuentran almacenados en una
cajonera de ferretería metálica con cajones.
'''
from Funciones2 import *

tornillos = [["to12", 65], ["to16", 86], ["to20", 65], ["to25", 45],
            ["to30", 68], ["to35", 73], ["to40", 85], ["to45", 89]]

tarugos = [["ta4", 58], ["ta5", 48], ["ta6", 64], ["ta7", 96],
          ["ta8", 36], ["ta10", 72], ["ta12", 78], ["ta14", 71]]


seguir = True
while seguir:
    print("\nBienvenido al menú de opciones:")
    print("1. Reponer mercadería.")
    print("2. Vender mercadería.")
    print("3. Listar inventario.")
    print("4. Salir.")
    
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        mercaderia = int(input("¿Desea reponer tornillos (1) o tarugos (2)?: "))
        while mercaderia != 1 and mercaderia != 2:
            mercaderia = int(input("Error. ¿Desea reponer tornillos (1) o tarugos (2)?: "))
        if mercaderia == 1:
            nombre = input("Ingrese el nombre del tornillo: ").lower()
            cantidad_tornillo(tornillos, nombre)
        elif mercaderia == 2:
            nombre = input("Ingrese el nombre del tarugo: ").lower()
            cantidad_tarugos(tarugos, nombre)
    elif opcion == "2":
        nombre = input("Ingrese el código del producto: ")
        cantidad = int(input("Ingrese la cantidad a vender: "))
        vender_producto(tornillos, tarugos, nombre, cantidad)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto que desea listar (en plural): ").lower()
        while nombre != "tornillos" and nombre != "tarugos":
            nombre = input("Ingrese el nombre del producto que desea listar (en plural): ").lower()
        if nombre == "tornillos":
            listar_inventario(nombre, tornillos)
        elif nombre == "tarugos":
            listar_inventario(nombre, tarugos)
    elif opcion == "4":
        seguir = False
        print("\nSaliendo del programa...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
    if not continuar_programa():
        print("\nSaliendo del programa...")
        break