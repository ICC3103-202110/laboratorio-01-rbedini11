
"""
Created on Tue Mar 23 10:07:43 2021

@author: RENZO
"""
import numpy as np
from random import sample

def create_real_table(cards):
    lista = range(1,1+cards)
    fila1=sample(lista, cards)
    fila2 = sample(lista, cards)
    matriz=np.array([fila1,fila2])
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
    print(matriz_censored)
    return(matriz_censored)
print("Welcome to Memory!")
cards = int(input("How many pair of cards do you want to play? "))
player1=0
player2=0
matriz_visible=create_real_table(cards)
board=create_censored_table(cards)

while (player1+player2)!=cards: 
    print("It´s your turn player 1")
    x1= int(input("Tell me the coordinate in x: "))
    while x1<0 or x1>cards-1:
        print ("Please, choose another coordinate")
        x1= int(input("Tell me the coordinate in x: "))
    y1= int(input("Choose a coordinate in y between -1 and 0: "))
    while y1!=-1 and y1!=0:
        print ("Please, choose another coordinate")
        y1= int(input("Choose a coordinate in y between -1 and 0: "))    
    board[-y1][x1] = matriz_visible[-y1][x1]
    number1=matriz_visible[-y1][x1]
    print(board)
    x2= int(input("Tell me the coordinate in x: "))
    while x2<0 or x2>cards-1:
        print ("Please, choose another coordinate")
        x2= int(input("Tell me the coordinate in x: "))
    y2= int(input("Choose a coordinate in y between -1 and 0: "))
    while y2!=-1 and y2!=0:
        print ("Please, choose another coordinate")
        y2= int(input("Choose a coordinate in y between -1 and 0: "))
    board[-y2][x2] = matriz_visible[-y2][x2]
    number2=matriz_visible[-y2][x2]
    print(board)
    if number1==number2:
        board[-y1][x1]=' '
        board[-y2][x2]=' '
        player1+=1
        print("You made it!")
        print(board)
    elif number1!=number2:
        board[-y1][x1]='?'
        board[-y2][x2]='?'
        print(board)
        print("Luck next time!")
        truth=True
        while truth:
            print("It´s your turn player 2")
            x1= int(input("Tell me the coordinate in x: "))
            while x1<0 or x1>cards-1:
                print ("Please, choose another coordinate")
                x1= int(input("Tell me the coordinate in x: "))
            y1= int(input("Choose a coordinate in y between -1 and 0: "))
            while y1!=-1 and y1!=0:
                print ("Please, choose another coordinate")
                y1= int(input("Choose a coordinate in y between -1 and 0: "))
            board[-y1][x1] = matriz_visible[-y1][x1]
            number1=matriz_visible[-y1][x1]
            print(board)
            x2= int(input("Tell me the coordinate in x: "))
            while x2<0 or x2>cards-1:
                print ("Please, choose another coordinate")
                x2= int(input("Tell me the coordinate in x: "))
            y2= int(input("Choose a coordinate in y between -1 and 0: "))
            while y2!=-1 and y2!=0:
                print ("Please, choose another coordinate")
                y1= int(input("Choose a coordinate in y between -1 and 0: "))
            board[-y2][x2] = matriz_visible[-y2][x2]
            number2=matriz_visible[-y2][x2]
            print(board)
            if number1==number2:
                board[-y1][x1]=' '
                board[-y2][x2]=' '
                player2+=1
                truth=True
                print("You made it!")
                print(board)
                if (player1+player2)==cards:
                    truth=False
            elif number1!=number2:
                board[-y1][x1]='?'
                board[-y2][x2]='?'
                truth=False
                print(board)
                print("Luck next time!")
if player1>player2:
    print("Player 1 wins, thanks to play")
elif player2>player1:
    print("Player 2 wins, thanks to play")      
else:
    print("It's a tie!, thanks to play")      
    







    
    
    
    

    
        
