#ejercicio 1
str = input("ingrese string: ")
print(len(str))

#ejercicio 2
un_string = input("dame un string: ")
print(un_string[4:6].upper())

#ejercicio 3
nombre = input("inserte_nombre_y_apellido: ")
print(nombre + " como andas")

#ejercicio 4
nombre_completo = input("Dame tu nombre y tus dos apellidos: ")
print(nombre_completo[0:1])

#ejercicio 5
promedio = input("inserte tres numeros: ")
print(promedio / 3)

#ejercicio 6
cant_de_min = int(input("inserte la cant de min"))
hora = cant_de_min == 60
minutos = cant_de_min % 60
print(hora,  "horas y ", minutos, "min")