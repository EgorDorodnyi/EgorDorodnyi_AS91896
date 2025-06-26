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
#Explanation is down bellow, order of recomended diffictly goes: Rows by Columns and then by mines

# Tile size can be ajusted to be bigger or smaller, The one i set it at is 32pxs
# Format of setting is
# Rows = how much tiles you want in width
# Columns = how much times you want in length
# Amount mines = how much mines you want in the board.

#Beginer:
# 9 by 9, 10 mines

#Intermedate level:
# 16 by 16, 40 mines

#Insane level
# 30 by 16, 99 mines


Tile_size = 32
Rows = 9
Columns = 9
Amount_mines = 5

# !!!Dont touch these!!!
#they are used todetermin how the grid is made, as well it has the title ans fps cap
Width = Tile_size * Rows
Height = Tile_size * Columns
FPS = 60
Title = 'Minesweeper: By "Egor"'

#this saves A LOT of space sd it allows the code to easly place tile numberd and allows the genator to be a lot more compact and effecent

Tile_num = []
for i in range(1, 9):
    Tile_num.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets", f"Tile{i}.jpg")), (Tile_size, Tile_size)))


#these are the uniqe tiles that cant be made into a list, This grabs my assits and use pygame image load and transorm fucntion to upsacle
# or downslace the image
Tile_empty = pygame.transform.scale(pygame.image.load(os.path.join("Assets", f"Empty tile.jpg")), (Tile_size, Tile_size))
Tile_boom = pygame.transform.scale(pygame.image.load(os.path.join("Assets", f"TileBomb.jpg")), (Tile_size, Tile_size))
Tile_not_bomb = pygame.transform.scale(pygame.image.load(os.path.join("Assets", f"TileNotBomb.jpg")), (Tile_size, Tile_size))
Tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("Assets", f"FlagTile.jpg")), (Tile_size, Tile_size))
Tile_mine = pygame.transform.scale(pygame.image.load(os.path.join("Assets", f"TileBomb.jpg")), (Tile_size, Tile_size))
Tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("Assets", f"TileUnknown.jpg")), (Tile_size, Tile_size))


