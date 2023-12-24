from ..npc import *
from .bullet import *
import pygame as pg


class Shooter(NPC):
    def __init__(self, game, pos, color=DEFAULT_COLOR, ttl=TTL, bullet_cnt=BULLET_CNT, bullet_speed=BULLET_SPEED):
        super().__init__(game=game, pos=pos, color=color)
        self.bullet_cnt = bullet_cnt
        self.bullet_params = [game, pos, color, bullet_speed]
        self.bullets = []

        self.timer_activate = False
        self.ttl = ttl
        self.time = pg.time.get_ticks() - ttl

    def logic(self):
        self.ray_cast_value = self.ray_cast_player_npc()
        if self.ray_cast_value == True:
            self.fire()

    @property
    def timer(self):
        if self.time + self.delay <= pg.time.get_ticks():
            self.time = pg.time.get_ticks()
            return True
        else:
            return False

    @timer.setter
    def timer(self, delay):
        self.delay = delay

    def toggle_timer(self):
        if self.timer_activate:
            self.timer = 0
        else:
            self.timer = self.ttl

        self.timer_activate = not self.timer_activate

    def fire(self):
        if len(self.bullets) < self.bullet_cnt:
            if not self.timer_activate:
                self.toggle_timer()
            if self.timer:
                self.bullets.append(
                    Bullet(*self.bullet_params, theta=self.theta))
        else:
            if self.timer_activate:
                self.toggle_timer()

    def draw(self):
        super().draw()
        for bullet in self.bullets:
            bullet.draw()

    def update(self):
        super().update()

        bullets = []

        for bullet in self.bullets:
            bullet.update()
            if not bullet.strike:
                bullets.append(bullet)

        self.bullets = bullets
