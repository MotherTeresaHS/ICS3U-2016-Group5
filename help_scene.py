
# Created by: Paul and Rehan
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the help scene.

from scene import *
from main_menu_scene import *
import ui
import sound

class HelpScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        center_of_screen = self.size/2

        # add background
        self.background = SpriteNode('./assets/sprites/background.JPG',
                                       parent = self,
                                       position = self.size/2,
                                       scale = 1)

        # back button
        back_button_position = Vector2()
        back_button_position.x = 100
        back_button_position.y = 924
        self.back_button = SpriteNode('./assets/sprites/left.PNG',
                                       parent = self,
                                       position = back_button_position,
                                       scale = 0.1)

        # how to play label
        how_to_play_label_position = Vector2()
        how_to_play_label_position.x = 384
        how_to_play_label_position.y = 800
        self.how_to_play_label = LabelNode(text = 'How To Play:',
                                      font=('Avenir Next Condensed', 100),
                                      parent = self,
                                      position = how_to_play_label_position,)

        # controls label
        controls_label_position = Vector2()
        controls_label_position.x = 384
        controls_label_position.y = 400
        self.controls_label = LabelNode(text = 'Controls:',
                                      font=('Avenir Next Condensed', 100),
                                      parent = self,
                                      position = controls_label_position,)

        # rules
        rules_position = Vector2()
        rules_position.x = 384
        rules_position.y = 600
        self.rules = SpriteNode('./assets/sprites/rules.PNG',
                                      parent = self,
                                      position = rules_position,
                                      scale = 0.65)

        # controls
        controls1_position = Vector2()
        controls1_position.x = 384
        controls1_position.y = 300
        self.controls1 = SpriteNode('./assets/sprites/controls1.PNG',
                                      parent = self,
                                      position = controls1_position,
                                      scale = 0.275)

        controls2_position = Vector2()
        controls2_position.x = 384
        controls2_position.y = 200
        self.controls2 = SpriteNode('./assets/sprites/controls2.PNG',
                                      parent = self,
                                      position = controls2_position,
                                      scale = 0.275)

        controls3_position = Vector2()
        controls3_position.x = 384
        controls3_position.y = 100
        self.controls3 = SpriteNode('./assets/sprites/controls3.PNG',
                                      parent = self,
                                      position = controls3_position,
                                      scale = 0.275)

        # credits label
        credits_label_position = Vector2()
        credits_label_position.x = 384
        credits_label_position.y = 28
        self.credits_label = LabelNode(text = 'Hockey Shootout was created by Paul Barasa and Rehan Fernando. Special thanks to qubodup, NenadSimic, David McKee, and Erik Streb!',
                                      font=('Avenir Next Condensed', 15),
                                      parent = self,
                                      position = credits_label_position,)

    def update(self):
        # this method is called, hopefully, 60 times a second
        pass

    def touch_began(self, touch):
        # this method is called, when user touches the screen

        # creating a pop effect when a button(s) is clicked

        # back button
        if self.back_button.frame.contains_point(touch.location):
            self.back_button.scale = 0.09

    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass

    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen

        # if the back button is pressed, go to the main menu scene
        if self.back_button.frame.contains_point(touch.location):
            self.back_button.scale = 0.1
            sound.play_effect('./assets/sounds/click.wav')
            self.dismiss_modal_scene()

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
