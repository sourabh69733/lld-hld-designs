import random

# Implement tic-tac-toe game in python
'''
Higher level components
- Board class which is nothing but implemented using matri of n x n
    - This need to have methods to play
    - get player whose turn function
    - move and check if somebody is winning
    - as it is only 2 player game, so we need to first choose between
    players
    - then maintain state of game 
    - restart game
    - winner reward
- Tournament class
    - which can take multiple board and 2-3 levels for playing game
    
'''

class Player():
    def __init__(self, username):
        self.username = username
    
    def getName(self):
        return self.username
        
    
class Board():
    def __init__(self, n, player1: Player, player2: Player, is_auto_play_enabled: bool):
        if n < 3:
            raise Exception('n must be greater than or equal to 3')

        self.n = n
        self.player1 = input(f'Hi, {player1.getName()}: Please Choose X or O\n')
        if self.player1 == 'X':
            self.player2 = 'O'
        else:
            self.player2 = 'X'
        
        self.players = {
            self.player1: player1.getName(),
            self.player2: player2.getName(),
        }
        
        # internal state matrix
        self.board = []
        for i in range(self.n):
            temp = []
            for j in range(self.n):
                temp.append('_')
            self.board.append(temp)
        
        self.available_moves = {}
        for row in range(self.n):
            for col in range(self.n):
                key = str(row + 1) + ', ' + str(col + 1)
                self.available_moves[key] = None
        
        self.current_player = self.player1
        self.is_auto_play_enabled = is_auto_play_enabled
        
    def __str__(self):
        # column and row printing
        for row in range(self.n):
            col = 0
            while col < self.n:
                print(self.board[row][col], " ", end=" ")
                col += 1
            print('\n')
        return ''
    
    def getAndUpdatePlayer(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
        return self.current_player

    def move(self, row, col):
        row = int(row) -  1
        col = int(col) - 1
        
        self.board[row][col] = self.current_player
        
        def isDiagonalMatch():
            i, j = 0, 0
            
            win = True
            while i < self.n and j < self.n:
                if self.board[i][j] != self.current_player:
                    win = False
                    break
                i += 1
                j += 1
            
            if not win:
                i, j = self.n - 1, 0
                while i > 0 and j < self.n:
                    if self.board[i][j] != self.current_player:
                        win = False
                        break
                    i -= 1
                    j += 1
                    
            return win
        
        def isColumnMatch():
            i, j = 0, col
            
            win = True
            
            while i < self.n:
                if self.board[i][j] != self.current_player:
                    win = False
                    break
                i += 1
                
            return win
            
        def isRowMatch():
            i, j = row, 0
            
            win = True
            while j < self.n:
                if self.board[i][j] != self.current_player:
                    win = False
                    break
                j += 1
                
            return win
        
        if isColumnMatch() or isDiagonalMatch() or isRowMatch():
            return "win"
        return "next"
    
    def startPlay(self):
        def play():
            print('-' * 50)
            print(self.__str__())
            counter = 1
            counter_to_key = {}
            for key in self.available_moves:
                if self.available_moves[key] == None:
                    print(f"{counter}. {key}", end= "\n")
                    counter_to_key[str(counter)] = key
                    counter += 1
            if counter == 1:
                return 'draw'
            
            if self.is_auto_play_enabled:
                move1 = random.choice(list(counter_to_key.keys()))
            else:
                move1 = input(f'Player {self.current_player}: Please tell which position you want to move\n')
            
            if not move1 in counter_to_key:
                raise Exception('Invalid move')
            if not counter_to_key[move1] in self.available_moves or self.available_moves[counter_to_key[move1]] != None:
                raise Exception('You have choosen wrong move')
            
            [row, col] = counter_to_key[move1].split(', ')
            
            self.available_moves[counter_to_key[move1]] = True
            
            move_status = self.move(row, col)
            
            print(self.__str__())
            
            if move_status == "win":
                print(f'Congrats {self.players[self.current_player]} {self.current_player}')
                return "break"
            
            self.getAndUpdatePlayer()
            
            return "next"
            
        while True:
            move1_status = play()
            if move1_status == "break" or move1_status == "draw":
                break
            
            move2_status = play()
            if move2_status == "break" or move2_status == "draw":
                break
            
    # we need to some kind of system that enables to play
    
board_size = int(input('Please enter the board  size\n'))
is_auto_play_enabled = input('Please enter is auto play is enabled or not: yes or no\n')
if is_auto_play_enabled == 'yes':
    is_auto_play_enabled = True
else:
    is_auto_play_enabled = False
    
player1 = Player('hardik')
player2 = Player('sourabh')

board = Board(board_size, player1, player2, is_auto_play_enabled)

board.startPlay()