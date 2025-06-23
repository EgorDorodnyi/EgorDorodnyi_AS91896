#Importing files and information
import pygame
from Setting import *

# Type guide
# X = mine
# / = empty
# ? = unknown
# C = clue



class Tile:
    def __init__(self, x, y, image, type, revealed=False, flagged=False):
        self.x, self.y = x * Tile_size, y * Tile_size
        self.image = image
        self.type = type
        self.revealed = revealed
        self.falgged = flagged


    def draw(self, board_surface):    
        board_surface.blit(Tile_unknown, (self.x, self.y))

    def __repr__(self):
        return self.type


class Board:
    def __init__(self):
        self.board_top = pygame.Surface((Width, Height))
        self.board_list = [[Tile(col, Row, Tile_empty, "?") for Row in range(Rows)] for col in range(Columns)]


    def draw(self, screen):
         for row in self.board_list:
              for tile in row:
                   tile.draw(self.board_top)
         screen.blit(self.board_surface, (0, 0))





    def display_board(self):
            for row in self.board_list:
                 print(row)