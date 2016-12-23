# Created by: Paul and Rehan
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the options scene.

from scene import *
from main_menu_scene import *
import ui
import sound

class OptionsScene(Scene):
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

        # sound options label
        sound_options_label_position = Vector2()
        sound_options_label_position.x = 384
        sound_options_label_position.y = 662
        self.sound_options_label = LabelNode(text = 'Sound Options:',
                                      font=('Avenir Next Condensed', 100),
                                      parent = self,
                                      position = sound_options_label_position,)

        # on button
        on_button_position = Vector2()
        on_button_position.x = 384
        on_button_position.y = 512
        self.on_button = SpriteNode('./assets/sprites/on.PNG',
                                       parent = self,
                                       position = on_button_position,
                                       scale = 0.1)

        # off button
        off_button_position = Vector2()
        off_button_position.x = 384
        off_button_position.y = 362
        self.off_button = SpriteNode('./assets/sprites/off.PNG',
                                       parent = self,
                                       position = off_button_position,
                                       scale = 0.1)

    def update(self):
        # this method is called, hopefully, 60 times a second
        pass

    def touch_began(self, touch):
        # this method is called, when user touches the screen

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

        # on button for sound
        if self.on_button.frame.contains_point(touch.location):
            self.on_button.scale = 0.1
            sound.play_effect('./assets/sounds/click.wav')
            sound.set_volume(100)

        # off button for sound
        if self.off_button.frame.contains_point(touch.location):
            self.off_button.scale = 0.1
            sound.set_volume(0)

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
