tornillos = [["to12", 65], ["to16", 86], ["to20", 65], ["to25", 45],
            ["to30", 68], ["to35", 73], ["to40", 85], ["to45", 89]]

tarugos = [["ta4", 58], ["ta5", 48], ["ta6", 64], ["ta7", 96],
          ["ta8", 36], ["ta10", 72], ["ta12", 78], ["ta14", 71]]


def continuar_programa()->bool:
    respuesta = input("\n¿Desea continuar usando el programa? (s/n): ").upper()
    return respuesta == "S"

#1 Tornillos
def encontrar_tornillos(tornillos:list, nombre:str)->bool:
    for i in range(len(tornillos)):
        if tornillos[i][0] == nombre:
            print(f"El producto se encontró.")
            retorno = True
            break
        else:
            continue
        break
    else:
        print("El producto no fue encontrado.")
        retorno = False

    return retorno

def cantidad_tornillo(tornillos:list, nombre:str):
    if encontrar_tornillos(tornillos, nombre) == True:
        for item in tornillos:
            if item[0] == nombre:
                print(f"La cantidad de {nombre} es de: {item[1]}")
                agregar = input("¿Desea agregar más stock? (s/n): ").upper()
                while agregar != "S" and agregar != "N":
                    agregar = input("¿Desea agregar más stock? (s/n): ").upper()
                if agregar == "S":
                    stock = int(input("Ingrese la cantidad: "))
                    item[1] += stock
                    print(f"Nueva cantidad de {nombre}: {item[1]}")
                break 
    

#1 Tarugos
def encontrar_tarugos(tarugos:list, nombre:str)->list:
    for i in range(len(tarugos)):
        for j in range(len(tarugos)):
            if tarugos[i][0] == nombre:
                print(f"El producto se encontró.")
                retorno = True
                break
        else:
            continue
        break
    else:
        print("El producto no fue encontrado.")
        retorno = False

    return retorno

def cantidad_tarugos(tarugos:list, nombre:str):
    if encontrar_tarugos(tarugos, nombre) == True:
        for item in tarugos:
            if item[0] == nombre:
                print(f"La cantidad de {nombre} es de: {item[1]}")
                agregar = input("¿Desea agregar más stock? (s/n): ").upper()
                while agregar != "S" and agregar != "N":
                    agregar = input("¿Desea agregar más stock? (s/n): ").upper()
                if agregar == "S":
                    stock = int(input("Ingrese la cantidad: "))
                    item[1] += stock
                    print(f"Nueva cantidad de {nombre}: {item[1]}")
                break 

#2
def verificar_stock(tornillos: list, tarugos: list, nombre: str):
    for producto in tornillos:
        if producto[0] == nombre:
            retorno = producto[1]
    
    # Busca en tarugos
    for producto in tarugos:
        if producto[0] == nombre:
            retorno = producto[1]
    
    return retorno

def vender_producto(tornillos: list, tarugos: list, nombre: str, cantidad: int):
    stock = verificar_stock(tornillos, tarugos, nombre)
    
    if stock >= cantidad:
        for producto in tornillos + tarugos:
            if producto[0] == nombre:
                producto[1] -= cantidad
                print(f"Vendidas {cantidad} unidades de {nombre}. Stock restante: {producto[1]}")
                break
    else:
        print(f"Stock insuficiente. Hay {stock} unidades de {nombre} (se necesitan {cantidad})")

#3

def listar_inventario(nombre, items):
    print(f"\n=== INVENTARIO DE {nombre.upper()} ===")
    for codigo, cantidad in items:
        print(f"{codigo}: {cantidad} unidades")
