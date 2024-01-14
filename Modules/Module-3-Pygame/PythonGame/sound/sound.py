import pygame as pg
from pathlib import Path

parent_path = Path(__file__).parent


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.theme = pg.mixer.music.load(parent_path / 'run.mp3')
        pg.mixer.music.set_volume(0.4)
        pg.mixer.music.play(-1)