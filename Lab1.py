from random import randint
number_of_cards = int(input("How many cards do you want to play? "))
player1=0
player2=0
card_1=randint(1, number_of_cards)
card_2=randint(1, number_of_cards)
if card_1 != 3:
    print("xao")
else:
    print("hola")

