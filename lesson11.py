numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    primes = numbers[i] % 2 == 0
    if primes == True:
        print('Четные числа:', primes)
        for j in range(len(numbers)):
            not_primes = numbers[i]
    if primes == False:
        print('Нечетные числа:', not_primes)
