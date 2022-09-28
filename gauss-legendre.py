import numpy as np
import ctypes
import time
import statistics
import math
import matplotlib.pyplot as plt

def gauss_legendre(n):  #n será las iteraciones que se quieran
    a_o = 1
    b_o = 1/(math.sqrt(2))
    t_o = 0.25

    a_n = a_o
    b_n = b_o
    t_n = t_o

    for i in range(n+1):
        a_nplus = 0.5*(a_n + b_n)
        b_nplus = math.sqrt(a_n*b_n)

        t_nplus = t_n - (pow(2,i))*pow(a_n-a_nplus,2)

        pi_nplus = (pow(a_nplus+b_nplus,2))/(4*t_nplus)

        a_n = a_nplus
        b_n = b_nplus
        t_n = t_nplus
    
    return pi_nplus

if __name__ == '__main__':

    lib = ctypes.CDLL('./gauss_legendre_c.so')
    lib.gauss_legendre_c.argtypes = [ctypes.c_int]
    lib.gauss_legendre_c.restype = ctypes.c_double

    lista_num = [32,64,128,256,512]
    iteraciones = 15

    lista_1 = []                                    #iterare 15 veces y en cada una de estas iteraciones creare arreglos de n elementos
    lista_2 = []

    lista_error_py_pro = []
    lista_error_c_pro = []


    for n in lista_num:
        print(n)
        

        lista_gauss_py = []
        lista_gauss_c = []

        lista_error_py = []
        lista_error_c = []

        for it in range(iteraciones):
            #Calculo en Py
            tic1 = time.time()
            pi_calculado_py = gauss_legendre(n)
            toc1 = time.time()

            error_py = abs(pi_calculado_py-math.pi)
            lista_error_py.append(error_py)

            lista_gauss_py.append(1e6*(toc1-tic1))

            #Calculo en C
            tic2 = time.time()
            pi_calculado_c = lib.gauss_legendre_c(n)
            toc2 = time.time()

            error_c = abs(pi_calculado_c-math.pi)
            lista_error_c.append(error_c)

            lista_gauss_c.append(1e6*(toc2-tic2))

        lista_1.append(statistics.mean(lista_gauss_py))
        lista_2.append(statistics.mean(lista_gauss_c))

        lista_error_py_pro.append(statistics.mean(lista_error_py))
        lista_error_c_pro.append(statistics.mean(lista_error_c))

print("Error promedio en Python: ",statistics.mean(lista_error_py_pro))
print("Error promedio en C: ", statistics.mean(lista_error_c_pro))

plt.plot(lista_num,lista_1,'r-')
plt.plot(lista_num,lista_2,'b-')
plt.xlabel("Size")
plt.ylabel ("Tiempo [us]")
plt.grid
plt.savefig("gauss.png",dpi = 300)
plt.close()

#Como ya se vio que el tiempo en Python es mas lento, entonces usaremos esta como referencia del speedup   SPup = tlento / trapido
SUP1 = [i / j for i,j in zip (lista_1, lista_2)] 
plt.plot(lista_num,SUP1,'g-+')
plt.xlabel("Tamaño del vector")
plt.ylabel("Tiempo [ms")
plt.grid
plt.savefig("speedup-gauss",dpi=300)
plt.close()         