"""
    Algoritmo para encontrar quanto tempo sera
    necessario esperar para obter um montante atravez 
    de um sistema de juros composto com aplicacao temporal
    de um valor fixo (mais os juros adiquiridos)
"""
import math
m = 0 # montante inicial

def montante_final(m, valor_buscado=math.pow(10,6), i=1/100):
    t = 0 # tempo inicial
    n = 0
    while n < valor_buscado:
        n += m 
        n = n*(1+i)
        t += 1

    return t

def montante(m,t, i=1/100):
    n = 0 
    for i in range(t):
        n += m
        n = n*(1+i)
    
    return n 

def det_tempo(m, i=1/100, valor_buscado=math.pow(10,6)):
    t = 0
    n = 0
    while n < valor_buscado:
        t += 1
        n += m 
        n = n*(1+i)
        
    return t

# print(montante_final(1200)/12)

