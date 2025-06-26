#Escreva uma função que simule o lançamento de um dado de 6 faces (use random.randint).
import random

def roll_dice():
    result = random.randint(1, 6)
    print(f"The dice roll result is: {result}")


roll_dice()
