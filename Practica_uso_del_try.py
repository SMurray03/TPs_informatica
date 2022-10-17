#Ejercicio 1

lista_super = ["tomate", "fideos", "arvejas", "detergente", "jabón", "alcohol"]

try:
    lista_super + "arroz"
except TypeError:
    print("Muy mal")
finally:
    print("Sarasa")

#Ejercicio 2
n = []

def dividida(lista_de_numeros, divisor):
    todo_hecho = []
    
    
    try:
        for num in lista_de_numeros:
          todo_hecho.append(num / divisor)

    except  ZeroDivisionError:
            
             print("No se puede dividor por 0")

dividida([2], 0)

    
