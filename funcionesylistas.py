# Desarrollar una función que pida 10 nombres de manera secuencial, los guarde en una lista y la retorne. 
# El programa principal debe invocar a la función y mostrar por pantalla el retorno.

def pedir_nombres():
    nombres = [None] * 10

    for i in range(10):
        nombre = input(f"Ingrese el nombre {i + 1}: ")
        nombres[i] = nombre

    return nombres

lista_nombres = pedir_nombres()

print(f"Los nombres ingresados son:")
print(lista_nombres)

#2 Desarrollar una función que inicialice una lista de 10 números en 0, pida 
#posición y número a guardar al usuario, lo guarde en una lista en la posición 
#solicitada aleatoriamente y la retorne. El programa principal debe invocar a la 
#función y mostrar por pantalla el retorno.

def inicializar_lista()->list:
    numeros = [0] * 10

    for i in range(len(numeros)):
        posicion = int(input("Ingrese la posicion de la lista: "))
        valor = int(input("Ingrese el valor: "))
        numeros[i] = valor


    return numeros

print(inicializar_lista())

#Desarrollar una función que pida 10 números dentro de un rango 
#especificado, validar los números solicitados dentro de ese rango, guardar en una 
#lista y retornarla. El programa principal debe invocar a la función y mostrar por 
#pantalla el retorno. 

def pedir_numeros()->list:
    lista_numeros = [0] * 10

    for i in range(len(lista_numeros)):
        numero = int(input(f"Ingrese el número {i + 1} dentro del rango 1-100: "))

        if 1 <= numero <= 100:
            lista_numeros[i] = numero
        else:
            print("Número fuera de rango. Se guardará como 0.")

    return lista_numeros

numeros_usuario = pedir_numeros()
print("Los números ingresados son:", numeros_usuario)

#4 Desarrollar una función que reciba por parámetro, una lista de números 
#y un número especificado.  La misma debe buscar el número especificado en la lista 
#y retornar “True” si existe.

def buscar_numero(nume:int, lista_numeros:list)->bool:
    for i in range(len(lista_numeros)):
        nume == False
        if i == nume:
            return True
        
lista_numeros = [20, 57, 37, 57, 24, 59, 51, 40, 29, 49, 60, 26, 52, 58, 49, 56, 20, 60, 35, 22, 31, 47, 44, 29, 60, 36, 48, 27, 48, 50, 29, 26, 47, 47, 42, 53, 38, 50, 52, 57, 35, 53, 47, 21, 28, 55, 20, 58, 25, 29]
nume = int(input("Ingrese el numero qe desee buscar: "))

numero_especifico = buscar_numero(nume, lista_numeros)
print(numero_especifico)

#5 Desarrollar una función que reciba por parámetro la lista de edades, busque a las 
#personas de menor edad (puede ser más de una) y las retorne.  El programa 
#principal deberá mostrar nombre y edad de los menores.

from lista_personas import nombres, edades


def persona_menor_edad(nombre, edades):
    persona_menor = []
    edad = 0
    for i in range(len(edades)):
        if edades[i] < 25:
            persona_menor.append((nombres[i], edades[i]))
    return persona_menor

persona_menor = persona_menor_edad(nombres, edades)

for i in persona_menor:
    print(f"Nombre: {i[0]}, Edad: {i[1]}")

# Analizar los datos del archivo listas_personas.py.  Utilizando el archivo 
#listas_personas.py. Importar los nombres a una lista. Realizar una función que 
#muestre los mismos.

from lista_personas import nombres

def lista_nombres():
    print(nombres)

lista_nombres()

