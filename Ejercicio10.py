nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David',
'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica', 
'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge',
'JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana', 'LAUTARO', 'Leonel', 'Luisa', 
'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás',  'Nancy', 'Noelia', 'Pablo', 
'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''

notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 12, 77, 
           13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37, 42, 95, 18, 7, 
           74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37, 64, 13, 8,
           87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73, 95, 19, 47, 15, 31,
           39, 15, 74, 33, 57, 10]


lista_nombres = nombres.replace("\n"," ").split(", ")

diccionario = {}

# para agregar cosas al diccionario lo que tengo que hacer diccionario["clave"]= valor

for i in range(len(lista_nombres)):
    diccionario[lista_nombres[i]] = [notas_1[i], notas_2[i]]

# de esta forma tengo un diccionario con lo que yo quiero. tuve que usar un i porque me pedia un entero para
# recorrerlo

#queremos calcular el promedio de cada estudiante

cant_estudiantes = 0
suma_promedios = 0

for clave, valor in diccionario.items():
    j = 0                               #nos va contando las iteraciones
    prom = 0                            #sumamos las notas de cada estudiante
    cant_estudiantes += 1               #sumamos la cantidad de estudiantes   
    
    
    for i in valor:   
        j += 1
        prom += i
        
    promedio = prom/j    
        
    print(f"El promedio de {clave} es {promedio}")
    
    suma_promedios += promedio 
    
promedio_general = suma_promedios/cant_estudiantes
    
print(f"El promedio general del curso es {promedio_general}")


#elijo ahora el promedio mas alto. vuelvo a calcular el promedio

mayor_promedio =0

for clave, valor in diccionario.items():
    j = 0                               
    prom = 0                           
                
    
    for i in valor:   
        j += 1
        prom += i
        
    promedio = prom/j 
    
    if promedio >= mayor_promedio:     #me quedo con la el promedio mas alto
        mayor_promedio = promedio
        nombre = clave

print(f"El mayor promedio lo tiene {nombre} con un promedio de {mayor_promedio}")        

#elegimos al estudiante con la nota mas baja

for clave, valor in diccionario.items():               
    
    nota = 100
    
    for i in valor:                #ahora elijo la nota mas baja de todas
        if i < nota:
            nota = i
            nombre = clave

print(f"La nota mas baja es de {nombre} con una nota de {nota}")
