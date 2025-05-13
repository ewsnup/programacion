from lista_personas import *

def obtener_usuarios_mexico(nombres, telefonos, mails, address, postalZip, region, country):
    usuarios_mexico = []
    for i in range(len(country)):
        if country[i] == 'Mexico':
            usuarios_mexico.append((nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i]))
    return usuarios_mexico


def obtener_usuarios_brasil(nombre, mail, telefono):
    usuarios_brasil = []
    for i in range(len(country)):
        if country[i] == 'Brazil':
            usuarios_brasil.append((nombres[i], mails[i], telefonos[i]))
    return usuarios_brasil

def obtener_usuarios_jovenes(nombres, telefonos, mails, address, postalZip, region, country):
    usuarios_jovenes = []
    for i in range(len(edades)):
        if edades[i] <= 24:
            usuarios_jovenes.append((nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i]))
    return usuarios_jovenes

def obtener_promedio_edad(edades):
    suma = 0
    if len(edades) == 0:
        return 0
    for i in edades:
        suma += i

    promedio = suma // len(edades)

    return promedio

def obtener_usuarios_mayores_br(nombres, telefonos, mails, address, postalZip, region, country):
    usuarios_mayores_br = []

    for i in range(len(country)):
        if country[i] == 'Brazil' and edades[i] >= 24:
            usuarios_mayores_br.append((nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i]))

    return usuarios_mayores_br


def usuarios_mex_br_postal(nombres, telefonos, mails, address, postalZip, region, edades):
    usuarios_postal = []
    for i in range(len(postalZip)):
        if postalZip[i] > 8000 and country[i] in ["Mexico", "Brazil"]:
            usuarios_postal.append((nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i]))
    return usuarios_postal

def italianos_mayores_40(nombre, mail, telefono):
    usuarios_italianos = []
    for i in range(len(country)):
        if country[i] == 'Italy' and edades[i] >= 40:
            usuarios_italianos.append((nombres[i], mails[i], telefono[i]))
    return usuarios_italianos


def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Datos de los usuarios de México")
    print("2. Nombre, Email y Teléfono de los usuarios de Brasil")
    print("3. Datos de los usuarios más jóvenes")
    print("4. Datos de los usuarios mayores en Brasil")
    print("5. Promedio de edad de los usuarios")
    print("6. Datos de los usuarios de México y Brasil con código postal > 8000")
    print("7. Nombre, Email y Teléfono de los usuarios italianos mayores a 40 años")
    print("8. Datos de los usuarios de México ordenados por nombre") 
    print("9. Datos de los usuarios más jovenes ordenados por edad/por nombre.")
    print("10. Datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000")
    print("11. Salir")

def opcion_menu():
    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            usuarios_mexico = obtener_usuarios_mexico(nombres, telefonos, mails, address, postalZip, region, country)
            for usuario in usuarios_mexico:
                print(f"Nombre: {usuario[0]}, Teléfono: {usuario[1]}, Email: {usuario[2]}, Dirección: {usuario[3]}, Código Postal: {usuario[4]}, Región: {usuario[5]}")
        case "2":
            usuarios_brasil = obtener_usuarios_brasil(nombres, mails, telefonos)
            for usuario in usuarios_brasil:
                print(f"Nombre: {usuario[0]}, Email: {usuario[1]}, Teléfono: {usuario[2]}")
        case "3":
            usuarios_jovenes = obtener_usuarios_jovenes(nombres, telefonos, mails, address, postalZip, region, country)
            for usuario in usuarios_jovenes:
                print(f"Nombre: {usuario[0]}, Teléfono: {usuario[1]}, Email: {usuario[2]}, Dirección: {usuario[3]}, Código Postal: {usuario[4]}, Región: {usuario[5]}")
        case "4":
            usuarios_mayores_br = obtener_usuarios_mayores_br(nombres, telefonos, mails, address, postalZip, region, country)
            for usuario in usuarios_mayores_br:
                print(f"Nombre: {usuario[0]}, Teléfono: {usuario[1]}, Email: {usuario[2]}, Dirección: {usuario[3]}, Código Postal: {usuario[4]}, Región: {usuario[5]}")
        case "5":
            promedio = obtener_promedio_edad(edades)
            print(f"El promedio de edad es: {promedio}")
        case "6":
            usuarios_postal = usuarios_mex_br_postal(nombres, telefonos, mails, address, postalZip, region, country)
            for usuario in usuarios_postal:
                print(f"Nombre: {usuario[0]}, Teléfono: {usuario[1]}, Email: {usuario[2]}, Dirección: {usuario[3]}, Código Postal: {usuario[4]}, Región: {usuario[5]}")
        case "7":
            usuarios_italianos = italianos_mayores_40(nombres, mails, telefonos)
            for usuario in usuarios_italianos:
                print(f"Nombre: {usuario[0]}, Email: {usuario[1]}, Telefono: {usuario[2]}")
        case "8":
            ordenados = usuarios_ordenados()
            for usuario in ordenados:
                print(f"Nombre: {usuario[0]}, Teléfono: {usuario[1]}, Email: {usuario[2]}, Dirección: {usuario[3]}, Código Postal: {usuario[4]}, Región: {usuario[5]}")
        case "9":
            datos_ordenados = ordenar_datos(obtener_usuarios_jovenes(nombres, telefonos, mails, address, postalZip, region, country))
            for i in datos_ordenados:
                print(i)
        case "10":
            datos_ordenados = ordenar_datos(usuarios_mex_br_postal(nombres, telefonos, mails, address, postalZip, region, edades))
            for i in datos_ordenados:
                print(i)
        case "11":
            print("Saliendo...")
        case _:
            print("Error.")

def usuarios_ordenados():
    usuarios_mexico = obtener_usuarios_mexico(nombres, telefonos, mails, address, postalZip, region, country)

    for i in range(len(usuarios_mexico)-1):
        for j in range(i+1,len(usuarios_mexico)):
            if(usuarios_mexico[i] > usuarios_mexico[j]):
                aux = usuarios_mexico[i]
                usuarios_mexico[i] = usuarios_mexico[j]
                usuarios_mexico[j] = aux
    return usuarios_mexico

def ordenar_datos(datos:list)->list:

    for i in range(len(datos)-1):
        for j in range(i+1,len(datos)):
            if (datos[i] > datos[j]):
                aux = datos[i]
                datos[i] = datos[j]
                datos[j] = aux
                
    return datos


def edad_ascendente(edades:list)->list:

    for i in range(len(edades)-1):
        for j in range(i+1,len(edades)):
            if(edades[i] > edades[j]):
                aux = edades[i]
                edades[i] = edades[j]
                edades[j] = aux
    return edades