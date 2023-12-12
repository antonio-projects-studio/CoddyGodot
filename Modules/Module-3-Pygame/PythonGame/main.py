import pygame as pg
import sys
from settings import *
from map import *
from player import *
from npc import *
#! Импортируем pathfinding
from path_finding import *


class Game:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode(size=RES)
        self.clock = pg.time.Clock()
        self.new_game()

    def new_game(self):
        self.delta_time = self.clock.tick(framerate=FPS)
        self.map = Map(game=self)
        self.player = Player(game=self)
        self.npc = NPC(game=self, pos=(8, 5))
        #! Добавляем переменную, которую будем использовать для поиска путей
        self.path_finding = PathFinding(game=self)

    def update(self):
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        self.player.update()
        self.npc.update()

    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()
        self.npc.draw()

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_event()
            self.draw()
            self.update()


if __name__ == '__main__':
    game = Game()
    game.run()
