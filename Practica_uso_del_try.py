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
    for num in lista_de_numeros:
        try:
            todo_hecho.append(num / divisor)
        except :
            print("No se puede dividor por 0")

print(dividida([2,4,6,8], 2))

    
