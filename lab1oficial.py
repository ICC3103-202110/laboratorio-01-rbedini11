# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 10:07:43 2021

@author: RENZO
"""
import numpy as np
from random import randint, random, sample
cards = int(input("How many pair of cards do you want to play? "))
lista = range(1,1+cards)
fila1=sample(lista, cards)
fila2 = sample(lista, cards)
matriz=np.array([fila1,fila2])
print(matriz)

x= int(input("Tell me the coordinate in x "))
while x<0 or x>cards-1:
    print ("Please, choose another coordinate")
    x= int(input("Tell me the coordinate in x "))
y= int(input("Choose a coordinate in y between -1 and 0 "))
print(matriz[-y][x])