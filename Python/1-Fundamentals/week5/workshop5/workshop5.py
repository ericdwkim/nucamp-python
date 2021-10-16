import random


def guess_random_number(tries, start, stop):
    rand_num = random.randint(start, stop)
    # print(rand_num)
    while tries != 0:
        print(f'Number of tries remaining: {tries}')
        user_guess = int(input("Guess a # b/w 0 and 10: "))
        if user_guess == rand_num:
            print("You guessed the correct #")
            return
        elif user_guess < rand_num:
            print("guess higher")
            tries -= 1
        elif user_guess > rand_num:
            print("guess lower!")
            tries -= 1
        else:
            print("you have failed at life")


def guess_random_num_linear(tries, start, stop):
    rand_num = random.randint(start, stop)
    print(f'the target num is {rand_num}')
    num_array = []
    x = start
    comp_guess = int(tries)
    while x < stop:
        num_array.append(x)
        x += 1
    # print(num_array, comp_guess)

    for i in num_array:
        if comp_guess > 0:
            if i == rand_num:
                print("you guessed the correct #")
                return
            elif i < rand_num:
                print("guess higher")
                tries -= 1
            elif i > rand_num:
                print("guess lower")
                tries -= 1
            else:
                print(f'you failure, the target # was {rand_num}')
        if comp_guess == 0:
            print("The program has failed to guess the correct #")
            break


"""
test task 1

"""

# guess_random_number(5, 0, 10)

guess_random_num_linear(5, 0, 10)
