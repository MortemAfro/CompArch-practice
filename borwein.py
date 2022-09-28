import numpy as np
import ctypes
import time
import statistics
import math
import matplotlib.pyplot as plt 

#NOTA DEL LAUMNO: COMO NO FUNCIONABA EL ALGORITMO DESCRITO EN EL TEXTO SE UTILIZO UNO DE WIKIPEDIA QUE IGUALMENTE ES LA
#CUADRATICA DE BORWEIN
def borwein_py(n): #n seran las iteraciones
    x_o = math.sqrt(2)
    y_o = pow(2,1/4)
    pi_o = 2 + math.sqrt(2)

    x_nback = x_o
    y_nback = y_o
    pi_nback = pi_o 

    i = 1

    while(i<=n):
        
        x_n = 0.5*(math.sqrt(x_nback) + 1/(math.sqrt(x_nback)))

        y_n = (y_nback*math.sqrt(x_n) + 1/math.sqrt(x_n))/(y_nback + 1)

        pi_n = (pi_nback*x_n)/y_nback


        x_nback = x_n
        y_nback = y_n
        pi_nback = pi_n

        i = i+1

    return pi_n

if __name__ == '__main__':

    lib = ctypes.CDLL('./borwein_c.so')
    lib.borwein_c.argtypes = [ctypes.c_int]
    lib.borwein_c.restype = ctypes.c_double

    lista_num = [32,64,128,256,512]
    iteraciones = 15

    lista_1 = []                                    #iterare 15 veces y en cada una de estas iteraciones creare arreglos de n elementos
    lista_2 = []

    lista_error_py_pro = []
    lista_error_c_pro = []


    for n in lista_num:
        print(n)

        lista_borwein_py = []
        lista_borwein_c = []

        lista_error_py = []
        lista_error_c = []

        for it in range(iteraciones):
            #Calculo en Py
            tic1 = time.time()
            pi_calculado_py = borwein_py(n)
            toc1 = time.time()

            error_py = abs(pi_calculado_py-math.pi)
            lista_error_py.append(error_py)

            lista_borwein_py.append(1e6*(toc1-tic1))

            #Calculo en C
            tic2 = time.time()
            pi_calculado_c = lib.borwein_c(n)
            toc2 = time.time()

            error_c = abs(pi_calculado_c-math.pi)
            lista_error_c.append(error_c)

            lista_borwein_c.append(1e6*(toc2-tic2))

        lista_1.append(statistics.mean(lista_borwein_py))
        lista_2.append(statistics.mean(lista_borwein_c))

        lista_error_py_pro.append(statistics.mean(lista_error_py))
        lista_error_c_pro.append(statistics.mean(lista_error_c))

print("Error promedio en Python: ",statistics.mean(lista_error_py_pro))
print("Error promedio en C: ", statistics.mean(lista_error_c_pro))


plt.plot(lista_num,lista_1,'r-')
plt.plot(lista_num,lista_2,'b-')
plt.xlabel("Size")
plt.ylabel ("Tiempo [us]")
plt.grid
plt.savefig("borwein.png",dpi = 300)
plt.close()

#Como ya se vio que el tiempo en Python es mas lento, entonces usaremos esta como referencia del speedup   SPup = tlento / trapido
SUP1 = [i / j for i,j in zip (lista_1, lista_2)] 
plt.plot(lista_num,SUP1,'g-+')
plt.xlabel("Tamaño del vector")
plt.ylabel("Tiempo [ms")
plt.grid
plt.savefig("speedup-borwein",dpi=300)
plt.close()     