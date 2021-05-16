import pygame
from .settings import BLACK, ROWS, SQUARE_SIZE, GREY, WHITE, COLS
from .player import Player

class Board:
    def __init__(self):
        self.board = []
        self.grey_player = self.white_player = 8
        self.grey_kings = self.white_kings = 0
        self.create_board()
    
    def evaluate(self):
        return self.white_player - self.grey_player + (self.white_kings * 0.5 - self.grey_kings * 0.5)

    def get_all_players(self, color):
        players = []
        for row in self.board:
            for player in row:
                if player != 0 and player.color == color:
                    players.append(player)
        return players
    
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

    def get_player(self, row, col):
        return self.board[row][col]
    
    def move(self, player, row, col):
        self.board[player.row][player.col], self.board[row][col] = self.board[row][col], self.board[player.row][player.col]
        player.move(row, col)
        if row == ROWS - 1 or row == 0:
            player.make_king()
            if player.color == WHITE:
                self.white_kings += 1
            else:
                self.grey_kings += 1 

    def get_valid_moves(self, player):
        moves = {}
        left = player.col - 1
        right = player.col + 1
        row = player.row
        if player.color == GREY or player.king:
            moves.update(self._shift_left(row -1, max(row-3, -1), -1, player.color, left))
            moves.update(self._shift_right(row -1, max(row-3, -1), -1, player.color, right))
        if player.color == WHITE or player.king:
            moves.update(self._shift_left(row +1, min(row+3, ROWS), 1, player.color, left))
            moves.update(self._shift_right(row +1, min(row+3, ROWS), 1, player.color, right))
        return moves
    
    def _shift_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._shift_left(r+step, row, step, color, left-1,skipped=last))
                    moves.update(self._shift_right(r+step, row, step, color, left+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            left -= 1
        return moves

    def _shift_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r, right)] = last
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._shift_left(r+step, row, step, color, right-1,skipped=last))
                    moves.update(self._shift_right(r+step, row, step, color, right+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            right += 1  
        return moves

    def remove(self, players):
        for player in players:
            self.board[player.row][player.col] = 0
            if player != 0:
                if player.color == GREY:
                    self.grey_player -= 1
                else:
                    self.white_player -= 1

    def winner(self):
        if self.grey_player <= 0:
            return WHITE
        elif self.white_player <= 0:
            return GREY
        return None 
