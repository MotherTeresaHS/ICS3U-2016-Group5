# Created by: Rehan and Paul
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the main game

from scene import *
import ui
import sound
import random

class GameScene(Scene):
    def setup(self):
        # constants 
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.leftBound = self.screen_center_x * 0.5
        self.rightBound = self.screen_center_x * 1.45
        self.player_move_speed = 30
        self.goalie_move_speed = random.randint(10,50)
        self.defender_attack_speed = 10
        self.defender_attack_rate = 1
        self.score = 0

        # true and false statements
        self.left_button_down = False
        self.right_button_down = False
        self.shoot_button_down = False
        self.movingLeft = True
        self.game_over = False

        # arrays
        self.defender = []
        self.pucks = []

        # add rink background
        rink_background_position = Vector2(self.screen_center_x, 
                                      self.screen_center_y)
        self.rink_background = SpriteNode('./assets/sprites/rink.JPG',
                                       parent = self,
                                       position = rink_background_position,
                                       size = self.size)

        # exit button
        exit_button_position = self.size
        exit_button_position.x = 75
        exit_button_position.y = exit_button_position.y - 100
        self.exit_button = SpriteNode('./assets/sprites/exit.PNG',
                                       parent = self,
                                       position = exit_button_position,
                                       scale = 0.1)

        # left button
        left_button_position = Vector2()
        left_button_position.x = 100
        left_button_position.y = 100
        self.left_button = SpriteNode('./assets/sprites/left.PNG',
                                      parent = self,
                                      position = left_button_position,
                                      scale = 0.1)

        # right button
        right_button_position = Vector2()
        right_button_position.x = 300
        right_button_position.y = 100
        self.right_button = SpriteNode('./assets/sprites/right.PNG',
                                       parent = self,
                                       position = right_button_position,
                                       scale = 0.1)

        # shoot button
        shoot_button_position = Vector2()
        shoot_button_position.x = self.size_of_screen_x - 100
        shoot_button_position.y = 100
        self.shoot_button = SpriteNode('./assets/sprites/shoot.PNG',
                                      parent = self,
                                      position = shoot_button_position,
                                      scale = 0.1)

        # net
        net_position = Vector2()
        net_position.x = self.screen_center_x
        net_position.y = self.screen_center_y * 1.762
        self.net = SpriteNode('./assets/sprites/net.PNG',
                                      parent = self,
                                      position = net_position,
                                      scale = 0.25)

        # player
        player_position = Vector2()
        player_position.x = self.screen_center_x
        player_position.y = 240
        self.player = SpriteNode('./assets/sprites/player.PNG',
                                    parent = self,
                                    position = player_position,
                                    scale = 0.15)

        # goalie
        goalie_position = Vector2(self.screen_center_x, self.screen_center_y * 1.4)
        self.goalie = SpriteNode('./assets/sprites/goalie.PNG',
                                    parent = self,
                                    position = goalie_position,
                                    scale = 0.15)

        # game over pop up
        game_over_background_position = Vector2(self.screen_center_x, 
                                      self.screen_center_y)
        self.game_over_background = SpriteNode('./assets/sprites/game_over.PNG',
                                       parent = self,
                                       position = game_over_background_position,
                                       scale = 1.2,
                                       alpha = 0)

        # game over label
        game_over_label_position = Vector2()
        game_over_label_position.x = self.screen_center_x
        game_over_label_position.y = self.screen_center_y * 1.185
        self.game_over_label = LabelNode(text = 'Game Over!',
                                      font = ('Avenir Next Condensed', 100),
                                      parent = self,
                                      position = game_over_label_position,
                                      alpha = 0)

        # main menu button
        menu_button_position = Vector2()
        menu_button_position.x = self.screen_center_x
        menu_button_position.y = self.screen_center_y * 0.875
        self.menu_button = SpriteNode('./assets/sprites/main_menu.PNG',
                                       parent = self,
                                       position = menu_button_position,
                                       scale = 0.5,
                                       alpha = 0)

        # score label
        self.score_position = Vector2()
        self.score_position.x = self.screen_center_x
        self.score_position.y = 30
        self.score_label = LabelNode(text = 'Score: 0',
                                     color = 'red',
                                     font = ('Avenir Next Condensed', 40),
                                     parent = self,
                                     position = self.score_position)

    def update(self):
        # makes the player move left
        if (self.player.position.x - self.player_move_speed) > (self.screen_center_x * 0.25):
            if self.left_button_down == True:
                playerMove = Action.move_by(-1 * self.player_move_speed, 
                                           0.0, 
                                           0.1)
                self.player.run_action(playerMove)

        # makes the player move right
        if (self.player.position.x + self.player_move_speed) < self.size_of_screen_x - (self.screen_center_x * 0.25):
            if self.right_button_down == True:
                playerMove = Action.move_by(self.player_move_speed, 
                                           0.0, 
                                           0.1)
                self.player.run_action(playerMove)

        # makes the goalie move
        if self.movingLeft == True:
            goalieMove = Action.move_by(-1 * self.goalie_move_speed, 
                                           0.0, 
                                           0.1)
            self.goalie.run_action(goalieMove)
            if self.goalie.position.x < self.leftBound:
                self.goalie.position.x = self.leftBound
                self.goalie_move_speed = random.randint(10,50)
                self.movingLeft = False

        if self.movingLeft == False:
            goalieMove = Action.move_by(self.goalie_move_speed, 
                                           0.0, 
                                           0.1)
            self.goalie.run_action(goalieMove)
            if self.goalie.position.x > self.rightBound:
                self.goalie_move_speed = random.randint(10,50)
                self.goalie.position.x = self.rightBound
                self.movingLeft = True

        # check every update to see if a puck is off the screen
        for puck in self.pucks:
            if puck.position.y > self.size_of_screen_y * 1.1:
                puck.remove_from_parent()
                self.pucks.remove(puck)

        # check every update to see if a puck has entered the net
        for puck in self.pucks:
            if self.net.frame.contains_rect(puck.frame):
                puck.remove_from_parent()
                self.pucks.remove(puck)
                sound.play_effect('./assets/sounds/goal.wav')
                self.score = self.score + 1

        # check every update to see if a new defender should be created
        defender_create_chance = random.randint(1, 120)
        if defender_create_chance <= self.defender_attack_rate:
            if self.game_over == False:
                self.add_defender()

        # check every update to see if a defender is off screen
        for defender in self.defender:
            if defender.position.y < -50:
                defender.remove_from_parent()
                self.defender.remove(defender)

        # limits you to one puck on the screen
        if len(self.pucks) > 0:
             self.shoot_button_down = False

        # check every update to see if a defender has hit the player
        if len(self.defender) > 0:
            for defender_hit in self.defender:
                if defender_hit.frame.intersects(self.player.frame):
                    sound.play_effect('./assets/sounds/game_over.wav')
                    defender_hit.remove_from_parent()
                    self.defender.remove(defender_hit)
                    self.game_over = True
                    self.menu_button.alpha = 1
                    self.game_over_background.alpha = 1
                    self.game_over_label.alpha = 1
                    self.player_move_speed = 0
                    self.goalie_move_speed = 0

        # check every update to see if a puck has hit a defender
        if len(self.defender) > 0 and len(self.pucks) > 0:
            for defender in self.defender:
                for puck in self.pucks:
                    if defender.frame.contains_rect(puck.frame):
                        sound.play_effect('./assets/sounds/game_over.wav')
                        puck.remove_from_parent()
                        self.pucks.remove(puck)
                        defender.remove_from_parent()
                        self.defender.remove(defender)
                        self.game_over = True
                        self.menu_button.alpha = 1
                        self.game_over_background.alpha = 1
                        self.game_over_label.alpha = 1
                        self.player_move_speed = 0
                        self.goalie_move_speed = 0

        # check every update to see if a puck has hit the goalie
        for puck in self.pucks:
            if self.goalie.frame.intersects(puck.frame):
                sound.play_effect('./assets/sounds/game_over.wav')
                puck.remove_from_parent()
                self.pucks.remove(puck)
                self.game_over = True
                self.menu_button.alpha = 1
                self.game_over_background.alpha = 1
                self.game_over_label.alpha = 1
                self.player_move_speed = 0
                self.goalie_move_speed = 0

        else:
            pass

        # shows the score
        self.score_label.text = 'Score: ' + str(self.score)

    def touch_began(self, touch):
        # creates a pop effect when a button(s) is clicked

        # exit button
        if self.exit_button.frame.contains_point(touch.location):
            self.exit_button.scale = 0.09

        # left button
        if self.left_button.frame.contains_point(touch.location):
            self.left_button.scale = 0.09
            self.left_button_down = True

        # right button
        if self.right_button.frame.contains_point(touch.location):
            self.right_button.scale = 0.09
            self.right_button_down = True

        # shoot button
        if self.shoot_button.frame.contains_point(touch.location):
            self.shoot_button.scale = 0.09
            self.shoot_button_down = True

        # main menu button
        if self.menu_button.frame.contains_point(touch.location):
            self.menu_button.scale = 0.475

    def touch_ended(self, touch):
        # if the exit button is pressed, go to the main menu scene
        if self.exit_button.frame.contains_point(touch.location):
            self.exit_button.scale = 0.1
            sound.play_effect('./assets/sounds/click.wav')
            self.dismiss_modal_scene()

        # left button
        if self.left_button.frame.contains_point(touch.location):
            self.left_button.scale = 0.1

        # right button
        if self.right_button.frame.contains_point(touch.location):
            self.right_button.scale = 0.1

        # shoot button
        if self.shoot_button.frame.contains_point(touch.location):
            sound.play_effect('./assets/sounds/click.wav')
            self.shoot_button.scale = 0.1

        # main menu button
        if self.game_over == True: 
            if self.menu_button.frame.contains_point(touch.location):
                sound.play_effect('./assets/sounds/click.wav')
                self.menu_button.scale = 0.5
                self.dismiss_modal_scene()

        # shoots a puck
        if self.shoot_button.frame.contains_point(touch.location):
            # only shoot if it is not game over
            if self.game_over == False:
                if self.shoot_button_down == True:
                    self.create_new_puck()

        # stops the player from moving when the left or right button isn't pressed
        else:
            self.left_button_down = False
            self.right_button_down = False

    def create_new_puck(self):
        # creates a puck
        puck_start_position = Vector2()
        puck_start_position.x = self.player.position.x
        puck_start_position.y = self.screen_center_y * 0.55

        puck_end_position = Vector2()
        puck_end_position.x = puck_start_position.x
        puck_end_position.y = self.size_of_screen_y + 100

        # puck
        self.pucks.append(SpriteNode('./assets/sprites/puck.png',
                             position = puck_start_position,
                             parent = self,
                             scale = 0.05))

        # makes a puck move forward
        puckMoveAction = Action.move_to(puck_end_position.x, 
                                           puck_end_position.y + 100, 
                                           2.5)
        self.pucks[len(self.pucks)-1].run_action(puckMoveAction)

    def add_defender(self):
        # creates a defender
        defender_start_position = Vector2()
        defender_start_position.x = random.randint(100, 
                                         self.size_of_screen_x - 100)
        defender_start_position.y = self.size_of_screen_y + 100

        defender_end_position = Vector2()
        defender_end_position.x = self.player.position.x
        defender_end_position.y = -100

        # defender
        self.defender.append(SpriteNode('./assets/sprites/defender.PNG',
                             position = defender_start_position,
                             parent = self,
                             scale = 0.125,
                             alpha = 0.8))

        # makes a defender move downward
        defenderMoveAction = Action.move_to(defender_end_position.x, 
                                         defender_end_position.y, 
                                         self.defender_attack_speed,
                                         TIMING_SINODIAL)
        self.defender[len(self.defender)-1].run_action(defenderMoveAction)
