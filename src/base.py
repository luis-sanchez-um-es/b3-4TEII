#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:22:59 2020

@author: luis
"""


'''
Práctica TEII - Bloque 4 - Código de la sesión 3 de prácticas
'''

import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from wrapper import wrapper 



# Función auxiliar: muestra la figura matplotlib pendiente y espera una pulsación de tecla:
#@profile
def show_plot_and_wait_for_key():
    plt.draw()
    plt.pause(0.01)
    input("<Hit Enter To Close>")
    plt.close()


# Función auxiliar que muestra en matplotlib los arrays de entrada y de salida:
def plot_values(values_in1, values_in2, line_else_bars=True, width=0.5):
    if line_else_bars == True:
        plt.plot(values_in1, color = 'r', label="Method 1")
        plt.plot(values_in2, color = 'g', label="Method 2") 
    else:
        plt.bar(np.arange(len(values_in1)) - width, values_in1, width=width, color='r', 
                label="Method 1")
        plt.bar(np.arange(len(values_in2)), values_in2, width=width, color='g', 
                label="Method 2")

    plt.title('Comparative of time spend between the methods'.format(["bars", "lines"][line_else_bars]))
    plt.legend()
    plt.xlabel('CasosConsiderados * 2000')
    plt.ylabel('Segundos')


# Código main:
def main():   
    # Control de argumentos de línea de comandos:
    if len(sys.argv) != 4:
        print("Uso: {} ficheroEntrada, ficheroSalida, pdfLogFile".format(sys.argv[0]))
        sys.exit(0)
        
    #reading fEntrada
    try:
        f = open(sys.argv[1])
        lista = f.readlines()
    except:
        print("No se encuentra el archivo de Entrada")
        sys.exit(-1)
        
    slist = sorted(lista)
    
    #parsing fEntrada
    try:
        for number in slist:
            N = int(number)
            if not (0 <= N <= 99999):
                raise ValueError()
    except:
        print("All values must be a int value between 0 and 99999")
        sys.exit(-1)
        
    timeOption1 = []
    timeOption2 = []
    timeOption3 = []
    
    #Creamos las soluciones
    for i in range(0,200000,2000):
        #Método 1
        t0_sol1 = time.time_ns()
        sol1 = sorted(set(slist[0:i]))
        texec_sol1 = (time.time_ns()-t0_sol1)/1.0e9
        
        print("La opcion 1: set ha tardado {} segundos en ejecutarse.".format(texec_sol1))
        
        #Método 2
        t0_sol2 = time.time_ns()
        sol2 = list(set(slist[0:i]))
        texec_sol2 = (time.time_ns()-t0_sol2)/1.0e9
        
        
        print("La opcion 2: set ha tardado {} segundos en ejecutarse.".format(texec_sol2))
    
        #Guardamos los datos para esta iteracion
        timeOption1.append(texec_sol1)
        timeOption2.append(texec_sol2)
    
    #Creamos el archivo solucion
    try:
        name = sys.argv[2]
        file = open(name, "w")
        
    except:
        print("Can't create file")
        sys.exit(-1)

    for num in sol1:
        
        file.write(str(num))
       
    
    
    # Imprimimos el grafico
    print("Comenzamos el plot de las comparativas")
    
    plot_values(timeOption1, timeOption2)
    show_plot_and_wait_for_key()
    plot_values(timeOption1, timeOption2, line_else_bars=False)
    show_plot_and_wait_for_key()

 
if __name__ == '__main__':
    main()

