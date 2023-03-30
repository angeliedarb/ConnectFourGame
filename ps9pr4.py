#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """ In particular, this “AI player” will look ahead some number of moves into 
        the future to assess the impact of each possible move that it could make for 
        its next move, and it will assign a score to each possible move. And since 
        each move corresponds to a column number, it will effectively assign a score
        to each column.
    """
    
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object """
        
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
      
    def __repr__(self):
        """ returns a string representing an AIPlayer object"""
        s = 'Player '
        m = self.tiebreak
        q = self.lookahead
        result = (s + self.checker + ' (' +str(m) + ', ' + str(q) + ')')
        return result
    
    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the board, 
            and that returns the index of the column with the maximum score.
        """
        m = []
        for score in range(len(scores)):
            if scores[score] == max(scores):
                m += [score]
                
        if self.tiebreak == 'LEFT':
            return m[0]
        elif self.tiebreak == 'RIGHT':
            return m[-1]
        else:
            return random.choice(m)
        
    def scores_for(self, b):
        """ takes a Board object b and determines the called AIPlayer‘s 
            scores for the columns in b
        """
        scores = [50] * b.width
        
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker)== True:
                scores[col] = 100
            elif b.is_win_for(Player.opponent_checker(self)) == True:
                scores[col] = 0 
            elif self.lookahead == 0:
                scores[col] = 50
            else: 
                b.add_checker(self.checker,col)
                opp_scores = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead -1).scores_for(b)
                scores[col] = 100 - max(opp_scores) 
                b.remove_checker(col)
               
        return scores
        
        
    def next_move(self, b):
        """ Rather than asking the user for the next move, this version of
            next_move should return the called AIPlayer‘s judgment of its
            best possible move.
        """
        
        next_m = self.scores_for(b)
        return self.max_score_column(next_m)
                
        
        
        
        
        