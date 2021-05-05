import pygame
from .settings import GREY, BLACK, WHITE
from .board import Board

class Game:
  def __init__(self, win):
    self.reset_game()
    self.win = win
  
  def update(self):
    self.board.draw(self.win)
    pygame.display.update()
  
  def reset_game(self):
    self.selected = None
    self.board = Board()
    self.turn = GREY
    self.valid_moves = {}

  def select_crof(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        player = self.board.get_player(row, col)
        if player != 0 and player.color == self.turn:
            self.selected = player
            self.valid_moves = self.board.get_valid_moves(player)
            return True
        else:
          return False

  def _move_player(self, row, col):
        player = self.board.get_player(row, col)
        if self.selected and player == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True
  
  def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)


  def change_turn(self):
        self.valid_moves = {}
        if self.turn == GREY:
            self.turn = WHITE
        else:
            self.turn = GREY
  


  