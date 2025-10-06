def check_hello(word):
    hello = "hello"
    i = 0
    for letter in word:
        if i < len(hello) and letter == hello[i]:
            i += 1
    if i == len(hello):
        return "YES"
    else:
        return "NO"

word = input("Enter: ")
# word = input("Enter: ")
# print(check_hello(word))
result = check_hello(word)

print(result)



# def check_hello():
#     word = input("Enter: ")  # Get input directly inside the function
#     hello = "hello"
#     i = 0
    
#     for letter in word:
#         if i < len(hello) and letter == hello[i]:
#             i += 1
#     if i == len(hello):
#         return "YES"
#     else:
#         return "NO"

# # Call the function
# result = check_hello()
# print(result)