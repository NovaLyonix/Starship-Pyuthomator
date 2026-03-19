import os;
import shutil;
import time

guia = "Este programa tiene 4 funciones\n\n1: Crear una lista de directorios(carpetas) basandose en el contenido de cada linea del archivo config.txt \n2: Eliminar una serie de directorios basandose en la misma lista que los crea.\n3: Actualizar la lista de directorios para que lo que esta en el archivo config.txt coincida con la lista que el programa tiene\n4: Crea 'readme.txt' un manual de ayuda que explica cada una de las funciones del programa. (Es decir, este que se está leyendo.)\n\nEste programa no puede borrar nada que no esté previamente escrito en el archivo config.txt, cualquier elemento \ncuyo nombre no esté alli está excluido tanto de su creación como de su destrucción mediante el programa.\n\nEste script fue desarrollado por @NovaLyonix. "

nombres = []

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

autoheal();
opc = -1

while opc != 0:
    entrada = input("\n1: Crear directorios | 2: Borrar Directorios | 3: Actualizar Datos | 4: Crear un archivo de ayuda (ReadMe.txt) | 0: Salir\nEscribe un número:").strip();
    opc = int(entrada or 0)

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
                if folder.endswith("py") or folder.endswith("txt"):
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
        input("\n\nHas salido del programa, se cerrará la terminal")
        break


