# pygame is a extra program that adds fetures and makes making pyton games a lot easier
import pygame
from Setting import *
from Sprite import *

#we are know defling the game and making the window that the game will be played on

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((Width, Height))
        pygame.display.set_caption(Title)
        self.clock = pygame.time.Clock()
#We are taking the Board class form the Sprite.py that contains the genaration and how the board looks
    def new(self):
        self.board = Board()
        self.board.display_board()

#Here we are making the run functions so that it allows us to stop the game and make a tick cycle.
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
        else:
            self.end_screen()

#this is what males the background of the boared.
    def draw(self):
        self.screen.fill(BGcolor)
        self.board.draw(self.screen)
        pygame.display.flip()

#this is what is used to determin if all the mines have been flagged
    def check_win(self):
        for row in self.board.board_list:
            for tile in row:
                if tile.type != "X" and not tile.revealed:
                    return False
        return True



    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                mx //= Tile_size
                my //= Tile_size

                if event.button == 1:
                    if not self.board.board_list[mx][my].flagged:
                        # revels(digs) tile and checks if it is a bomb and sees if it explodes
                        if not self.board.dig(mx, my):
                            # Kaboom
                            for row in self.board.board_list:
                                for tile in row:
                                    if tile.flagged and tile.type != "X":
                                        tile.flagged = False
                                        tile.revealed = True
                                        tile.image = Tile_not_bomb
                                    elif tile.type == "X":
                                        tile.revealed = True
                            self.playing = False

                if event.button == 3:
                    if not self.board.board_list[mx][my].revealed:
                        self.board.board_list[mx][my].flagged = not self.board.board_list[mx][my].flagged

                if self.check_win():
                    self.win = True
                    self.playing = False
                    for row in self.board.board_list:
                        for tile in row:
                            if not tile.revealed:
                                tile.flagged = True 


    def end_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    return

game = Game()
while True: 
    game.new()
    game.run()




