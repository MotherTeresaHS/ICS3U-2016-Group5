# Created by: Paul and Rehan
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the company logo scene for 2 seconds, then transitions to the game logo scene

from scene import *
from game_logo_scene import *
import ui
import time
import sound

class CompanyLogoScene(Scene):
    def setup(self):
        # loading sound
        sound.set_volume(100)
        sound.play_effect('./assets/sounds/loading.wav')

        # create timer, so that after 2 seconds move to next scene
        self.start_time = time.time()

        # add white background
        self.background = SpriteNode(position = self.size/2, 
                                     color = 'white', 
                                     parent = self, 
                                     size = self.size)

        # company logo
        self.company_logo = SpriteNode('./assets/sprites/company_logo.PNG',
                                       parent = self,
                                       position = self.size/2,
                                       scale = 0.5)

    def update(self):
        # after 2 seconds, move to game logo scene
        if not self.presented_scene and time.time() - self.start_time > 2:
            self.present_modal_scene(GameLogoScene())
