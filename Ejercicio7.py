#7
from lista_personas import *

#Datos de los usuarios de mexico

def obtener_usuarios_mexico(nombres, telefonos, mails, address, postalZip, region, country):
    usuarios_mexico = []
    for i in range(len(country)):
        if country[i] == 'Mexico':
            usuarios_mexico.append((nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i]))
    return usuarios_mexico


usuarios_mexico = obtener_usuarios_mexico(nombres, telefonos, mails, address, postalZip, region, country)
for usuario in usuarios_mexico:
    print(f"Nombre: {usuario[0]}, Teléfono: {usuario[1]}, Email: {usuario[2]}, Dirección: {usuario[3]}, Código Postal: {usuario[4]}, Región: {usuario[5]}")


#Datos de los usuarios de brasil

def obtener_usuarios_brasil(nombre, mail, telefono):
    usuarios_brasil = []
    for i in range(len(country)):
        if country[i] == 'Brazil':
            usuarios_brasil.append((nombres[i], mails[i], telefonos[i]))
    return usuarios_brasil
    
usuarios_brasil = obtener_usuarios_brasil(nombres, mails, telefonos)
for usuario in usuarios_brasil:
    print(f"Nombre: {usuario[0]}, Email: {usuario[1]}, Teléfono: {usuario[2]}")


#Listar los datos de los usuarios mas jovenes

def obtener_usuarios_jovenes(nombres, telefonos, mails, address, postalZip, region, country):
    usuarios_jovenes = []
    for i in range(len(edades)):
        if edades[i] <= 24:
            usuarios_jovenes.append((nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i]))
    return usuarios_jovenes

usuarios_jovenes = obtener_usuarios_jovenes(nombres, telefonos, mails, address, postalZip, region, country)
for usuario in usuarios_jovenes:
    print(f"Nombre: {usuario[0]}, Teléfono: {usuario[1]}, Email: {usuario[2]}, Dirección: {usuario[3]}, Código Postal: {usuario[4]}, Región: {usuario[5]}")


#Obtener un promedio de edad

def obtener_promedio_edad(edades):
    suma = 0
    if len(edades) == 0:
        return 0
    for i in edades:
        suma += i

    promedio = suma // len(edades)

    return promedio

promedio = obtener_promedio_edad(edades)
print(f"El promedio de edad es: {promedio}")

#Usuarios brasil mayores de edad

def obtener_usuarios_mayores_br(nombres, telefonos, mails, address, postalZip, region, country):
    usuarios_mayores_br = []

    for i in range(len(country)):
        if country[i] == "Brazil" and edades[i] >= 24:
            usuarios_mayores_br.append((nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i]))

    return usuarios_mayores_br

usuarios_mayores_br = obtener_usuarios_mayores_br(nombres, telefonos, mails, address, postalZip, region, country)
for usuario in usuarios_mayores_br:
    print(f"Nombre: {usuario[0]}, Teléfono: {usuario[1]}, Email: {usuario[2]}, Dirección: {usuario[3]}, Código Postal: {usuario[4]}, Región: {usuario[5]}")


#listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 

def usuarios_mex_br_postal(nombres, telefonos, mails, address, postalZip, region, edades):
    usuarios_postal = []
    for i in range(len(postalZip)):
        if postalZip[i] > 8000 and country[i] in ["Mexico", "Brazil"]:
            usuarios_postal.append((nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i]))
    return usuarios_postal

usuarios_postal = usuarios_mex_br_postal(nombres, telefonos, mails, address, postalZip, region, country)
for usuario in usuarios_postal:
    print(f"Nombre: {usuario[0]}, Teléfono: {usuario[1]}, Email: {usuario[2]}, Dirección: {usuario[3]}, Código Postal: {usuario[4]}, Región: {usuario[5]}")


#-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años. 

def italianos_mayores_40(nombre, mail, telefono):
    usuarios_italianos = []
    for i in range(len(country)):
        if country[i] == 'Italy' and edades[i] >= 40:
            usuarios_italianos.append((nombres[i], mails[i], telefono[i]))
    return usuarios_italianos

usuarios_italianos = italianos_mayores_40(nombres, mails, telefonos)
for usuario in usuarios_italianos:
    print(f"Nombre: {usuario[0]}, Email: {usuario[1]}, Telefono: {usuario[2]}")
