def second_old():
    max_age = 0
    second_age = 0
    while True:
        age = int(input("Enter your age: "))
        if age == -1:
            break
        try:    
            if age >= 10 and age <= 90:
                if age > max_age:
                    second_age = max_age
                    max_age = age
                elif age > second_age:
                    second_age = age
            else:
                print("age should between 10 - 90")
        except ValueError:
            print("You can only enter numbers")
        except KeyboardInterrupt:
            print("Use keyboard")
        except:
            print("Invalid")
    print (max_age, second_age)
second_old()
        
                