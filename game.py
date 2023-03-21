from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")

#tenemos los contadores para las opciones correctas e incorrectas
m = 0
j = 0
p = 0
l = 0

for i in range(0, times):
# Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)

    #separamos en casos para que el numero2 no sea nulo
    
    if number_2 != 0:
        print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
        result = float(input("resultado: "))
        if operator == "+":
            resultado = number_1 + number_2
        elif operator == "-":
            resultado = number_1 - number_2
        elif operator == "*":
            resultado = number_1*number_2
        else: 
            resultado = number_1/number_2                
        if result == resultado: 
            print("El resultado es correcto!! :-)")
            p = p+1
        else: 
            print("El resultado es incorrecto :'(")
            l = l+1
                    
    else:
        operators = ["+", "-", "*"]
        operator = choice(operators)
        print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
        # Le pedimos al usuario el resultado
        result = input("resultado: ")
        if operator == "+":
            resultado = number_1 + number_2
        elif operator == "-":
            resultado = number_1 - number_2
        elif operator == "*":
            resultado = number_1*number_2              
        if result == resultado: 
            print("El resultado es correcto!! :-)")
            m = m+1
        else: 
            print("El resultado es incorrecto :'(")
            j = j+1
        
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")

print(m, p, j, l)
print(m+p, j+l)

print(f" Tuviste {m+p} resultados correctos y {j+l} resultados incorrectos")

