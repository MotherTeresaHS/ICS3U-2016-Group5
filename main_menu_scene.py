# Created by: Paul and Rehan
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the main menu scene.

from scene import *
from help_scene import *
from options_scene import *
from game_scene import *
import ui
import sound

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene

        # add background
        self.background = SpriteNode('./assets/sprites/background.JPG',
                                       parent = self,
                                       position = self.size/2,
                                       scale = 1)

        # title (game logo)
        title_position = Vector2()
        title_position.x = 384
        title_position.y = 800
        self.title = SpriteNode('./assets/sprites/game_logo.PNG',
                                      parent = self,
                                      position = title_position,
                                      scale = 0.4)

        # help button
        help_button_position = Vector2()
        help_button_position.x = 384
        help_button_position.y = 305
        self.help_button = SpriteNode('./assets/sprites/help.PNG',
                                      parent = self,
                                      position = help_button_position,
                                      scale = 0.5)

        # options button
        options_button_position = Vector2()
        options_button_position.x = 384
        options_button_position.y = 105
        self.options_button = SpriteNode('./assets/sprites/options.PNG',
                                      parent = self,
                                      position = options_button_position,
                                      scale = 0.5)

        # start button
        start_button_position = Vector2()
        start_button_position.x = 384
        start_button_position.y = 505
        self.start_button = SpriteNode('./assets/sprites/start.PNG',
                                       parent = self,
                                       position = start_button_position,
                                       scale = 0.5)

    def update(self):
        # this method is called, hopefully, 60 times a second
        pass

    def touch_began(self, touch):
        # this method is called, when user touches the screen

        # creating a pop effect when a button(s) is clicked

        # back button
        if self.options_button.frame.contains_point(touch.location):
            self.options_button.scale = 0.45

        # help button
        if self.help_button.frame.contains_point(touch.location):
            self.help_button.scale = 0.45

        # start button
        if self.start_button.frame.contains_point(touch.location):
            self.start_button.scale = 0.45

    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass

    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen

        # if the options button is pressed, go to the options scene
        if self.options_button.frame.contains_point(touch.location):
            self.options_button.scale = 0.5
            sound.play_effect('./assets/sounds/click.wav')
            self.present_modal_scene(OptionsScene())

        # if the help button is pressed, go to the help scene
        if self.help_button.frame.contains_point(touch.location):
            self.help_button.scale = 0.5
            sound.play_effect('./assets/sounds/click.wav')
            self.present_modal_scene(HelpScene())

        # if the start button is pressed, go to the game scene
        if self.start_button.frame.contains_point(touch.location):
            self.start_button.scale = 0.5
            sound.play_effect('./assets/sounds/click.wav')
            self.present_modal_scene(GameScene())

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
