'''
    Things to do
    
    main menu
        Graphic part done
    
    play agaain
    
    

'''

import pygame as p
import time
import GameEngine


p.init()

WIDTH = 512
HEIGHT = 512
DIMENSION = 3

sqSize = WIDTH // DIMENSION
OFFSET = int(0.125 * sqSize)
running = True
maxFPS = 15

scene = 0
gameOver = False

whoWins = ''
whereWin = ''

def drawGameState(screen, gs):

    if scene == 1:

        screen.blit(Board, (0, 0))

        for row in range(3):
            for col in range(3):
                if gs.board[row][col] == 'X':
                    screen.blit(X, (row * sqSize + OFFSET, col * sqSize + OFFSET))
                elif gs.board[row][col] == 'O':
                    screen.blit(O, (row * sqSize + OFFSET, col * sqSize + OFFSET))


        whoWins = gs.checkWin(gs.board)[0]
        whereWin = gs.checkWin(gs.board)[1]

        #Test drawing


        '''
            NOTE
            HORIZONTAL and  VERTICAL are interchanged
        '''
        if whoWins != '-':
            if whereWin == '1':
                screen.blit(HorizontalLine, (sqSize * 0 + OFFSET * 3,0))
                print("Horizontal 1")
            elif whereWin == '2':
                screen.blit(HorizontalLine, (sqSize * 1 + OFFSET * 3,0))
                print("Horizontal 2")
            elif whereWin == '3':
                screen.blit(HorizontalLine, (sqSize * 2 + OFFSET * 3,0))
                print("Horizontal 3")
            elif whereWin == '4':
                screen.blit(VerticalLine, (1, sqSize * 0 + OFFSET * 3))
                print("vertical 1")
            elif whereWin == '5':
                screen.blit(VerticalLine, (1, sqSize * 1 + OFFSET * 3))
                print("Vertical 2")
            elif whereWin == '6':
                screen.blit(VerticalLine, (1, sqSize * 3 + OFFSET * 3))
                print("Vertical 3")
            elif whereWin == '7':
                screen.blit(DiagonalLine2, (0, 0))
                print("Diagonal 2")
            elif whereWin == '8':
                screen.blit(DiagonalLine1, (0, 0))
            
        '''
        if whoWins == 'X':
            screen.fill((238,238,210))
            screen.blit(resultMessageX, (sqSize - OFFSET , sqSize + OFFSET * 2))
        elif whoWins == 'O':
            screen.fill((238,238,210))
            screen.blit(resultMessageO, (sqSize - OFFSET, sqSize + OFFSET * 2))
        elif whoWins == 'D':
            screen.fill((238,238,210))
            screen.blit(resultMessageDraw, (sqSize - OFFSET, sqSize + OFFSET * 2))
        '''
    elif scene == 0:
        screen.fill((238, 238, 210))
        screen.blit(menuTitleText, (sqSize // 2 - OFFSET, OFFSET * 2 ))
        screen.blit(PlayButton, (sqSize + OFFSET - sqSize // 2, sqSize + OFFSET))
        screen.blit(QuitButton, (sqSize + OFFSET + sqSize // 2, sqSize + OFFSET))
        



p.init()
screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("Tic Tac Toe by Tanish M.")

resultMessageFont = p.font.SysFont(None, 100) 
menuFont = p.font.Font(r'D:\Programming\Python\IDLE\TicTakToe\Font\PermanentMarker-Regular.ttf', 72)

menuTitleText = menuFont.render('TicTacToe', True, (0, 15, 155))

resultMessageX = resultMessageFont.render('X Wins', True,  (66, 245, 230))
resultMessageO = resultMessageFont.render('O Wins', True,  (255, 0, 0))
resultMessageDraw = resultMessageFont.render('Draw', True,  (0, 0, 0))
clock = p.time.Clock()
screen.fill((238,238,210))

gs = GameEngine.GameState()

running = True
xToMove = True


X = p.transform.scale(p.image.load(r"D:\Programming\Python\IDLE\TicTakToe\Images\X.png"), (sqSize - (OFFSET * 2), sqSize - (OFFSET * 2)))
O = p.transform.scale(p.image.load(r"D:\Programming\Python\IDLE\TicTakToe\Images\O.png"), (sqSize - (OFFSET * 2), sqSize - (OFFSET * 2)))

DiagonalLine1 = p.transform.scale(p.image.load(r"D:\Programming\Python\IDLE\TicTakToe\Images\DiagonalLine1.png"), (sqSize * 3, sqSize * 3))
DiagonalLine2 = p.transform.scale(p.image.load(r"D:\Programming\Python\IDLE\TicTakToe\Images\DiagonalLine2.png"), (sqSize * 3, sqSize * 3))
HorizontalLine = p.transform.scale(p.image.load(r"D:\Programming\Python\IDLE\TicTakToe\Images\HorizontalLine.png"), (sqSize * 2, sqSize * 3))
VerticalLine = p.transform.scale(p.image.load(r"D:\Programming\Python\IDLE\TicTakToe\Images\VerticalLine.png"), (sqSize * 3, sqSize * 2))

PlayButton = p.transform.scale(p.image.load(r"D:\Programming\Python\IDLE\TicTakToe\Images\Play.png"), (sqSize - (OFFSET * 2), sqSize - (OFFSET * 2)))
QuitButton = p.transform.scale(p.image.load(r"D:\Programming\Python\IDLE\TicTakToe\Images\Quit.png"), (sqSize - (OFFSET * 2), sqSize - (OFFSET * 2)))

Board = p.transform.scale(p.image.load(r"D:\Programming\Python\IDLE\TicTakToe\Images\Board.png"), (sqSize * 3, sqSize * 3))

#   LOOP STARTS HERE
while running:
    for event in p.event.get():
        #drawGameState(screen, gs)
        if event.type == p.QUIT:
            p.quit()
        elif event.type == p.MOUSEBUTTONDOWN:
            if gameOver == False:
                location = p.mouse.get_pos()
                col = location[1] // sqSize
                row = location[0] // sqSize

                gs.Move(row, col)
            elif gameOver == True:
                print("The game is over")
                location = p.mouse.get_pos()
                #this is a comment



    drawGameState(screen, gs)
    clock.tick(maxFPS)
    p.display.flip()






'''

    CODE REPOSITORY

V1.0
+++++++++++++

====================================================================================================
import pygame as p
import time
import GameEngine


p.init()

WIDTH = 512
HEIGHT = 512
DIMENSION = 3

sqSize = WIDTH // DIMENSION
OFFSET = int(0.125 * sqSize)
running = True
maxFPS = 15

whoWins = ''

def drawGameState(screen, gs):
    screen.blit(Board, (0, 0))
    #screen.blit(DiagonalLine1, (0, 0))

    #Display the X and O

    for row in range(3):
        for col in range(3):
            if gs.board[row][col] == 'X':
                screen.blit(X, (row * sqSize + OFFSET, col * sqSize + OFFSET))
            elif gs.board[row][col] == 'O':
                screen.blit(O, (row * sqSize + OFFSET, col * sqSize + OFFSET))


    whoWins = gs.checkWin(gs.board)

    if whoWins == 'X':
        screen.fill((238,238,210))
        screen.blit(resultMessageX, (sqSize - OFFSET , sqSize + OFFSET * 2))
    elif whoWins == 'O':
        screen.fill((238,238,210))
        screen.blit(resultMessageO, (sqSize - OFFSET, sqSize + OFFSET * 2))
    elif whoWins == 'D':
        screen.fill((238,238,210))
        screen.blit(resultMessageDraw, (sqSize - OFFSET, sqSize + OFFSET * 2))




p.init()
screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("Tic Tac Toe by Tanish M.")

resultMessageFont = p.font.SysFont(None, 100) 
resultMessageX = resultMessageFont.render('X Wins', False,  (66, 245, 230))
resultMessageO = resultMessageFont.render('O Wins', False,  (255, 0, 0))
resultMessageDraw = resultMessageFont.render('Draw', False,  (0, 0, 0))
clock = p.time.Clock()
screen.fill((238,238,210))

gs = GameEngine.GameState()

running = True
xToMove = True


X = p.transform.scale(p.image.load(r"D:\Programming\Python\IDLE\TicTakToe\Images\X.png"), (sqSize - (OFFSET * 2), sqSize - (OFFSET * 2)))
O = p.transform.scale(p.image.load(r"D:\Programming\Python\IDLE\TicTakToe\Images\O.png"), (sqSize - (OFFSET * 2), sqSize - (OFFSET * 2)))
DiagonalLine1 = p.transform.scale(p.image.load(r"D:\Programming\Python\IDLE\TicTakToe\Images\DiagonalLine1.png"), (sqSize * 3, sqSize * 3))
DiagonalLine2 = p.transform.scale(p.image.load(r"D:\Programming\Python\IDLE\TicTakToe\Images\DiagonalLine2.png"), (sqSize * 3, sqSize * 3))
HorizontalLine = p.transform.scale(p.image.load(r"D:\Programming\Python\IDLE\TicTakToe\Images\HorizontalLine.png"), (sqSize * 3, sqSize * 3))
VerticalLine = p.transform.scale(p.image.load(r"D:\Programming\Python\IDLE\TicTakToe\Images\VerticalLine.png"), (sqSize * 3, sqSize * 3))
Board = p.transform.scale(p.image.load(r"D:\Programming\Python\IDLE\TicTakToe\Images\Board.png"), (sqSize * 3, sqSize * 3))

#   LOOP STARTS HERE
while running:
    for event in p.event.get():
        #drawGameState(screen, gs)
        if event.type == p.QUIT:
            p.quit()
        elif event.type == p.MOUSEBUTTONDOWN:
            location = p.mouse.get_pos()
            col = location[1] // sqSize
            row = location[0] // sqSize

            gs.Move(row, col)
            



    drawGameState(screen, gs)
    clock.tick(maxFPS)
    p.display.flip()

==============================================================================================







'''