"""

1. RNG b/w mook (rock), jji (scissors), bba (paper) 
2. user chooses b/w (3) options; have options in normal english, so if user inputs "rock" when presented options, it'll default to mook in the game
3. take string input from user and compare it against the computer's choice
    3a. if user_choice == computer_choice then tie and loop back to (3) options menu
4. determine roles (attacker, defender) and winner:
    4a. if user_choice == mook and computer_choice == jji
         user_role = attacker
         computer_role = defender
         attacker_option == user_choice_2
         defender_option == computer_choice_2
            if user_choice_2 == computer_choice_2
                print("user has won!")
            if user_choice_2 != computer_choice_2:
                if user_choice_2 == bba and computer_choice_2 == jji
                    user_role = defender
                    computer_role = attacker
                    options menu again w/ computer choosing first ---> options are presented again starting w/ computer and then user (both choices are hidden until reveal phase)
                        if user_choice 2a == computer_choice_2a:
                            print("computer has won!")
                        if user_choice 2a == bba and computer_choice_2a == mook
                            user_role = attacker
                            computer_role = defender
                            options menu again w/ user choosing first
                                if user_choice_2b == computer_choice_2b
                                    "user has won!"
                if user_choice_2 == jji and computer_choice_2 == mook
                    user_role = defender
                    computer_role = attacker
                    computer_choice_3 == computer_choice ---> options are presented again starting w/ computer and then user (both choices are hidden until reveal phase)
                if user_choice_2 == mook and computer_choice_2 == bba
                    user_role = defender
                    computer_role = attacker
                    computer_choice_3 == computer_choice ---> options are presented again starting w/ computer and then user (both choices are hidden until reveal phase)



        4b_1. if user_choice == computer_choice, then user wins match
        4b_2. if user_choice == mook and computer_choice == bba, then computer has advantage, so computer attacks; user and computer decides again
            4b_2_a. if user_choice == computer_choice then computer wins match

    4c. if user_choice == jji and computer_choice == bba then user has advantage, so user attacks; user and computer decides again
        4c1. if user_choice == mook and computer_choice == jji; computer has defended properly, but user still has an advantage, so user attacks again; user and computer decides again
        while True:
            if defender_option != attacker_option:
                    if attacker_option == jji and defender_option == bba:
                        
                attacker and defender chooses again (loop through again)
            if defender_option == attacker_option:
                print("attacker has won!")

"""
