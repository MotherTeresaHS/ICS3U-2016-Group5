# Created by: Paul and Rehan
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the help scene

from scene import *
from main_menu_scene import *
import ui
import sound

class HelpScene(Scene):
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

        # how to play label
        how_to_play_label_position = Vector2()
        how_to_play_label_position.x = self.screen_center_x
        how_to_play_label_position.y = self.screen_center_y * 1.59
        self.how_to_play_label = LabelNode(text = 'How To Play:',
                                      font = ('Avenir Next Condensed', 100),
                                      parent = self,
                                      position = how_to_play_label_position)

        # the rules
        rules_position = Vector2()
        rules_position.x = self.screen_center_x
        rules_position.y = self.screen_center_y * 1.19
        self.rules = SpriteNode('./assets/sprites/rules.PNG',
                                      parent = self,
                                      position = rules_position,
                                      scale = 0.65)

        # controls label
        controls_label_position = Vector2()
        controls_label_position.x = self.screen_center_x
        controls_label_position.y = self.screen_center_y * 0.79
        self.controls_label = LabelNode(text = 'Controls:',
                                      font = ('Avenir Next Condensed', 100),
                                      parent = self,
                                      position = controls_label_position)

        # controls
        controls1_position = Vector2()
        controls1_position.x = self.screen_center_x
        controls1_position.y = self.screen_center_y * 0.59
        self.controls1 = SpriteNode('./assets/sprites/controls1.PNG',
                                      parent = self,
                                      position = controls1_position,
                                      scale = 0.275)

        controls2_position = Vector2()
        controls2_position.x = self.screen_center_x
        controls2_position.y = self.screen_center_y * 0.39
        self.controls2 = SpriteNode('./assets/sprites/controls2.PNG',
                                      parent = self,
                                      position = controls2_position,
                                      scale = 0.275)

        controls3_position = Vector2()
        controls3_position.x = self.screen_center_x
        controls3_position.y = self.screen_center_y * 0.19
        self.controls3 = SpriteNode('./assets/sprites/controls3.PNG',
                                      parent = self,
                                      position = controls3_position,
                                      scale = 0.275)

        # credits label
        credits_label_position = Vector2()
        credits_label_position.x = self.screen_center_x
        credits_label_position.y = self.screen_center_y * 0.035
        self.credits_label = LabelNode(text = 'Hockey Shootout was created by Paul Barasa and Rehan Fernando. Special thanks to qubodup, NenadSimic, David McKee, and Erik Streb!',
                                      font = ('Avenir Next Condensed', 15),
                                      parent = self,
                                      position = credits_label_position)

    def touch_began(self, touch):
        # creating a pop effect when a button(s) is clicked

        # back button
        if self.back_button.frame.contains_point(touch.location):
            self.back_button.scale = 0.09

    def touch_ended(self, touch):
        # if the back button is pressed, go to the main menu scene
        if self.back_button.frame.contains_point(touch.location):
            self.back_button.scale = 0.1
            sound.play_effect('./assets/sounds/click.wav')
            self.dismiss_modal_scene()
