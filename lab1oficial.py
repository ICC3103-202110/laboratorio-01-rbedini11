# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 10:07:43 2021

@author: RENZO
"""
import numpy as np
from random import randint, random, sample
def create_real_table(cards):
    lista = range(1,1+cards)
    fila1=sample(lista, cards)
    fila2 = sample(lista, cards)
    matriz=np.array([fila1,fila2])
    print(matriz)
    return(matriz)

def create_censored_table(cards):
    lista2=[]
    lista3=[]
    count=0
    while count<cards:
        lista2.append('?')
        lista3.append('?')
        count+=1
    matriz_censored=np.array([lista2,lista3])
    return(matriz_censored)
cards = int(input("How many pair of cards do you want to play? "))
player1=0
player2=0
matriz_visible=create_real_table(cards)
board=create_censored_table(cards)
truth=True
"""
def movement(cards,board):
 """
while (player1+player2)!=cards: 
    print("It´s your turn player 1")
    x1= int(input("Tell me the coordinate in x "))
    while x1<0 or x1>cards-1:
        print ("Please, choose another coordinate")
        x1= int(input("Tell me the coordinate in x "))
    y1= int(input("Choose a coordinate in y between -1 and 0 "))
    board[-y1][x1] = matriz_visible[-y1][x1]
    number1=matriz_visible[-y1][x1]
    print(board)
    x2= int(input("Tell me the coordinate in x "))
    while x2<0 or x2>cards-1:
        print ("Please, choose another coordinate")
        x2= int(input("Tell me the coordinate in x "))
    y2= int(input("Choose a coordinate in y between -1 and 0 "))
    board[-y2][x2] = matriz_visible[-y2][x2]
    number2=matriz_visible[-y2][x2]
    print(board)
    if number1==number2:
        board[-y1][x1]=' '
        board[-y2][x2]=' '
        player1+=1
        print("You made it")
    else:
        print("It´s your turn player 2")
        x1= int(input("Tell me the coordinate in x "))
        while x1<0 or x1>cards-1:
            print ("Please, choose another coordinate")
            x1= int(input("Tell me the coordinate in x "))
        y1= int(input("Choose a coordinate in y between -1 and 0 "))
        board[-y1][x1] = matriz_visible[-y1][x1]
        number1=matriz_visible[-y1][x1]
        print(board)
        x2= int(input("Tell me the coordinate in x "))
        while x2<0 or x2>cards-1:
            print ("Please, choose another coordinate")
            x2= int(input("Tell me the coordinate in x "))
        y2= int(input("Choose a coordinate in y between -1 and 0 "))
        board[-y2][x2] = matriz_visible[-y2][x2]
        number2=matriz_visible[-y2][x2]
        print(board)
        if number1==number2:
            board[-y1][x1]=' '
            board[-y2][x2]=' '
            player2+=1
       
    





"""
matriz_visible= create_real_table(cards)
board= first_move(cards)
print(matriz_visible)

cards = int(input("How many pair of cards do you want to play? "))
player1=0
player2=0
matriz_visible=create_real_table(cards)
board=create_censored_table(cards)
a=0
truth=True
while a!=2:
    print("It´s your turn player 1")
    movement(cards,board)
"""
    
    
    
    

    
        
