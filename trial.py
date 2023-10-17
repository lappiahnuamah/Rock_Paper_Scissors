#!/usr/bin/env python3
import random

class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class RandomPlayer(Player):
    def move(self):
        return random.choice(['rock', 'paper', 'scissors'])

class HumanPlayer(Player):
    def move(self):
        my_move = input("Rock, paper, scissors? >").lower()
        while my_move not in ['rock', 'paper', 'scissors']:
            print("Invalid move. Please choose 'rock', 'paper', or 'scissors'.")
            my_move = input("Rock, paper, scissors? >").lower()
        return my_move

class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.their_move = None

    def move(self):
        if self.their_move:
            return self.their_move
        else:
            return random.choice(['rock', 'paper', 'scissors'])

    def learn(self, my_move, their_move):
        self.their_move = their_move

class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.my_move = None

    def move(self):
        if self.my_move == 'rock':
            self.my_move = 'paper'
        elif self.my_move == 'paper':
            self.my_move = 'scissors'
        else:
            self.my_move = 'rock'
        return self.my_move

    def learn(self, my_move, their_move):
        self.my_move = my_move

class AllRockPlayer(Player):
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

class Game:
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}  \nOpponent played {move2}")

        if move1 == move2:
            print("** TIE **")
        elif beats(move1, move2):
            print("** PLAYER ONE WINS **")
            self.p1_score += 1
        else:
            print("** PLAYER TWO WINS **")
            self.p2_score += 1

        print("Current scores:")
        print(f"Player 1: {self.p1_score}")
        print(f"Player 2: {self.p2_score}")

    def play_game(self, num_rounds):
        print("Game start!\n")
        print("Rock Paper Scissors, Go!\n")

        for _ in range(num_rounds):
            print(f"Round {self.p1_score + self.p2_score + 1} --")
            self.play_round()

        print("Game over!")
        print("General scores:")
        print(f"Player 1: {self.p1_score}")
        print(f"Player 2: {self.p2_score}")

if __name__ == '__main__':
    opponents = [
        AllRockPlayer(),
        RandomPlayer(),
        ReflectPlayer(),
        CyclePlayer(),
        HumanPlayer()
    ]
    print("Player list:")
    for index, opponent in enumerate(opponents):
        print(f"{index}. {opponent.__class__.__name__}")

    p1_choice = int(input("Choose player 1: "))
    p2_choice = int(input("Choose player 2: "))

    p1 = opponents[p1_choice]
    p2 = opponents[p2_choice]

    num_rounds = int(input("Enter the number of rounds: "))

    game = Game(p1, p2)
    game.play_game(num_rounds)