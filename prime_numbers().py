def is_prime(n):
    avval = True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            avval = False
            break
    return avval

prime_count = 0
last_prime_number = 0

for i in range (1,10):
    if is_prime(i):
        last_prime_number = i
        prime_count = prime_count + 1

print ("")
print ("we had", prime_count,"Prime numbers")
print ("last prime number was", last_prime_number)