def palindrome(word):
    while True:
        try:
            word = word.lower().replace(" ","")
            # word = word.replace(" ","")

            if word == word[::-1]:
                return True
            elif not word == word[::-1]:
                return False
            else:
                raise ValueError
        
        except ValueError:
            print("Enter a word")
        
        word = input("Enter a word: ")
word = input("Enter a word: ")
print(palindrome(word))

