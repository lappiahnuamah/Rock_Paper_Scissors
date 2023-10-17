import time

def print_pause(string):
    print(string)
    time.sleep(2)
    
print_pause("You have just arrived at your new job!")
print_pause("You are in the elevator.")


def lobby():
    print_pause("You push the buttton for the first floor.")
    print_pause("After a few moments, you find yourself in the lobby")

def human_resource():
    print_pause("You push the buttton for the second floor.")
    print_pause("After a few moments, you find yourself in the human resources department")

def engineering():
    print_pause("You push the buttton for the third floor.")
    print_pause("After a few moments, you find yourself in the engineering department.")
    

def valid_input():
    response = input("Please enter the number for the floor you would like to visit:\n"
                    "1. Lobby\n"
                    "2. Human resources\n"
                    "3. Engineering department\n")
    if '1' in response:
        lobby()
        print_pause("Where would you like to go next?")
        valid_input()
    elif '2' in response:
        human_resource()
        print_pause("Where would you like to go next?")
        valid_input()
    elif '3' in response:
        engineering()
        print_pause("Where would you like to go next?")
        valid_input()
    else:
        print_pause("I don't know where you are mentioning")
        valid_input()
        
valid_input()


##import time
##items = []
##
##def print_sleep(message_to_print, time_to_wait):
##    print(message_to_print)
##    time.sleep(time_to_wait)
##
##print_sleep("You have just arrived at your new job!",2)
##print_sleep("You are in the elevator.",2)
##
##while True:
##    print_sleep("Please enter the number for the "
##                "floor you would like to visit:", 2)
##    floor = input("1. Lobby\n"
##              "2. Human resources\n"
##              "3. Engineering offices\n")
##    if floor == '1':
##        print_sleep("You push the button for the first floor", 2)
##        print_sleep("After a few moments, you find "
##                "yourself in the lobby.", 2)
##        if "ID card" in items:
##            print_sleep("The clerk greets you, but she has already "
##                    "given you your ID card, so there is nothing "
##                    "more to do here now.", 2)
##        else:
##            print_sleep("The clerk greets you and gives you your ID card.", 2)
##            items.append("ID card")
##        print_sleep("You head back to the elevator.", 2)
##    elif floor == '2':
##        print_sleep("You push the button for the second floor", 2)
##        print_sleep("After a few moments, you find "
##                "yourself in the human resource department.", 2)
##        if "handbook" in items:
##            print_sleep("The HR folks are busy at their desks.", 2)
##            print_sleep("There doesn't seem to be much to do here.", 2)
##        else:
##            print_sleep("The head of HR greets you.", 2)
##            if "ID card" in items:
##                print_sleep("He looks at your ID card and then" 
##                            " gives you a copy of the employee handbook.", 2)
##                items.append("handbook")
##            else:
##                print_sleep("He has something for you, but says he can't"
##                        "give it to you until you go get your ID card.", 2)
##            print_sleep("You head back to the elevator.", 2)
##    elif floor == '3':
##        print_sleep("You push the button for the third floor", 2)
##        print_sleep("After a few moments, you find youreself "
##                    "in the engineering department.", 2)
##        print_sleep("This is where you work!", 2)



###This is the complete version of the elevator game

##import time
##
##
##def print_pause(message_to_print):
##    print(message_to_print)
##    time.sleep(1)
##
##
##def intro():
##    print_pause("You have just arrived at your new job!")
##    print_pause("You are in the elevator.")
##
##
##def first_floor(items):
##    print_pause("You push the button for the first floor.")
##    print_pause("After a few moments, you find "
##                "yourself in the lobby.")
##    if "ID card" in items:
##        print_pause("The clerk greets you, but she has already "
##                    "given you your ID card, so there is nothing "
##                    "more to do here now.")
##    else:
##        print_pause("The clerk greets you and gives you your ID "
##                    "card.")
##        items.append("ID card")
##    print_pause("You head back to the elevator.")
##    ride_elevator(items)
##
##
##def second_floor(items):
##    print_pause("You push the button for the second floor.")
##    print_pause("After a few moments, you find yourself "
##                "in the human resources department.")
##    if "handbook" in items:
##        print_pause("The HR folks are busy at their desks.")
##        print_pause("There doesn't seem to be much to do here.")
##    else:
##        print_pause("The head of HR greets you.")
##        if "ID card" in items:
##            print_pause("He looks at your ID card and then "
##                        "gives you a copy of the employee handbook.")
##            items.append("handbook")
##        else:
##            print_pause("He has something for you, but says he can't "
##                        "give it to you until you go get your ID card.")
##    print_pause("You head back to the elevator.")
##    ride_elevator(items)
##
##
##def third_floor(items):
##    print_pause("You push the button for the third floor.")
##    print_pause("After a few moments, you find yourself "
##                "in the engineering department.")
##    print_pause("This is where you work!")
##    if "ID card" in items:
##        print_pause("You use your ID card to open the door.")
##        print_pause("Your program manager greets you and tells "
##                    "you that you need to have a copy of the "
##                    "employee handbook in order to start work.")
##        if "handbook" in items:
##            print_pause("Fortunately, you got that from HR!")
##            print_pause("Congratulatons! You are ready to start your new job "
##                        "as vice president of engineering!")
##        else:
##            print_pause("They scowl when they see that you don't have it, "
##                        "and send you back to the elevator.")
##            ride_elevator(items)
##    else:
##        print_pause("Unfortunately, the door is locked "
##                    "and you can't get in.")
##        print_pause("It looks like you need some kind of "
##                    "key card to open the door.")
##        print_pause("You head back to the elevator.")
##        ride_elevator(items)
##
##
##def ride_elevator(items):
##    print_pause("Please enter the number for the "
##                "floor you would like to visit:")
##    floor = input("1. Lobby\n"
##                  "2. Human resources\n"
##                  "3. Engineering department\n")
##    if floor == '1':
##        first_floor(items)
##    elif floor == '2':
##        second_floor(items)
##    elif floor == '3':
##        third_floor(items)
##
##
##def play_game():
##    items = []
##    intro()
##    ride_elevator(items)
##
##
##play_game()
