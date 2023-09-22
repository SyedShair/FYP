def fiz_buz_func(r):
    if r % 15 == 0:
        return 'FizzBuzz'
    if r % 3 == 0:
        return 'Fizz'
    if r % 5 == 0:
        return 'Buzz'
    else:
        return r
