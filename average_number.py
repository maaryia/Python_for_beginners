from termcolor import colored
count = 0
sum = 0
print(colored("Enter -1 to stop progress","red"))

while True: 
    #get inputs from user until input == -1
    num = int(input("Enter the number: "))
    #if input == -1 thr program will break
    if num == -1:
        break
    
    count += 1
    sum += num
#calculate the average    
if count > 0:
    average =int(sum / count)
    #way2:average = int(average)
    print("Average is: ", average)
