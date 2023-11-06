from enum import Enum
import random


class Move(Enum):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'

    @classmethod
    def moves(cls):
        """ Returns a list of all available moves. """
        return [e.value for e in cls]


# Define ANSI escape codes for text colors
RED = "\033[91m"
DARK_RED = "\033[31m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"


class Player:
    def __init__(self):
        self.my_move = None
        self.their_move = None

    def move(self):
        pass

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class AllRockPlayer(Player):
    def move(self):
        return Move.ROCK.value


class RandomPlayer(Player):
    def move(self):
        return random.choice(Move.moves())


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(Move.moves())
        return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(Move.moves())
        index = Move.moves().index(self.my_move)
        return Move.moves()[(index + 1) % len(Move.moves())]


class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input("Enter your move (rock/paper/scissors): ").lower()
            if choice in Move.moves():
                return choice
            else:
                print("Invalid move. Please try again.")


def beats(one, two):
    return ((one == Move.ROCK.value and two == Move.SCISSORS.value) or
            (one == Move.SCISSORS.value and two == Move.PAPER.value) or
            (one == Move.PAPER.value and two == Move.ROCK.value))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def display_accumulated_score(self):
        p1, p2 = self.p1_score, self.p2_score
        print(f"Accumulated Score: Player 1 - {p1}, Player 2 - {p2}")

    def play_round(self, round):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"{BLUE}Round {round + 1}:")
        print(f"{RESET}Player 1: {GREEN}{move1}{RESET}")
        print(f"{RESET}Player 2:{RED}{move2}{RESET}")
        if beats(move1, move2):
            print(f"{GREEN}Player 1 wins this round!{RESET}")
            self.p1_score += 1
        elif beats(move2, move1):
            print(f"{RED}Player 2 wins this round!{RESET}")
            self.p2_score += 1
        else:
            print(f"{YELLOW}It's a tie!{RESET}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.display_accumulated_score()

    def play_game(self):
        print('Game start!')
        for round in range(3):
            self.play_round(round)
            self.display_accumulated_score()
            if round < 2:
                input("Press Any key to start the next round...")

        if self.p1_score > self.p2_score:
            print(f"{GREEN}Player 1 wins the game!{RESET}")
        elif self.p2_score > self.p1_score:
            print(f"{RED}Player 2 wins the game!{RESET}")
        else:
            print(f"{YELLOW}It's a tie!{RESET}")

        self.restart_game()  # Properly indented as a method

    def restart_game(self):
        while True:
            choice = input("Do you want to play a new game? (yes/no)").lower()
            if choice in ('yes', 'y'):
                self.p1_score = 0
                self.p2_score = 0
                self.play_game()
                break
            elif choice in ('no', 'n'):
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no.'")


if __name__ == '__main__':
    opponents = {
        '1': AllRockPlayer,
        '2': RandomPlayer,
        '3': ReflectPlayer,
        '4': CyclePlayer,
        '5': HumanPlayer
    }
    print("Player list:")
    for key, value in opponents.items():
        print(f"{key}. {value.__name__}")

    while True:
        p1_choice = input("Choose player 1: ")
        p2_choice = input("Choose player 2: ")
        if p1_choice in opponents and p2_choice in opponents:
            p1 = opponents[p1_choice]
            p2 = opponents[p2_choice]
            game = Game(p1(), p2())
            game.play_game()
            break
        else:
            print("Invalid choice. Please enter valid player numbers.")
