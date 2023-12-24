import pygame as pg
import math
from settings import *

class Bullet():
    def __init__(self, game, pos, color, speed, theta):
        #! npc
        self.x, self.y = pos
        self.game = game
        self.color = color
        self.theta = theta
        self.speed = speed
        self.strike = False
        
    def kill(self):
        len_to_player = ((self.game.player.x - self.x) ** 2 + (self.game.player.y - self.y) ** 2)
        if len_to_player < BULLET_KILL_LEN:
            self.strike = True

    def move(self):
        #! runner
        dx = math.cos(self.theta) * self.speed * self.game.delta_time
        dy = math.sin(self.theta) * self.speed * self.game.delta_time
        self.check_wall_collision(dx, dy)

    def draw(self):
        #! npc
        pg.draw.circle(self.game.screen, self.color,
                       (100 * self.x, 100 * self.y),  5)

    def check_wall(self, x, y):
        if (x, y) not in self.game.map.world_map:
            return True
        else:
            self.strike = True
            return False

    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy
            
    def update(self):
        self.move()
        self.kill()
