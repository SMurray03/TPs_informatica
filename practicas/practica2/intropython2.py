#ejercicio 1
from locale import locale_alias


def es_mayus_o_minus(str):
    if str[0:1] == str.upper():
        return "es mayuscula"
    else:
        return "es minuscula"

print(es_mayus_o_minus("Lona"))  