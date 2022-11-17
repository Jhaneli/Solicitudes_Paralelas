import logging
import psutil
import struct
from concurrent.futures import ThreadPoolExecutor

#Pasa saber que hilo se está utilizando --
logging.basicConfig(level = logging.DEBUG,format ='%(threadName)s: %(message)s')

##############################################
# Función catidad de IDS utilizando el .logging para imprimir los datos guardados.
# Recolección de datos solicitados con librería Psutil.pids.
def Solicitud_1():
    x = len(psutil.pids())
    logging.info(f'Cantidad de IDS:{x}. \n' )

##############################################
# Función catidad de Procesadores físicos utilizando el .logging para imprimir los datos guardados.
# Recolección de datos solicitados con librería Psutil.cpu_count.
def Solicitud_2():
     cpus_count = psutil.cpu_count(logical=False)
     x = cpus_count
     logging.info(f'Cantidad de procesadores:{x}. \n' )

 ##############################################
# Función catidad de RAM utilizando el .logging para imprimir los datos guardados.
# Recolección de datos solicitados con librería Psutil.virtual_memory.

def Solicitud_3(): 

    x = psutil.virtual_memory().total
    logging.info(f'Cantidad de Memoria Ram:{x} bytes. \n') 

##############################################
# Función de solicitud del bus de datos utilizando el .logging para imprimir los datos guardados.
# Recolección de punteros o variables de 4/8 con librería struct.calcsize. 
# Multiplicamos por 8 para recoger el resultado esperado.

def Solicitud_4(): 

    x = struct.calcsize('P')*8
    logging.info(f'Cantidad de bus de datos :{x}. \n' )

##############################################
# Función catidad de Hilos utilizando el .logging para imprimir los datos guardados.
# Con librería Psutil.cpu_count(logical = False), Psutil.cpu_count(logical = True) y guardamos los datos de los cores y procesadores logicos respectivamente.
def Solicitud_5(): 

    A = psutil.cpu_count(logical=False)
    B = psutil.cpu_count(logical=True)
    x = A*B
    logging.info(f'Cantidad de hilos:{x}. \n' )



#  Bloqueo condicional dependiente del accionar del usuario 
 
if __name__ == '__main__':

 # Limitar los hilos a: "5" para evitar problemas al utilizar la computadora con otros programas abiertos

    executor = ThreadPoolExecutor(max_workers = 5)

# Ejecutar las funciones realizadas, con los datos obtenidos, en el orden asignado. 
 
    executor.submit(Solicitud_1)
    executor.submit(Solicitud_2)
    executor.submit(Solicitud_3)
    executor.submit(Solicitud_4)
    executor.submit(Solicitud_5) 
    

     
