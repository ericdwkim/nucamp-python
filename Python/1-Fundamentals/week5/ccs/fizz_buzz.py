# NOTE: first attempt

# def fizzbuzz(num):
#     for n in range(1, num+1):
#         if (n % 3 == 0) and (n % 5 != 0):
#             print("Fizz")
#         if (n % 5 == 0) and (n % 3 != 0):
#             print("Buzz")
#         if (n % 3 == 0) and (n % 5 == 0):
#             print("FizzBuzz")
#         elif (n % 3 != 0) and (n % 5 != 0):
#             print(n)


# fizzbuzz(50)

# NOTE: second attempt w/ solution improvements using `str` var

# def fizzbuzz(num):
#     for n in range(1, num + 1):
#         if (n % 3 == 0) and (n % 5 == 0):
#             str = "FizzBuzz"
#         elif (n % 3 == 0):
#             str = "Fizz"
#         elif (n % 5 == 0):
#             str = "Buzz"
#         else:
#             str = n
#         print(str)


# fizzbuzz(50)

# more advanced method

# def fizzbuzz(num):

#     [print("Fizz"*(n % 3 == 0) + "Buzz"*(n % 5 == 0) or n)
#      for n in range(1, num + 1)]


# fizzbuzz(50)
