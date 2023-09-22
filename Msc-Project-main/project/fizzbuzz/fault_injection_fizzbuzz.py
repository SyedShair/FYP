# Description: Fault injection for FizzBuzz
# fault: fault is at line 6
def fiz_buz_func(r):
    if r % 15 == 0:
        return 'FizzBuzz'
    if r % 3 == 1:  # fault
        return 'Fizz'
    if r % 5 == 0:
        return 'Buzz'
    else:
        return r
