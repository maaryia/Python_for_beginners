import math

def sqrt_num():
    try:
        num = int(input("Enter the number of inputs: "))
        for _ in range(num):
            num2 = float(input("Enter a number: "))
            sqrt = math.sqrt(num2)
            print('{:.4f}'.format(sqrt))
    except ValueError:
        print("You can only enter numbers.")

sqrt_num()