# Created by: Paul and Rehan
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the company logo scene for 2 seconds, then transitions to the game logo scene.

from scene import *
from game_logo_scene import *
import ui
import time
import sound

class CompanyLogoScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene

        # loading sound
        sound.set_volume(100)
        sound.play_effect('./assets/sounds/loading.wav')

        # create timer, so that after 2 seconds move to next scene
        self.start_time = time.time()

        # add white background
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'white', 
                                     parent = self, 
                                     size = self.size)

        # company logo
        self.company_logo = SpriteNode('./assets/sprites/company_logo.PNG',
                                       parent = self,
                                       position = self.size/2,
                                       scale = 0.5)

    def update(self):
        # this method is called, hopefully, 60 times a second

        # after 2 seconds, move to game logo scene
        if not self.presented_scene and time.time() - self.start_time > 2:
            self.present_modal_scene(GameLogoScene())

    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass

    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass

    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        pass

    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass

    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass

    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
