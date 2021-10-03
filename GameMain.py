import pygame as p
import tkinter as tk
import time
import GameEngine


p.init()

WIDTH = 512
HEIGHT = 512
DIMENSION = 3
scene = 1

sqSize = WIDTH // DIMENSION
OFFSET = int(0.125 * sqSize)
running = True
maxFPS = 15

whoWins = ''

def drawGameState(screen, gs):

    if scene == 1:

        screen.fill((238,238,210))
        screen.blit(Board, (0, 0))

        for row in range(3):
            for col in range(3):
                if gs.board[row][col] == 'X':
                    screen.blit(X, (row * sqSize + OFFSET, col * sqSize + OFFSET))
                elif gs.board[row][col] == 'O':
                    screen.blit(O, (row * sqSize + OFFSET, col * sqSize + OFFSET))


        whoWins = gs.checkWin(gs.board)[0]
        whereWin = gs.checkWin(gs.board)[1]
        
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
            
        if whoWins != '-':

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


X = p.transform.scale(p.image.load(r"D:\Programming\Python\Projects\Pygame\TicTakToe\Images\X.png"), (sqSize - (OFFSET * 2), sqSize - (OFFSET * 2)))
O = p.transform.scale(p.image.load(r"D:\Programming\Python\Projects\Pygame\TicTakToe\Images\O.png"), (sqSize - (OFFSET * 2), sqSize - (OFFSET * 2)))

DiagonalLine1 = p.transform.scale(p.image.load(
    r"D:\Programming\Python\Projects\Pygame\TicTakToe\Images\DiagonalLine1.png"), (sqSize * 3, sqSize * 3))
DiagonalLine2 = p.transform.scale(p.image.load(
    r"D:\Programming\Python\Projects\Pygame\TicTakToe\Images\DiagonalLine2.png"), (sqSize * 3, sqSize * 3))
HorizontalLine = p.transform.scale(p.image.load(
    r"D:\Programming\Python\Projects\Pygame\TicTakToe\Images\HorizontalLine.png"), (sqSize * 2, sqSize * 3))
VerticalLine = p.transform.scale(p.image.load(
    r"D:\Programming\Python\Projects\Pygame\TicTakToe\Images\VerticalLine.png"), (sqSize * 3, sqSize * 2))

PlayButton = p.transform.scale(p.image.load(
    r"D:\Programming\Python\Projects\Pygame\TicTakToe\Images\Play2.png"), (sqSize - (OFFSET * 2), sqSize - (OFFSET * 2)))
QuitButton = p.transform.scale(p.image.load(
    r"D:\Programming\Python\Projects\Pygame\TicTakToe\Images\Quit.png"), (sqSize - (OFFSET * 2), sqSize - (OFFSET * 2)))

Confetti = p.transform.scale(p.image.load(
    r"D:\Programming\Python\Projects\Pygame\TicTakToe\Images\Confetti.gif"), (sqSize * 3, sqSize * 3))

Board = p.transform.scale(p.image.load(
    r"D:\Programming\Python\Projects\Pygame\TicTakToe\Images\Board.png"), (sqSize * 3, sqSize * 3))

#   LOOP STARTS HERE



root = tk.Tk()
root.title('Tic Tac Toe')

tk.Label(root, text='Tic Tac Toe', font=('arial', 20, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)


def game():
    root.destroy()
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

tk.Button(root, text='Play ►', font=('arial', 20, 'bold'), command=game).grid(row=1, column=0, ipadx=10, ipady=20)
tk.Button(root, text='Exit |←', font=('arial', 20, 'bold'), command=root.destroy).grid(row=1, column=1, ipadx=10, ipady=20)

tk.Label(root, text='by Tanish M').grid(row=2, column=1, pady=5, sticky='e')

tk.mainloop()
