import pygame
import time

from sudoku-1 import is_valid, solve_sudoku

def draw_grid():
    for i in range(0,10):
        if i % 3 == 0:
            pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i, 500), 4)
            pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4)
        else:
             pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i, 500), 1)
             pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 1)

def draw_numbers(board):
    font = pygame.font.Font(None, 50)
    for i in range(0,9):
        for j in range(0,9):
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), True, (0,0,0))
                win.blit(text, (65 + 50*j, 60 + 50*i))

# Pygame setup
pygame.init()
win = pygame.display.set_mode((550,550))
pygame.display.set_caption("Sudoku Solver")

# Game loop
board = [[...]]
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((255,255,255))

    draw_grid()
    draw_numbers(board)
    pygame.display.flip()

    # Uncomment this line to solve the board automatically after a delay
    # time.sleep(3); solve_sudoku(board)

pygame.quit()