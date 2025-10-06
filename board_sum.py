from termcolor import colored

def board_sum():
    print(colored("Enter q to stop program.","red"))
    while True:
        try:
            x = input("Enter numbers (only 1,2,3)(with no space ex)123213): ")
            if x.lower() == "q":
                print("Program stopped by user.")
                break
            
            # Check if the input contains only 1, 2, or 3
            if all(char in "123" for char in x):
                numbers = sorted(x) 
                result = "+".join(numbers)
                
                
                total_sum = sum(int(num) for num in x) 
                
                # Display the formatted output and the total sum
                print(f"Formatted: {result}")
                print(f"Total Sum: {total_sum}")
            else:
                print(colored("Invalid input. Please enter only the numbers 1, 2, or 3","light_red"))
                
        except Exception as e:
            print("An error occurred:", e)


board_sum()




#SECOND WAY
# def board_sum():
#     while True:
#         try:
#             x = input("Enter: ")
#             if x.lower() == "q":
#                 print("Program stopped by user.")
#                 break
            
#             x = x.split("+")
            
#             l = []
#             for i in x:
#                 l.append(int(i))
#             l.sort()
#             f_l = []
#             for i in l:
#                 f_l.append(str(i))

#             r = "+".join(f_l)
#             print(r)
#         except ValueError:
#             print("Invalid input. Please enter numbers separated by '+', or 'q' to quit.")

# board_sum()


