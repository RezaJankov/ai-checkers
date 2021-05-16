from copy import deepcopy
from game.settings import GREY, WHITE
from game.board import Board
import pygame


def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, GREY, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        return minEval, best_move


def simulate_move(player, move, board, game, skip):
    board.move(player, move[0], move[1])
    if skip:
        board.remove(skip)
    return board

def draw_moves(game, board, player):
    valid_moves = board.get_valid_moves(player)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (player.x, player.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()

def get_all_moves(board, color, game):
    moves = []
    for player in board.get_all_players(color):
        valid_moves = board.get_valid_moves(player)
        for move, skip in valid_moves.items():
            draw_moves(game, board, player)
            temp_board = deepcopy(board)
            temp_player = temp_board.get_player(player.row, player.col)
            new_board = simulate_move(temp_player, move, temp_board, game, skip)
            moves.append(new_board)
    return moves

