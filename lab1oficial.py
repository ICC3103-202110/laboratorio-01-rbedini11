# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 10:07:43 2021

@author: RENZO
"""
import numpy as np
from random import randint, random, sample
cards = int(input("How many pair of cards do you want to play? "))
player1=0
player2=0
def create_real_table(cards):
    lista = range(1,1+cards)
    fila1=sample(lista, cards)
    fila2 = sample(lista, cards)
    matriz=np.array([fila1,fila2])
    print(matriz)
def create_censored_table(cards):
    lista2=[]
    lista3=[]
    count=0
    while count<cards:
        lista2.append('?')
        lista3.append('?')
        count+=1
    matriz_censored=np.array([lista2,lista3])
    print(matriz_censored)
create_real_table(cards)
create_censored_table(cards)

"""       
x= int(input("Tell me the coordinate in x "))
while x<0 or x>cards-1:
    print ("Please, choose another coordinate")
    x= int(input("Tell me the coordinate in x "))
y= int(input("Choose a coordinate in y between -1 and 0 "))
print(matriz[-y][x])
"""