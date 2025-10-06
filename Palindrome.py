def palindrome(word):
    word = word.lower()
    return word == word[::-1]

while True:
    word = input("Enter a word: ")
    if not word.isalpha():
        print("Please enter only letters.")
        continue
    
    if palindrome(word):
        print("palindrome")
    else:
        print("not palindrome")
    
    con = input("Do you want to check another word? (yes or no): ").strip().lower()
    if con != "yes":
        break


#2
# def palindrome(word):
#     while True:
#         try:
#             word = word.lower()
#             word = word.replace(" ","")

#             if word == word[::-1]:
#                 return True
#             elif not word == word[::-1]:
#                 return False
#             else:
#                 raise ValueError
        
#         except ValueError:
#             print("Enter a word")
        
#         word = input("Enter a word: ")
# word = input("Enter a word: ")
# print(palindrome(word))

