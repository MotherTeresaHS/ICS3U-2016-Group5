# Created by: Paul and Rehan
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the options scene

from scene import *
from main_menu_scene import *
import ui
import sound

class OptionsScene(Scene):
    def setup(self):
        # constants
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2

        # add background
        background_position = Vector2(self.screen_center_x, 
                                      self.screen_center_y)
        self.background = SpriteNode('./assets/sprites/background.JPG',
                                       parent = self,
                                       position = background_position,
                                       size = self.size)

        # back button
        back_button_position = self.size
        back_button_position.x = 100
        back_button_position.y = back_button_position.y - 100
        self.back_button = SpriteNode('./assets/sprites/left.PNG',
                                       parent = self,
                                       position = back_button_position,
                                       scale = 0.1)

        # sound options label
        sound_options_label_position = Vector2()
        sound_options_label_position.x = self.screen_center_x
        sound_options_label_position.y = self.screen_center_y * 1.3
        self.sound_options_label = LabelNode(text = 'Sound Options:',
                                      font = ('Avenir Next Condensed', 100),
                                      parent = self,
                                      position = sound_options_label_position,)

        # on button
        on_button_position = Vector2()
        on_button_position.x = self.screen_center_x
        on_button_position.y = self.screen_center_y
        self.on_button = SpriteNode('./assets/sprites/on.PNG',
                                       parent = self,
                                       position = on_button_position,
                                       scale = 0.1)

        # off button
        off_button_position = Vector2()
        off_button_position.x = self.screen_center_x
        off_button_position.y = self.screen_center_y * 0.7
        self.off_button = SpriteNode('./assets/sprites/off.PNG',
                                       parent = self,
                                       position = off_button_position,
                                       scale = 0.1)

    def touch_began(self, touch):
        # creating a pop effect when a button(s) is clicked

        # back button
        if self.back_button.frame.contains_point(touch.location):
            self.back_button.scale = 0.09

        # on button
        if self.on_button.frame.contains_point(touch.location):
            self.on_button.scale = 0.09

        # off button
        if self.off_button.frame.contains_point(touch.location):
            self.off_button.scale = 0.09

    def touch_ended(self, touch):
        # if the back button is pressed, go to the main menu scene
        if self.back_button.frame.contains_point(touch.location):
            self.back_button.scale = 0.1
            sound.play_effect('./assets/sounds/click.wav')
            self.dismiss_modal_scene()

        # on button for sound
        if self.on_button.frame.contains_point(touch.location):
            self.on_button.scale = 0.1
            sound.play_effect('./assets/sounds/click.wav')
            sound.set_volume(100)

        # off button for sound
        if self.off_button.frame.contains_point(touch.location):
            self.off_button.scale = 0.1
            sound.set_volume(0)
