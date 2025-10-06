import random

def guess_number():
    low = 1
    high = 99
    guess = random.randint(low, high)
    
    while True:
        print(guess)
        response = input("Smaller(s) or larger(l) or True (t): ")
        
        if response == 's':
            high = guess - 1
            guess = random.randint(low, high)
        elif response == 'l':
            low = guess + 1
            guess = random.randint(low, high)
        elif response == 't':
            print("rightt!!!!")
            break
        else:
            print("You can only choose betweeen s,l,t")

guess_number()


        
        



























