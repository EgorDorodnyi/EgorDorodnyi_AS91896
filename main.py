# pygame is a extra program that adds fetures and makes making pyton games a lot easier
import pygame
from Setting import *
from Sprite import *


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((Width, Height))
        pygame.display.set_caption(Title)
        self.clock = pygame.time.Clock()

    def new(self):
        self.board = Board()
        self.board.display_board()

    def run(self):
        self.clock.tick(FPS)
        self.events()
        self.draw()

    def draw(self):
        self.screen.fill(BGcolor)
        self.board.draw(self.screen)
        pygame.display.flip()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            if event == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                mx //= Tile_size
                my //= Tile_size

                if event.button == 1:
                    if not self.board.board_list[mx][my].falgged:
                        # revels(digs) tile and checks if it is a bomb and sees if it explodes
                        pass

                if event.button == 3:
                    if not self.board.board_list[mx][my].revealed:
                        self.board.board_list[mx][my].falgged = not self.board.board_list[mx][my].falgged
            



game = Game()
game.new()
while True: 
    game.run() 




