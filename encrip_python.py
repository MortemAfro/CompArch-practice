import numpy as np
import ctypes
import time
import statistics
import math
import matplotlib.pyplot as plt 

def encrip_python(palabra):    #Volvere en python mi string en una lista numpy y esta lista va a ingresarse en el C y
                        #En el C me va a botar una lista tmbn
    encriptada = palabra
    neumatico = "NEUMATICO"
    j = 0
    for i in palabra:
        if i in neumatico:
            encriptada = encriptada.replace(i,str(neumatico.index(i) + 1))
    
    return encriptada


if __name__ == '__main__':

    palabra_analizada = str(input("Ingrese el string: "))

    palabra_encriptada = encrip_python(palabra_analizada)

    print("Será ",palabra_encriptada)

    longitud = len(palabra_encriptada)

    a = np.random.rand(longitud,1)

    lib.suma_arreglo_c.argtypes = [np.ctypeslib.ndpointer(dtype = char),np.ctypeslib.ndpointer]

    #Ahora como el C no puede recibir strings volvere a mi cadena una lista
    a = np.random.rand(len(palabra_analizada),1)

