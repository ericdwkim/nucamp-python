def fizzbuzz(num):
    for n in range(1, num+1):
        if (n % 3 == 0) and (n % 5 != 0):
            print("Fizz")
        if (n % 5 == 0) and (n % 3 != 0):
            print("Buzz")
        if (n % 3 == 0) and (n % 5 == 0):
            print("FizzBuzz")
        elif (n % 3 != 0) and (n % 5 != 0):
            print(n)


fizzbuzz(50)
