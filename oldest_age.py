def older_age():
    max_age = 0
    while True:
        age = input("Enter your age: ")
        if age == "-1":
            break
        try:
            age = int(age)
            if age >= 10 and age <= 90:
                if age > max_age:
                    max_age = age
            else:
                print("Age should be between 10 and 90.")
        except ValueError:
            print("Please enter a number!")
        except KeyboardInterrupt:
            print("\nUse keyboard!")
        except:
            print("Invalid input")
    print("The oldest one is:", max_age)

older_age()



#1..... def older_age():
#     max_age = 0
#     age = int(input("Enter your age: "))        
#     while age != -1:
#         try:
#             if age >= 10 and age <= 90:
#                 if age > max_age:
#                     max_age = age
#                 else:
#                     print("age should between 10 - 99")
#         except ValueError:
#             print("Please enter a number!!")
#         except KeyboardInterrupt:
#             print("\n Use keyboard!!")
#         except:
#             print("Invalid")
#     print("The oldset one is: ", max_age)

# older_age()
                
#2.......def older_age():
#     max_age = 0
#     age = int(input("Enter your age: "))        
#     while age != -1:
#         try:
#             if age >= 10 and age <= 90:
#                 if age > max_age:
#                     max_age = age
#             else:
#                 print("Age should be between 10 and 90.")
#         except ValueError:
#             print("Please enter a number!!")
#         except KeyboardInterrupt:
#             print("\n Use keyboard!!")
#         except:
#             print("Invalid")
#         age = int(input("Enter your age: "))
#     print("The oldest one is: ", max_age)

# older_age()        



#3...... max_age = 0

# while True:
#     try:
#         age = int(input("لطفاً سن کاندیدا را وارد کنید: "))
#         if age < 0:
#             break
#         if age >= 10 and age <= 90:
#             if age > max_age:
#                 max_age = age
#         else:
#             print("ورودی نامعتبر! سن باید در بازه ۱۰ تا ۹۰ سال باشد.")
#     except ValueError:
#         print("ورودی نامعتبر! لطفاً یک عدد صحیح وارد کنید.")
#     except KeyboardInterrupt:
#         print("\nلطفاً اعداد را با استفاده از کیبورد وارد کنید.")
#     except:
#         print("خطای نامشخص!")

# print(f"بزرگترین سن کاندیدا: {max_age}")


# 4........max_age = 0

# age = int(input("لطفاً سن کاندیدا را وارد کنید: "))
# while age != -1:
#     if age >= 10 and age <= 90:
#         if age > max_age:
#             max_age = age
#     else:
#         print("ورودی نامعتبر! سن باید در بازه ۱۰ تا ۹۰ سال باشد.")
#     age = int(input("لطفاً سن کاندیدا را وارد کنید: "))

# print(f"بزرگترین سن کاندیدا: {max_age}")

