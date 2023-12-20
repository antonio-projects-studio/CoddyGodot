from npc import *

class NpcControl:
    def __init__(self, game):
        self.game = game
        self.npc_list = []
        #! создаем список позиций npc
        self.npc_positions = set()
        self.add_npc()
        
    def add_npc(self):
        self.npc_list.append(NPC(game=self.game, pos=(11.5, 7.5), color='blue'))
        self.npc_list.append(NPC(game=self.game, pos=(6.5, 7.5), color='yellow'))
        self.npc_list.append(NPC(game=self.game, pos=(9.5, 1.5), color='green'))
        self.npc_list.append(NPC(game=self.game, pos=(13, 3)))
    
    def update(self):
        for npc in self.npc_list:
            npc.update()
        
        self.npc_positions.clear()
        for npc in self.npc_list:
            self.npc_positions.add(npc.map_pos)
    
    def draw(self):
        for npc in self.npc_list:
            npc.draw()