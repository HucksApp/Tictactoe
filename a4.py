# NOTE: Until you fill in the TTTBoard class mypy is going
# to give you multiple errors talking about unimplemented
# class attributes, don't worry about this as you're working


class TTTBoard:

    """A tic tac toe board

    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X',
        'O's represent moves by player 'O' and '*'s are spots no one has yet
        played on
    """
    # initial state of the board
    def __init__(self):
        self.board =['*','*','*','*','*','*','*','*','*']


    # the user Interface
    def __str__(self):

        return(
            "----------\n" + "|"+  self.board[0] + "  " + self.board[1]  + "  " + self.board[2] + " " + "|\n" + "|--+--+--|\n" + "|"+ self.board[3] + "  "  + self.board[4]  + "  " + self.board[5] + " " + "|\n" + "|--+--+--|\n" + "|"+ self.board[6]  + "  " + self.board[7]  + "  " + self.board[8] + " " + "|\n" + "----------"
        )
        

    def make_move(self, player, pos):
        if int(pos) > 8 or int(pos) < 0 or self.board[int(pos)] != "*":
            return False
        else:
            self.board[pos] = player
            return True

    def find_positions(self,player):
        index_pos= []
       
        
    
        for index in range (len(self.board)):
            if self.board[index] == player:
                index_pos.append(index)
            
        print(index_pos)
        return index_pos


    
    def has_won(self, player): 
        played_positions = self.find_positions(player)
        print('here')
        #print(played_positions)
        if len(played_positions) >= 3:
            
            if played_positions[0] == 0 :
                if played_positions[1] == 1:

                    if played_positions[2] == 2:
                        return True
                    else :
                        return False

                elif played_positions[1] == 3:

                    if played_positions[2] == 6:
                        return True
                    else :
                        return False
                    
                
                elif played_positions[1] == 4 :
                    if played_positions[2] == 8:
                        return True
                    else :
                        return False
            elif played_positions[0] == 1:
                if played_positions[1] == 4:

                    if played_positions[2] == 6:
                        return True
                    else :
                        return False
                else:
                    return False

            elif played_positions[0] == 2:
                if played_positions[1] == 4:

                    if played_positions[2] == 6:
                        return True
                    else :
                        return False
                elif played_positions[1] == 5:
                    if played_positions[2] == 8:
                        return True
                    else :
                        return False
                
            elif played_positions[0] == 3:
                if played_positions[1] == 4:

                    if played_positions[2] == 5:
                        return True
                    else :
                        return False
                else:
                    return False
            
            elif played_positions[0] == 6:
                if played_positions[1] == 7:
                    print('here 1')

                    if played_positions[2] and played_positions[2] == 8:
                        
                        return True
                    else :
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
                    
    
    def game_over(self):
        if self.has_won("X") or self.has_won("O") or self.board.index("*") == -1 :
            return True
        else:
            return False

    
    def clear(self):
        self.board = ['*','*','*','*','*','*','*','*','*'] 







def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""

    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise

        Args:
            maybe_int - string to check if it's an int

        Returns:
            True if maybe_int is an int, False otherwise
        """
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False

    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")

        if not is_int(move):
            raise ValueError(
                f"Given invalid position {move}, "
                "position must be integer between 0 and 8 inclusive"
            )

        if brd.make_move(players[turn], int(move)):
            turn = not turn

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, that's game!")


if __name__ == "__main__":
    # here are some tests. These are not at all exhaustive tests. You will
    # DEFINITELY need to write some more tests to make sure that your TTTBoard class
    # is behaving properly.
    brd = TTTBoard()
    brd.make_move("X", 8)
    brd.make_move("O", 7)

    assert brd.game_over() == False

    brd.make_move("X", 5)
    brd.make_move("O", 6)
    brd.make_move("X", 2)
    print(brd.__str__())
    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over() == True

    brd.clear()

    assert brd.game_over() == False

    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)

    assert brd.has_won("X") == False
    assert brd.has_won("O") == True
    assert brd.game_over() == True

    print("All tests passed!")

    # uncomment to play!
    # play_tic_tac_toe()
