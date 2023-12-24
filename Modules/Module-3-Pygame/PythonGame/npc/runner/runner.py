from ..npc import *


class Runner(NPC):
    def __init__(self, game, pos, color=DEFAULT_COLOR, speed=SPEED_NPC):
        super().__init__(game=game, pos=pos, color=color)
        self.speed = speed

    def move(self):
        next_pos = self.game.path_finding.get_path(
            self.map_pos, self.game.player.map_pos)
        next_x, next_y = next_pos

        angle = math.atan2(next_y + 0.5 - self.y, next_x + 0.5 - self.x)
        dx = math.cos(angle) * self.speed * self.game.delta_time
        dy = math.sin(angle) * self.speed * self.game.delta_time

        #! Добавляем проверку, что на следующей клетке никто не стоит
        if next_pos not in self.game.npc_control.npc_positions:
            self.check_wall_collision(dx, dy)

    def logic(self):
        self.ray_cast_value = self.ray_cast_player_npc()
        if self.ray_cast_value == True:
            self.move()
