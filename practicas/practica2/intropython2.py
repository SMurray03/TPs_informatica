#ejercicio 1




#s = input("ingrese su palabra: ")
#if s[0] != s.upper():
#    print("es minuscula")
#else:
#    print("es mayuscula")



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
#dado = int(input("Que numero te salio: "))
#if dado == 1:
#    print("Su opuesto es el 6")
#elif dado == 2:
#    print("El opuesto es el 5")
#elif dado == 3:
#    print("El opuesto es el 4")
#elif dado == 4:
#    print("El opuesto es el 3")
#elif dado == 5:
#    print("El opuesto es el 2")
#else:
#    print("Su opuesto es el 1")

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

#Ejercicio 6
#lista1 = []
#for i in range(5):
#    lista1.append(input("Inserte cadena: "))
#lista2 = list(lista1)
#lista2.reverse()
#for e in lista2:
#    print(e)

#Ejercicio 7
#l = []
#for i in range():
#    l.append(input("Ingrese su numero:"))
#for e in l:
#    print(l)

#Ejercicio 8
l1 = []
for i in range(5):
    l1.append(int(input("Ingrese sus numeros:")))
    print(l1)
l2 = []
for i in range(5):
    l2.append(int(input("Dame tus numeros:")))
    print(l2)
l3 = [l1[0] + l2[0], l1[1] + l2[1], l1[2] + l2[2], l1[3] + l2[3], l1[4] + l2[4]]
print(l3)

#Ejercicio 9




#Ejercicio 10
string = input("Inserte string: ")
diccionario = {}
for caracter in string:
    diccionario[caracter] = string.count(caracter)
print(diccionario)

#Ejercicio 14
def temperatura_media(temp_max,temp_min):
    return (temp_max + temp_min) / 2

c_de_dias = int(input("cantidad de días: "))

for dia in range(c_de_dias):
    t_maxima = float(input("Temperatura maxima: "))
    t_minima = float(input("Temperatura minima: "))
    print("La temperatura media del día es de " + str(temperatura_media(t_maxima,t_minima)) + " grados")
