from termcolor import colored

def count_divisors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

def find_max_divisors_num():
    max_divisors = 0
    max_num = 0

    for i in range(10):
        while True:
            try:
                user_input = input(f"Enter number {i+1}: ")
                if not user_input.isdigit():
                    raise ValueError(colored("Only positive numbers are allowed!", 'light_red'))
                num = int(user_input)
                break
            except ValueError as e:
                print(e, "Try again.")

        divisors = count_divisors(num)

        if divisors > max_divisors:
            max_divisors = divisors
            max_num = num
        elif divisors == max_divisors and num > max_num:
            max_num = num

    print("Number with the maximum divisors:", max_num)
    print("Number of divisors:", max_divisors)

find_max_divisors_num()


#2. def count_factors(num):
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     return count

# max_divisors = 0
# max_number = None

# for _ in range(20):
#     number = int(input("Enter a number: "))
#     divisors = count_factors(number)
#     if divisors > max_divisors:
#         max_divisors = divisors
#         max_number = number
#     elif divisors == max_divisors and number > max_number:
#         max_number = number

# print("The number with the most divisors is:", max_number)
# print("Number of divisors:", max_divisors)
