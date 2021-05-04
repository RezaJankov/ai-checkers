import pygame
from .settings import BLACK, ROWS, SQUARE_SIZE, GREY


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.grey_player = self.white_player = 12
        self.grey_kings = self.white_kings = 0
        self.create_board()
    
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, GREY, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def create_board(self):
        pass
