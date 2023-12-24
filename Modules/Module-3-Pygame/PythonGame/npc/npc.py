
import pygame as pg
import math
from settings import *


class NPC():
    def __init__(self, game, pos, color):
        self.x, self.y = pos
        self.color = color
        self.game = game
        self.player = game.player
        self.theta = 0

    @property
    def map_pos(self):
        return int(self.x), int(self.y)

    def draw(self):
        pg.draw.circle(self.game.screen, self.color,
                       (100 * self.x, 100 * self.y), 15)
        pg.draw.line(self.game.screen, self.color, (self.x * 100 - 14.5 * math.sin(self.theta), self.y * 100 + 14.5 * math.cos(self.theta)),
                     (self.x * 100 + 35 * math.cos(self.theta),
                     self.y * 100 + 35 * math.sin(self.theta)), 2)
        pg.draw.line(self.game.screen, self.color, (self.x * 100 + 14.5 * math.sin(self.theta), self.y * 100 - 14.5 * math.cos(self.theta)),
                     (self.x * 100 + 35 * math.cos(self.theta),
                     self.y * 100 + 35 * math.sin(self.theta)), 2)

    def look(self):
        dx = self.player.x - self.x
        dy = self.player.y - self.y
        self.theta = math.atan2(dy, dx)



    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def ray_cast_player_npc(self):
        if self.game.player.map_pos == self.map_pos:
            return True

        wall_dist_v, wall_dist_h = 0, 0
        player_dist_v, player_dist_h = 0, 0

        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        ray_angle = math.pi + self.theta

        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)

        # horizontals
        y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

        depth_hor = (y_hor - oy) / sin_a
        x_hor = ox + depth_hor * cos_a

        delta_depth = dy / sin_a
        dx = delta_depth * cos_a

        for i in range(MAX_DEPTH):
            tile_hor = int(x_hor), int(y_hor)
            if tile_hor == self.map_pos:
                player_dist_h = depth_hor
                break
            if tile_hor in self.game.map.world_map:
                wall_dist_h = depth_hor
                break
            x_hor += dx
            y_hor += dy
            depth_hor += delta_depth

        # verticals
        x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

        depth_vert = (x_vert - ox) / cos_a
        y_vert = oy + depth_vert * sin_a

        delta_depth = dx / cos_a
        dy = delta_depth * sin_a

        for _ in range(MAX_DEPTH):
            tile_vert = int(x_vert), int(y_vert)
            if tile_vert == self.map_pos:
                player_dist_v = depth_vert
                break
            if tile_vert in self.game.map.world_map:
                wall_dist_v = depth_vert
                break
            x_vert += dx
            y_vert += dy
            depth_vert += delta_depth

        player_dist = max(player_dist_v, player_dist_h)
        wall_dist = max(wall_dist_v, wall_dist_h)

        if 0 < player_dist < wall_dist or not wall_dist:
            return True
        return False

    def logic(self):
        pass

    def update(self):
        self.look()
        self.logic()
