import random
#Guessing Words
# words = ["inheritance", "objects", "classes", "lists", "dictionary", "sets"]
# limits = 5
# word = random.choice(words)
# count  = 0
# while count < limits:
#     guess = input("Enter any term in python to get the guessed word?\n").lower()
#     if guess == word:
#         print("You had the correct word")
#         break
#     elif guess != word:
#         print("Not right")
#     else:
#          print("You Loose")
        
#     count += 1

min_num = int(input('Enter the minimum number for the guess game\n'))
max_num = int(input('Enter the maximum number for the guess game\n'))
guess = random.randint(min_num, max_num)
while True:
    guessed_num = int(input(f"Enter the number between {min_num} and {max_num}?\n"))
    if guessed_num > max_num or guessed_num < min_num:
        print("Error")
    elif guessed_num > guess :
        print('You number is high')
    elif guessed_num <  guess:
        print("You number is lower")
    else:
        print("You guessed correct. You won")
        break
