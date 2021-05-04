import pygame
from game.settings import WIDTH, HEIGHT, SQUARE_SIZE, GREY, WHITE
from game.board import Board

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
  
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                player = board.get_player(row, col)
                board.move(player, 4, 3)
        
        board.draw(WIN)
        pygame.display.update()
    
    pygame.quit()

main()

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col