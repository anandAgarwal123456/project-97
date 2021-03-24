import random

rand = random.randInt(1,9)
number = 9
chances = 4



while chances < 4:
    msg = 'Enter a number (between 1 and 9):'
    guess1 = input('enter your guess:')

    if (guess1 < 4) :
        print('Your guess was too low:' + 'guess a number higher than 4') 
        input('enter your guess:')
    elif (guess1 > 4 and < 8):   
        print('Your guess was too low' + 'guess a number higher than' + guess1 
        input('enter your guess:')
    elif (guess1 > 6 and < 8):   
        print('Your guess was too low' + 'guess a number higher than' + guess1 
        input('enter your guess:')    
    elif (guess1 > 7 and < 9):   
        print('Your guess was too low' + 'guess a number higher than' + guess1 
        input('enter your guess:')    
    elif(guess1===number):
        print('CONGRATULATIONS YOU WON!!')
        break

    if not chances < 5:
        print('YOU LOSE!!! the number is' + number) 
