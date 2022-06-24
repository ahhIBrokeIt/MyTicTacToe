###################################
# -- This script is designed to run in Python 3.8 --
#  Tic Tac Toe Voard object class
#
###################################


class TTTBoard():
    '''-- Tic-Tac-Toe Board Object --
       object class to handle game state

       instances:
            board : holds value for each cell
             size : row x col = size x size for board
            state : tuple for winning/ending game state
                    (win Type, winning player, placement of win)

                            win type : 'R' row, 'C' col, 'D' diagonal, 'RD' reverse diagonal
                      winning player : 'X', 'O', 'C' (cat's game)
                    placement of win : row/col/corner value
    '''

    def __init__(self, size, cellSize, margin):

        self.board = [size * ['-'] for _ in range(size)]
        self.size = size
        self.state = None
        self.player = 'X'

    def boardIsFull(self):
        '''check if board is full'''
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == '-':
                    return False
        return True

    def CellInUse(self, row, col):
        '''check if selected cell is possible to play'''
        if self.board[row][col] == '-':
            return False
        return True

    def insertVal(self, row, col, value):
        '''update cell with new value'''
        self.board[row][col] = value

    def isThisAWin(self):
        '''Check all possible ways to win'''
        # check for a row win
        onRow = 0
        for col in range(self.size):
            result = ''
            for row in range(self.size):
                result += self.board[row][col]

            if result in ['X' * self.size, 'O' * self.size]:
                self.state = ('R', result[0], onRow)
                return True
            onRow += 1

        # check for a column win
        onCol = 0
        for row in range(self.size):
            result = ''
            for col in range(self.size):
                result += self.board[row][col]

            if result in ['X' * self.size, 'O' * self.size]:
                self.state = ('C', result[0], onCol)
                return True
            onCol += 1

        # check diagonal
        result = ''
        for n in range(self.size):
            result += self.board[n][n]

        if result in ['X' * self.size, 'O' * self.size]:
            self.state = ('D', self.board[0][0], 0)
            return True

        # check reverse diagonal
        result = ''
        for n in range(self.size):
            result += self.board[self.size - n - 1][n]

        if result in ['X' * self.size, 'O' * self.size]:
            self.state = ('RD', self.board[0][-1], 0)
            return True

        return False
