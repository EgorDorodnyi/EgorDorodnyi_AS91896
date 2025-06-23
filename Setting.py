import pygame
import os
#This is the coulers for the numbers: in RGB or (R, G, B)
White = (255, 255, 255)
Black = (0, 0 ,0)
Dark_grey = (48, 48, 48)
Light_grey = (100, 100, 100)
Green = (0 , 255, 0)
Dark_green = (0, 200, 0)
Red = (255, 0, 0)
Yellow = (255, 255, 0)
Blue = (0, 0, 255)
BGcolor = Dark_grey

#Game setting
#this will be used to modify the size, amount of mines and title of the game.
#you can change difficty by modifing the size of the colloum

#easy level:
# 9 by 9, 10 mines

#Intermedate level:
# 16 by 16, 40

Tile_size = 32
Rows = 10
Columns = 10
Amount_mines = 10
Width = Tile_size * Rows
Height = Tile_size * Columns
FPS = 60
Title = 'Minesweeper: By "Egor"'


Tile_num = []
for i in range(1, 9):
    Tile_num.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets", f"Tile{i}.jpg")), (Tile_size, Tile_size)))

Tile_empty = pygame.transform.scale(pygame.image.load(os.path.join("Assets", f"Empty tile.jpg")), (Tile_size, Tile_size))
Tile_boom = pygame.transform.scale(pygame.image.load(os.path.join("Assets", f"TileBomb.jpg")), (Tile_size, Tile_size))
Tile_not_bomb = pygame.transform.scale(pygame.image.load(os.path.join("Assets", f"TileNotBomb.jpg")), (Tile_size, Tile_size))
Tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("Assets", f"FlagTile.jpg")), (Tile_size, Tile_size))
Tile_mine = pygame.transform.scale(pygame.image.load(os.path.join("Assets", f"TileBomb.jpg")), (Tile_size, Tile_size))
Tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("Assets", f"TileUnknown.jpg")), (Tile_size, Tile_size))


