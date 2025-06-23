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
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)



game = Game()
game.new() 
game.run() 


pygame.quit()
quit(0)
