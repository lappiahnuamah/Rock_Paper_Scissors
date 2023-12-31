#!/usr/bin/env python3
import random


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0
        self.opponent_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.opponent_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def learn(self, my_move, their_move):
        super().learn(my_move, their_move)


class HumanPlayer(Player):
    def move(self):
        my_move = input("Rock, paper, scissors? >").lower()
        while my_move not in ['rock', 'paper', 'scissors']:
            print("Invalid move. Please choose 'rock', 'paper' or 'scissors'.")
            my_move = input("Rock, paper, scissors? >").lower()
        return my_move

    def learn(self, my_move, their_move):
        return super().learn(my_move, their_move)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class ReflectPlayer(Player):
    def move(self):
        if self.opponent_move:
            return self.opponent_move
        else:
            #  if no opponent move is recorded, play randomly
            return random.choice(['rock', 'paper', 'scissors'])


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.last_move = None

    def move(self):
        if self.last_move == 'rock':
            self.last_move = 'paper'
        elif self.last_move == 'paper':
            self.last_move = 'scissors'
        else:
            self.last_move = 'rock'
        return self.last_move

    def learn(self, my_move, their_move):
        return super().learn(my_move, their_move)


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.round = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}  \n Opponent played {move2}")
        if beats(move1, move2):
            print("** PLAYER ONE WINS **")
            self.p1.score += 1
        elif beats(move2, move1):
            print("** PLAYER TWO WINS **")
            self.p2.score += 1
        else:
            print("** TIE **")
        self.round += 1
        self.display_scores()
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def display_scores(self):
        print(f"Scores: Player One:{self.p1.score},",
              "Player Two: {self.p2.score}\n")

    def play_game(self):
        print("Game start!\n")
        print("Rock Paper Scissors, Go!\n")

        while True:
            print(f"Round {self.round + 1} --")
            self.play_round()
            play_again = input("Play another round? (yes/no) ").lower()
            if play_again != 'yes':
                break
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
