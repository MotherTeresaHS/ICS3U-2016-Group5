# Created by: Paul and Rehan
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the main menu scene

from scene import *
from game_scene import *
from help_scene import *
from options_scene import *
import ui
import sound

class MainMenuScene(Scene):
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

        # title (game logo)
        title_position = Vector2()
        title_position.x = self.screen_center_x
        title_position.y = self.screen_center_y * 1.565
        self.title = SpriteNode('./assets/sprites/game_logo.PNG',
                                      parent = self,
                                      position = title_position,
                                      scale = 0.4)

        # start button
        start_button_position = Vector2()
        start_button_position.x = self.screen_center_x
        start_button_position.y = self.screen_center_y
        self.start_button = SpriteNode('./assets/sprites/start.PNG',
                                       parent = self,
                                       position = start_button_position,
                                       scale = 0.5)

        # help button
        help_button_position = Vector2()
        help_button_position.x = self.screen_center_x
        help_button_position.y = self.screen_center_y * 0.6
        self.help_button = SpriteNode('./assets/sprites/help.PNG',
                                      parent = self,
                                      position = help_button_position,
                                      scale = 0.5)

        # options button
        options_button_position = Vector2()
        options_button_position.x = self.screen_center_x
        options_button_position.y = self.screen_center_y * 0.2
        self.options_button = SpriteNode('./assets/sprites/options.PNG',
                                      parent = self,
                                      position = options_button_position,
                                      scale = 0.5)

    def touch_began(self, touch):
        # creating a pop effect when a button(s) is clicked

        # back button
        if self.options_button.frame.contains_point(touch.location):
            self.options_button.scale = 0.475

        # help button
        if self.help_button.frame.contains_point(touch.location):
            self.help_button.scale = 0.475

        # start button
        if self.start_button.frame.contains_point(touch.location):
            self.start_button.scale = 0.475

    def touch_ended(self, touch):
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
