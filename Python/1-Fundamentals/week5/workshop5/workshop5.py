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

# test task 1
# guess_random_number(5, 0, 10)


def guess_random_num_linear(tries, start, stop):
    rand_num = random.randint(start, stop)
    print(f'The target number is {rand_num}')

    for i in range(start, stop + 1):
        if tries <= 0:
            print("The program has failed to guess the correct number.")
            break
        if i == rand_num:
            print("The progam has guessed the correct number!")
            return
        elif i < rand_num:
            print(f'The program is guessing... {i}')
        elif i > rand_num:
            print(f'The program is guessing... {i}')
        tries -= 1


# test task 2
guess_random_num_linear(5, 0, 10)
