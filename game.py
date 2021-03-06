import pygame
import json

from snake import Snake
from food import Food
from utils.settings import game_settings


class Game:

    def __init__(self, game_width, game_height, mode_file):
        pygame.display.set_caption('SnakeGen')
        self.game_width = game_width
        self.game_height = game_height

        if game_settings['display_option']:
            self.gameDisplay = pygame.display.set_mode((game_width, game_height+60))
            self.bg = pygame.image.load("./game_modes/img/background.png")
            self.barrierImage = pygame.image.load("game_modes/img/barrier.png")

        self.crash = False
        self.player = Snake(self)
        self.food = Food()
        self.score = 0
        self.barrierPositions = []

        if mode_file != '':
            with open(mode_file, 'r') as coordinates:
                self.barrierPositions = json.load(coordinates)
