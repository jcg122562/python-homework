
for my_int in range(101):
    if my_int % 3 == 0 and my_int % 5 == 0:
        print('FizzBuzz')
    elif my_int % 5 == 0:
        print('Buzz')
    elif my_int % 3 == 0:
        print('Fizz')
    else:
        print(my_int)

