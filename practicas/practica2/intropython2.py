#ejercicio 1




s = input("ingrese su palabra: ")
if s[0] != s.upper():
    print("es minuscula")
else:
    print("es mayuscula")



#Ejercicio 2

n = int(input("Ingrese su numero: "))

if n == 0:
    print("Es cero y es par")
elif n < 0 and n % 2 == 0:
    print ("Es par y negativo")
elif n < 0 and n % 2 != 0:
    print("Es negativo e impar")
elif n > 0 and n % 2 == 0:
    print("Es par y positivo")
else: 
    print("Es impar y positivo")

#Ejercicio 3
dado = int(input("Que numero te salio: "))
if dado == 1:
    print("Su opuesto es el 6")
elif dado == 2:
    print("El opuesto es el 5")
elif dado == 3:
    print("El opuesto es el 4")
elif dado == 4:
    print("El opuesto es el 3")
elif dado == 5:
    print("El opuesto es el 2")
else:
    print("Su opuesto es el 1")

#Ejercicio 4







#Ejercicio 5
semana = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
dia_de_semana = int(input("Inserte número del 1 al 7: "))
if dia_de_semana > 7:
    print("No es el numero adecuado")
else:
    for i in range(7):
        if i == dia_de_semana:
            print(semana[i-1])
