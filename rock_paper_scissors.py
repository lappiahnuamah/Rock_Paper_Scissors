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
        my_move = input("Rock, paper, scissors? > ").lower()
        while my_move not in ['rock', 'paper', 'scissors']:
            print("Invalid move. Please choose 'rock', 'paper', or 'scissors'.")
            my_move = input("Rock, paper, scissors? > ").lower()
        return my_move

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.round = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2):
            print("Player 1 wins!")
            self.p1.score += 1
        elif beats(move2, move1):
            print("Player 2 wins!")
            self.p2.score += 1
        else:
            print("It's a tie!")

        self.round += 1
        self.display_scores()

    def display_scores(self):
        print(f"Scores - Player 1: {self.p1.score}, Player 2: {self.p2.score}")

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
        self.display_scores()

if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()

# In this updated version, the `display_scores` method is called at the end of each round to display the scores, ensuring they are updated and shown after each round of the game.