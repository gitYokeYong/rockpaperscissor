import random

moves = ['rock','paper','scissors']

class Player:
  def __init__(self):
      self.my.move = None
      self.their.move = None

  def move(self):
      return 'rock'
  
  def learn(self,my_move,their_move):
      self.my_move = my_move
      self.their_move = their_move

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)
    
class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move
    
class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        Index = moves.index(self.my_move)
        return moves[(index + 1) % len(moves)]
    
class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input("Enter your move(rock/paper/scissors):").lower
            if choice in moves:
                return choice
            else:
                 print("Invalid move.Please try again.")

def beats(one,two):
    return ((one == 'rock') or two == 'scissors' or
           (one == 'scissors' and two == 'paper') or
           (one == 'paper' and two == 'rock'))

class Game:
    def __init__(self,p1, p2): 
       self.p1 = p1
       self.p2 = p2
       self.p1_score = 0
       self.p2_score = 0
    
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print =(f"Player 1: {move1} Player 2:{move2}")
        if beats(move1,move2):
            print("Player 1 wins this round!")
            self.p1_score += 1
        elif beats(move2,move1):
            print("Player 2 wins this round!")
            self.p2_score +=1
        else:
            print("Player 2 wins this round!")

        self.p1.learn(move1, move2)
        self.p2.learn(move2,move1) 

    def play_game(self,rounds=3):
        print('Game start!')
        for round in range(rounds):
            print(f"Round{round+1}:")
            self.play_round()
            print(f"Score: Player 1 - {self.p1_score}, Player 2 - {self.p2_score}")
        print("Game over!")

    if __name__ =='_main_':
        player1 = HumanPlayer()
        player2 = RandomPlayer()
        game = Game(player1, player2)
        game.play_game()


             







        







      

