from .npc import *
from .runner import *
from .shooter import *


class NpcControl:
    def __init__(self, game):
        self.game = game
        self.npc_list = []
        self.npc_positions = set()
        self.add_npc()

    def add_npc(self):
        self.npc_list = [
            Runner(game=self.game, pos=(11.5, 7.5), color='blue'),
            Shooter(game=self.game, pos=(6.5, 7.5), color='yellow', ttl=100, bullet_cnt=5),
            Shooter(game=self.game, pos=(8, 3), ttl=250)
        ]

    def update(self):
        for npc in self.npc_list:
            npc.update()

        self.npc_positions.clear()
        for npc in self.npc_list:
            self.npc_positions.add(npc.map_pos)

    def draw(self):
        for npc in self.npc_list:
            npc.draw()
