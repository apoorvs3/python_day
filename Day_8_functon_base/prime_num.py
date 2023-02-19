def prime_checker(number):
    flag = True
    for num in range(2, int(number / 2) + 1):
        if number % num == 0:
            flag = False

    if flag:
        print('Prime number')
    else:
        print('Not a prime')


n = int(input("Check this number: "))
prime_checker(number=n)
