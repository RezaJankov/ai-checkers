import pygame
from .settings import BLACK, ROWS, SQUARE_SIZE, GREY, WHITE, COLS
from .player import Player


class Board:
    def __init__(self):
        self.board = []
        self.selected_player = None
        self.grey_player = self.white_player = 12
        self.grey_kings = self.white_kings = 0
        self.create_board()
    
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, WHITE, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    if row < 2:
                        self.board[row].append(Player(row, col, WHITE))
                    elif row > 5:
                        self.board[row].append(Player(row, col, GREY))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
    
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                player = self.board[row][col]
                if player != 0:
                    player.draw(win)
