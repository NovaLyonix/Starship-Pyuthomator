import os;
import shutil;
import time

guia = """Este programa tiene 4 funciones
1: Crear una lista de directorios(carpetas) basandose en el contenido de cada linea del archivo config.txt 
2: Eliminar una serie de directorios basandose en la misma lista que los crea.
3: Actualizar la lista de directorios para que lo que esta en el archivo config.txt coincida con la lista que el programa tiene
4: Crea 'readme.txt' un manual de ayuda que explica cada una de las funciones del programa. (Es decir, este que se está leyendo.)

Este programa no puede borrar nada que no esté previamente escrito en el archivo config.txt, cualquier elemento
cuyo nombre no esté alli está excluido tanto de su creación como de su destrucción mediante el programa. 

Detalles Tecnicos:

El programa usa conceptos como Self-Healing, Funciones y Verificación de entrada

El programa hace uso de la librerias:
'os': Para la manipulación y gestión de archivos,
'shutil': Para realizar acciones de admistración de archivos,
'time': Realizar pausas o ajustes del tiempo usando como referencia la fecha actual del sistema

El programa funciona de la siguiente manera:

(inicio) >

Se verifica que el archivo 'config.tx' existe, de no existir, lo crea >
Se impreme el titulo y las opciones >
Se recibe la decision del usuario >>>>>

< Si la decision es un caracter NO NUMERICO: Se le notifica que se incertó un valor incorrecto, y se cierra el programa para evitar errores
< Si la decision es un VALOR IMCOMPRENDIDO entre el numero de opciones: Se le notifica que no hay funcion para ese numero y se lleva de nuevo a la seleccion. 
< Si la opcion es BORRAR: Verifica que existan carpetas cuyo nombre coincida con alguna entrada en el "config.txt", si existen se borra, y si no hay ninguna coincidencia, se le notifica al usuario
< Si la opcion es CREAR: Verifica que existan carpetas cuyo nombre coincida con alguna entrada en el "config.txt", si existe, se ignora esa entrada y si no, se crea la carpeta
< Si la opcion es ACTUALIZAR: Borra su version vieja del "config.txt" que existe en el array "nombres" y la sobreescribe con lo que haya en el "config.txt" sea nuevo, viejo o lo mismo.
< Si la opcion es CERRAR: Se le notifica al usuario que salio del programa (de insertar un caracter que no es un numero, o un espacio en blanco, esta es la opcion por defecto)

(fin)
 
Este script fue desarrollado por @NovaLyonix.
"""
nombres = []

def Ventana(ancho, alto):
    if os.name == 'nt':  # Solo si estamos en Windows
        os.system(f'mode con: cols={ancho} lines={alto}')
    os.system("title: Folder_Automator (creador/eliminador) v1.2 - @NovaLyonix ")


def aclarar():

    if os.name == "nt": os.system("cls")
    else: os.system("clear")

def ayuda():
    with open("README.txt","w", encoding="utf-8") as f:
        f.write(guia)
        print("Archivo de ayuda creado. Es un archivo de texto que está en el mismo lugar que el programa.")
        input("\nPresione para continuar.")
        aclarar()

def autoheal():
    if os.path.exists("config.txt"):
        with open("config.txt","r") as f:
            for linea in f:
                limpiar = linea.strip();
                if limpiar != "":
                    nombres.append(limpiar)
    else:
        print("[!] No se encontró el archivo 'config.txt', creando uno nuevo...")
        with open("config.txt","w") as f:
            f.write("Carpeta_ejemplo1\n");
            f.write("Carpeta_ejemplo2\n");
        input("\nPresiona Enter para continuar")
        autoheal()
        aclarar()

Ventana(140, 40)
autoheal();
opc = -1

while opc != 0:

    entrada = input("\n1: Crear directorios | 2: Borrar Directorios | 3: Actualizar Datos | 4: Crear un archivo de ayuda (ReadMe.txt) | 0: Salir\nEscribe un número:").strip();
#    opc = int(entrada or -1)
    if not entrada: 
        aclarar()
        print("[Error] No puedes dejar la opcion en blanco")
        continue
    
    if entrada.isnumeric():
        opc = int(entrada)

        if opc > 4: 
            aclarar();
            print(f"[Error] El numero {opc} No tiene función asignada.")
            continue

        if opc == 4:
            ayuda()

        if opc == 3:
            nombres = [];
            with open("config.txt","r") as f:
                for linea in f:
                    limpiar = linea.strip();
                    if limpiar != "":
                        nombres.append(limpiar)
            input("\nDirectorios Actualizados.")
            aclarar()

        if opc == 2:
            yll = False
            confirmar = ""
            
            for color in nombres:
                if os.path.exists(color): 
                    if not yll:
                        confirmar = input(f"\nCarpeta: {color} ¿Eiminar? \n[Y: Yes / N: No /Yll: Yes All]").strip().upper()
                        if confirmar == "YLL": 
                            yll = True

                    if yll or confirmar == "Y": 
                        shutil.rmtree(color) 
                        print(f"[-] Eliminado: {color} ")
                        time.sleep(0.1)
                    else: 
                        print("[!] Conservado ")
            else:
                input("¡Carpeta Vacía!")
                aclarar()       

        elif opc == 1:
            if len(nombres) > 0:
                for color in nombres:
                    if not os.path.exists(color): 
                        print(f"[+] Creando: {color}/")
                        os.mkdir(color)
                        time.sleep(0.2)
                    else:
                        print(f"[=] {color}/ ya existe.")
                        time.sleep(0.2)

                print("---------------------------")
                directory = os.listdir(".")
                for folder in directory:
                    if folder.endswith("py") or folder.endswith("txt") or folder.startswith("."):
                        continue
                    else:
                        print(f"[{folder}]")
                print("---------------------------")
                input("¡Directorios creados!")
                aclarar();
            else: 
                print("¡No hay directorios que crear!")
                input("Verificar que exista contenido en el archivo config.txt")
                

        elif opc == 0:
            input("\nHas salido del programa, se cerrará la terminal")
            break
    else:
        aclarar()
        print(f"[Error]: '{entrada}' no es un número válido.")
        continue

