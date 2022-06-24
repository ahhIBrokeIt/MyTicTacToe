###################################
# -- This script is designed to run in Python 3.8 --
#  Tic Tac Toe : Main py file
#  module dependencies: random  - (for NPC choice)
#                       pygame  - (GUI of game)
#                       TicTacToeBoard - (object for game)
#
###################################

import random
import pygame
import TicTacToeBoard

# Define some colors in RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
aGREEN = (160, 255, 160)
RED = (255, 0, 0)

# Set the height and width of the screen
canvasSize = 400
size = [canvasSize, canvasSize]


# define N x N grid size
cellsPerRow = 4

# define board parameters
margin = int(canvasSize * 0.125)
cellSize = int((canvasSize - 2 * margin)/cellsPerRow)


def isPointInBox(xPos, yPos, width, height, x, y):
    '''check is (x,y) point is in/on specified box'''
    if (xPos <= x and x <= xPos + width) and (yPos <= y and y <= yPos + height):
        return True
    return False


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


def message_display(text, x, y):
    TextSurf, TextRect = text_objects(text, posFont)
    TextRect.center = (x, y)
    screen.blit(TextSurf, TextRect)


def DrawBoard(board):
    """Render the current state of the game board"""
    for i in range(1, board.size):
        src_x = board.margin + i * board.cellSize
        src_y = board.margin
        tar_x = board.margin + i * board.cellSize
        tar_y = canvasSize - board.margin
        pygame.draw.line(screen, BLACK, (src_x, src_y), (tar_x, tar_y), 3)
        src_y = board.margin + board.cellSize * i
        src_x = board.margin
        tar_y = board.margin + board.cellSize * i
        tar_x = canvasSize - board.margin
        pygame.draw.line(screen, BLACK, (src_x, src_y), (tar_x, tar_y), 3)

    for row in range(board.size):
        for col in range(board.size):
            if board.board[row][col] != '-':
                xPos = int(board.margin + (row + 0.5) * board.cellSize)
                yPos = board.margin + (col + 0.5) * board.cellSize
                message_display(board.board[row][col], xPos, yPos)


def DrawWinLine(board):

    if board.state[0] == 'R':
        src_x = board.margin
        src_y = board.margin + (board.state[-1] + 0.5) * board.cellSize
        tar_x = canvasSize - board.margin
        tar_y = board.margin + (board.state[-1] + 0.5) * board.cellSize

    if board.state[0] == 'C':
        src_x = board.margin + (board.state[-1] + 0.5) * board.cellSize
        src_y = board.margin
        tar_x = board.margin + (board.state[-1] + 0.5) * board.cellSize
        tar_y = canvasSize - board.margin

    if board.state[0] == 'D':
        src_x = board.margin
        src_y = board.margin
        tar_x = canvasSize - board.margin
        tar_y = canvasSize - board.margin

    if board.state[0] == 'RD':
        src_x = canvasSize - board.margin
        src_y = board.margin
        tar_x = board.margin
        tar_y = canvasSize - board.margin

    # print(board.state[0], board.state[-1], (src_x, src_y), (tar_x, tar_y))
    pygame.draw.line(screen, BLUE, (src_x, src_y), (tar_x, tar_y), 6)


def Pnt2Cell(mx, my, board):
    '''identify which cell (if any) mouse cursor is located in'''
    for row in range(board.size):
        for col in range(board.size):
            xPos = int(board.margin + row * board.cellSize)
            yPos = board.margin + col * board.cellSize
            if isPointInBox(xPos, yPos, board.cellSize, board.cellSize, mx, my):
                return (row, col)

    # if nothing came up ==> return None
    return (None, None)


def DrawPossibleSelection(mx, my, board):
    """draw square for possible cell selection"""
    for row in range(board.size):
        for col in range(board.size):
            xPos = int(board.margin + row * board.cellSize)
            yPos = board.margin + col * board.cellSize
            if isPointInBox(xPos, yPos, board.cellSize, board.cellSize, mx, my) and board.board[row][col] == '-':
                pygame.draw.rect(screen, aGREEN, (xPos, yPos,
                                 board.cellSize, board.cellSize))


def ComputerPlayerMove(board):
    ''''''
    if not board.boardIsFull():
        findSelection = False
        while findSelection == False:
            XChoice = random.randint(0, gameBoard.size - 1)
            YChoice = random.randint(0, gameBoard.size - 1)
            if not gameBoard.CellInUse(XChoice, YChoice):
                findSelection = True

        board.insertVal(XChoice, YChoice, 'O')
    else:
        pass


# main
if __name__ == "__main__":

    gameBoard = TicTacToeBoard.TTTBoard(cellsPerRow, cellSize, margin)

    # Initialize the pygame object
    pygame.init()

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Tic Tac Toe")

    pygame.font.init()
    posFont = pygame.font.SysFont('Arial', 48)

    inProcess = False

    clock = pygame.time.Clock()
    # Loop until the user clicks the close button.
    # enter main game loop
    gameOver, done = False, False
    while not done:

        # Limit the while loop to a max of 60 times per second.
        clock.tick(60)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

        # Clear the screen and set the screen background
        screen.fill(WHITE)

        if (pygame.mouse.get_focused() == True):  # check if mouse is focused on window
            pygame.event.get()
            buttons = pygame.mouse.get_pressed()  # get state of mouse buttons

            # initial LMB press
            if buttons[0] == True and inProcess == False and gameBoard.player == 'X' and not gameOver:
                inProcess = True
                mx, my = pygame.mouse.get_pos()
                rowCell, colCell = Pnt2Cell(mx, my, gameBoard)
                if not rowCell == None and not gameBoard.CellInUse(rowCell, colCell):
                    gameBoard.insertVal(rowCell, colCell, 'X')
                    gameBoard.player = 'O'

            if (buttons[0] == True and inProcess == True):  # process LMB action
                mx, my = pygame.mouse.get_pos()

            if (buttons[1] == True):
                print("centerMB pressed")

            if (buttons[2] == True and inProcess == False):
                inProcess = True

            # buttons released
            if buttons[0] == False and buttons[2] == False and inProcess == True:
                inProcess = False

            # buttons up and no process occuring
            if buttons[0] == False and buttons[2] == False and inProcess == False and not gameOver:
                mx, my = pygame.mouse.get_pos()
                # message_display(str(mx)+' '+str(my), 250, 30)
                DrawPossibleSelection(mx, my, gameBoard)

        if gameBoard.isThisAWin() == True:
            gameOver = True

        if gameBoard.player == 'O' and not gameOver:
            ComputerPlayerMove(gameBoard)
            gameBoard.player = 'X'

        if gameBoard.isThisAWin() == True:
            gameOver = True

        DrawBoard(gameBoard)

        # did anyone win?
        if gameBoard.isThisAWin() == True:
            gameOver = True
            DrawWinLine(gameBoard)
            if gameBoard.state[1] == 'X':
                message_display('Player Wins!', 150, 30)
            else:
                message_display('Computer Wins!', 200, 30)

        # is it really over?
        if gameBoard.boardIsFull() and gameBoard.isThisAWin() == False:
            gameOver = True
            message_display('Tie Game!', 150, 30)

        # update display
        pygame.display.flip()

    # Be IDLE friendly
    pygame.quit()
    pygame.font.quit()
