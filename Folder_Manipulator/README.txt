Este programa tiene 4 funciones
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
