import random
from colorama import Fore, Style

def rand_game():
    answer = random.randint(0, 10)
    name = input("What is your name? ")

    while True:
        try:
            guess = int(input("What is your guess? "))
            if 0 <= guess <= 5:
                if guess == answer:
                    print("Woww you did it", name)
                    break
                elif guess > answer:
                    print("Mine is smaller")
                else:
                    print("Mine is larger")
            else:
                print("Error: You can only choose a number between 0 and 5.")        
        except ValueError:
            print(f"{Fore.RED}Please enter a number{Style.RESET_ALL}")
            continue

rand_game()
