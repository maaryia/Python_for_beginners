def jam_argham(ramz_digits):
    sum_digits = 0
    for k in ramz_digits:
        sum_digits += ramz_digits[k]
    return sum_digits

def ramz_is_ok(ramz_digits):
    if ramz_digits["five"] + ramz_digits["three"] == 14 and \
       ramz_digits["one"] == ramz_digits["two"]*2 - 1 and \
       ramz_digits["four"] == ramz_digits["two"] + 1 and \
       ramz_digits["two"] + ramz_digits["three"] == 10 and \
       jam_argham(ramz_digits) == 30:
        return True
    else:
        return False

for ramz in range(0, 100000): 
    this_ramz = str(ramz).zfill(5)
    ramz_digits = {
        "one": int(this_ramz[0]),
        "two": int(this_ramz[1]),
        "three": int(this_ramz[2]),
        "four": int(this_ramz[3]),
        "five": int(this_ramz[4])
    }
    if ramz_is_ok(ramz_digits):
        print(ramz)
        break