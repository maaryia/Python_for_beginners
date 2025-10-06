def prime_number():
    while True:
        try:
            num = int(input("Enter the number: "))
            p = 0
            
            for i in range(1, num):
                if (num % i == 0):
                    p += 1
            if (p==1):
                print("Prime")
            else:
                print("Not Prime")
            
            continue_check = input("Do you want to continue(yes/no)? ").strip().lower()
            if continue_check not in ['yes', 'y']:
                print("Goodbye")
                break
        except ValueError:
            print("print only number")
prime_number()
                            