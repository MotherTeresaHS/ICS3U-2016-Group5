# Created by: Paul and Rehan
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the game logo screen for 2 seconds, then transitions to the main menu

from scene import *
from main_menu_scene import *
import ui
import time

class GameLogoScene(Scene):
    def setup(self):
        # create timer, so that after 2 seconds move to next scene
        self.start_time = time.time()

        # add white background
        self.background = SpriteNode(position = self.size/2, 
                                     color = 'white', 
                                     parent = self, 
                                     size = self.size)

        # game logo
        self.game_logo = SpriteNode('./assets/sprites/game_logo.PNG',
                                       parent = self,
                                       position = self.size/2,
                                       scale = 0.5)

    def update(self):
        # after 2 seconds, move to main menu scene
        if not self.presented_scene and time.time() - self.start_time > 2:
            self.present_modal_scene(MainMenuScene())
