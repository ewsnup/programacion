def nombre_ascendente(nombres:list)->list:

    for i in range(len(nombres)-1):
        for j in range(i+1, len(nombres)):
            if(nombres [i] > nombres[j]):
                aux = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux
    return nombres

def puntos_descendentes(puntos:list)->list:
    
    for i in range(len(puntos)-1):
        for j in range(i+1,len(puntos)):
            if(puntos[i] < puntos[j]):
                aux = puntos[i]
                puntos[i] = puntos[j]
                puntos[j] = aux
    return puntos

def apellidos_ascendentes(apellidos:list)->list:
    
    for i in range(len(apellidos)-1):
        for j in range(i+1,len(apellidos)):
            if(apellidos[i] > apellidos[j]):
                aux = apellidos[i]
                apellidos[i] = apellidos[j]
                apellidos[j] = aux
    return apellidos

def nota_descendentes(nota:list)->list:
    
    for i in range(len(nota)-1):
        for j in range(i+1,len(nota)):
            if(nota[i] < nota[j]):
                aux = nota[i]
                nota[i] = nota[j]
                nota[j] = aux
    return nota

def ordenar_datos(datos:list)->list:

    for i in range(len(datos)-1):
        for j in range(i+1,len(datos)):
            if (datos[i] > datos[j]):
                aux = datos[i]
                datos[i] = datos[j]
                datos[j] = aux
                
    return datos
