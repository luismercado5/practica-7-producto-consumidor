# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 13:40:52 2023

@author: luis mercado
"""

import threading
import time
import tkinter as tk
import random

# define el objeto estacionamiento
estacionamiento = []

# define control de bloqueo, esto evita que el programa se cierre al llenarse o vaciarse el estacionamiento
lock = threading.Lock()

# define el tamaño maximo del estacionamiento
capacidad_Max = 10

# define la funcion del productor
def producer(frecuencia_llegada):
    global estacionamiento
    while True:
        # espera a que el usuario especifique el tiempo
        time.sleep(frecuencia_llegada)

        # crea un bloqueo
        lock.acquire()

        # checa que el estacionamiento no esta lleno
        if len(estacionamiento) >= capacidad_Max:
            print("estacionamiento lleno, no pueden entrar mas autos.")

        else:
            # genera un el objeto carro
            nuevo_carro = "Carro " + str(random.randint(1,100))

            # añade un carro al estacionamiento
            estacionamiento.append(nuevo_carro)
            print("carro entrando:", nuevo_carro)

       
        lock.release()

# define la funcion consumidor
def consumer(frecuencia_salida):
    global estacionamiento
    while True:
        # espera a que el usuario especifique el tiempo de salida
        time.sleep(frecuencia_salida)

        # crea ub bloqueo
        lock.acquire()

        # checa que el estacionamiento no este vacio
        if len(estacionamiento) == 0:
            print("estacionamiento vacio, no hay carros por salir.")

        else:
            # remueve el primer carro
            saliendo = estacionamiento.pop(0)
            print("carro saliendo:", saliendo)

        
        lock.release()

# 
def gui():
    # crea la ventana 
    window = tk.Tk()
    window.title("simulador de estacionamiento")
    window.config(bg="dark blue")
    window.geometry("800x600")
    

    #
    entrada_label = tk.Label(window, text="ingresa los datos en segundos")
    entrada_label.grid(row=0, column=0, padx=10, pady=10)
    entrada_label.config(bg="grey")
    entrada_label.config(font="MarioLuigi2")
    # crea la entrada de frecuencias
    llegada_label = tk.Label(window, text="frecuencia de llegada:")
    llegada_label.grid(row=2, column=2, padx=10, pady=10)
    llegada_label.config(bg="dark green")
    llegada_label.config(font="MarioLuigi2")
    
    llegada_entry = tk.Entry(window)
    llegada_entry.grid(row=5, column=2, padx=10, pady=10)

    salida_label = tk.Label(window, text="frecuencia de salida:")
    salida_label.grid(row=6, column=2, padx=10, pady=10)
    salida_label.config(bg="dark red")
    salida_label.config(font="MarioLuigi2")
 
    salida_entry = tk.Entry(window)
    salida_entry.grid(row=7, column=2, padx=10, pady=10)

    # define los comandos de entrada de frecuencia
    def inicio():
     
    
        # obtiene las entradas
        frecuencia_llegada = float(llegada_entry.get())
        frecuencia_salida = float(salida_entry.get())

        # crea el hilo de productor consumidor
        producer_thread = threading.Thread(target=producer, args=(frecuencia_llegada,))
        consumer_thread = threading.Thread(target=consumer, args=(frecuencia_salida,))
        producer_thread.start()
        consumer_thread.start()



    # crea el boton start
    inicio_button = tk.Button(window, text="iniciar", command=inicio)
    inicio_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
   

    # start the main loop
    window.mainloop()
    

# create and start the GUI thread
gui_thread = threading.Thread(target=gui)
gui_thread.start()