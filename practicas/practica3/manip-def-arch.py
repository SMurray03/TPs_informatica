#open(path_al_archivo, modo)

#"path_al_archivo" es un objeto de tipo str que indica la ruta en la que se encuentra el archivo.
#"modo" es un objeto de tipo str que indica la forma en la que Python accederá al archivo en cuestión.

#r	abre un archivo solo para lectura
#r+	abre un archivo para lectura y escritura
#a	Abre un archivo para agregar información. Si el archivo no existe, crea un nuevo archivo para escritura
#w	Abre un archivo solo para escritura. Sobreescribe el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo para escritura
import os , glob
#os.getcwd() #Nos dice donde estamos
#os.chdir("/Users/Santi/Desktop/informatica/practicas/practica3/manip-def-arch.py/Dale Dale") #Podemos cambiar de directorio
#os.getcwd()
#os.listdir() #devuelve una lista que contiene los nombres de las entradas (archivos y directorios) del directorio indicado (path).
#os.mkdir() #creará un nuevo directorio con el nombre proporcionado como un parámetro de cadena.
#Ejercicio 1

def start_with(archivo,letra):
    count = 0
    with open(archivo, "r") as file:
        f = file.readlines()
        for line in f:
            if (line[0] == letra.lower()) or (line[0] == letra.upper()):
                count += 1
            print(len(f) - (count), "lineas de", str(archivo), "no empiezan con", letra)
            

# 2
def read_and_print_first_lines(archivo, cantidad_de_lineas):
    linea = open("Lorem.txt","r").readlines()[:cantidad_de_lineas]
    print(*linea)       
read_and_print_first_lines("Lorem.txt",2)

# 3
def read_and_print_last_lines(archivo, cantidad_de_lineas):
    linea = open("Lorem.txt","r").readlines()[-cantidad_de_lineas:]
    print(*linea)       
read_and_print_last_lines("Lorem.txt",2)

#4
def conteo_palabras_de_archivo(archivo):
    arch = open(archivo,"r")
    leer_archivo = arch.read()
    por_palabra = leer_archivo.split()
    print('El archivo tiene',len(por_palabra), "palabras.")
conteo_palabras_de_archivo("Lorem.txt")

#5
def replace_letter(entrada,salida,letter):
    with open(entrada,"r") as file, open(salida,"w") as archivo_nuevo:
        for line in file:
            archivo_nuevo.write(line.replace(letter, letter + "\n"))
replace_letter("Lorem.txt","ArchEj5.txt","l")

#6
def eliminar_saltos_de_linea(entrada,salida):
    with open(entrada,"r") as e, open(salida,"w") as s:
        for line in e:
            s.write(line.strip("\n"))
eliminar_saltos_de_linea("LaPelotaNoSeMancha.txt","ArchEj6.txt")

#7
def palabra_mas_larga(archivo):
    file = open(archivo,"r")
    leer_archivo = file.read()
    leer_palabras = leer_archivo.split()
    palabra_mas_larga_del_archivo = ""
    for palabra in leer_palabras:
        if len(palabra) > len(palabra_mas_larga_del_archivo):
            palabra_mas_larga_del_archivo = palabra
    print("La palabra más larga del archivo es",palabra_mas_larga_del_archivo,"y tiene",str(len(palabra_mas_larga_del_archivo)),"caracteres")   
palabra_mas_larga("Lorem.txt")   

#8
def GuardarContenidoDeDosArchivosEnOtro(arch1, arch2, salida):
    f1 = open(arch1,"r")
    f2 = open(arch2,"r")
    file1 = f1.read()
    file2 = f2.read()
    existing_file = open(salida, "a")
    for line in file1, file2:
        existing_file.write(line)
GuardarContenidoDeDosArchivosEnOtro("Lorem.txt","Discurso.txt","Dos_en_unoNro8.txt")

#9
def frecuencia_de_palabras(archivo):
    arch = open(archivo,"r")
    texto = arch.read()
    frec = {}
    lista_de_palabras = texto.split()
    for palabra in lista_de_palabras:
        frec[palabra] = lista_de_palabras.count(palabra) / len(lista_de_palabras)
    print(frec)
frecuencia_de_palabras("LaPelotaNoSeMancha.txt")

# 10
def unir_txt(carpeta1, nombre):
    os.chdir(carpeta1)
    textos = glob.glob("*.txt")
    os.mkdir("Resultado")
    with open("Resultado/" + nombre,"a") as s:
        for file in textos:
            with open(file,"r") as texto:
                s.write(texto.read() + "\n")
unir_txt('EjNro10Archivos','ArchivoDeSalidaDelEj10.txt')