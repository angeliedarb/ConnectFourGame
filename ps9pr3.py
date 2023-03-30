#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
   
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b
      
        
def process_move(p, b):
    """ takes two parameters: a Player object p for the player whose move is
        being processed, and a Board object b for the board on which the game
        is being played.
    """
    
    print (repr(p) + "'s" + " Turn")
        
    next_m = p.next_move(b)
    if repr(p) == 'Player X':
        m = 'X'
    else:
        m = 'O'
    b.add_checker(m, next_m)
    print()
    print(b)
   
    if b.is_win_for(m) == True:
        print (repr(p), ' wins in', p.num_moves, 'moves')
        print('Congratulations!')
        return True 
    elif b.is_win_for(m) == False :
        print ("It's a tie!")
        return True
    else:
        
        return False 

#subclass of class Player
class RandomPlayer(Player):
    """ can be used for an unintelligent computer player that chooses at
        random from the available columns
    """
    
    def next_move(self, b):
        a = []
        for col in range(b.width):
            if b.can_add_to(col) == True:
                a += [col]       
        result = random.choice(a) 
        return result
        
           
        
        
        
        
        
        
        
        
    