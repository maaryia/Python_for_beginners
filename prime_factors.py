voles = "aeiouAEIOU"

while True:
    input_str = input("Enter your string: ")
    if not input_str.isalpha():
        print("Enter only string please!!")
        continue
    else:
        break

    
output_str = ""

for char in input_str:
    if char in voles:
        continue
    else:
        output_str += "."
        if char.islower():
            output_str += char
        else:
            output_str += char.islower()

print(output_str)


