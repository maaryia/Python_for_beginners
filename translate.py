from collections import OrderedDict

def translate():
    num = int(input("Enter number of dictionary entries: "))
    order = OrderedDict()

    # Read dictionary entries
    for i in range(num):
        enter = input(f"Enter entry {i + 1} : ")
        original, translate = enter.split()
        order[original] = translate

    # Read the sentence to translate
    user = input("Enter sentence to translate: ").strip()

    # Translate the sentence
    trans_word = []
    for word in user.split():
        if word in order:
            trans_word.append(order[word])  # Append translated word
        else:
            trans_word.append(word)  # Append original word if not found

    # Join and print the translated sentence
    trans_wo = " ".join(trans_word)
    print(trans_wo)

translate()  # Call the function to execute


# from collections import OrderedDict

# def translator():
#     n = int(input("num:"))
#     dictionary = OrderedDict()

#     # خواندن دیکشنری
#     for _ in range(n):
#         word, translation = input().split()
#         dictionary[word] = translation

#     sentence = input().split()

#     # ترجمه جمله
#     translated_sentence = []
#     for word in sentence:
#         if word in dictionary:
#             translated_sentence.append(dictionary[word])
#         else:
#             translated_sentence.append(word)

#     # چاپ جمله ترجمه شده
#     print(' '.join(translated_sentence))

# translator()