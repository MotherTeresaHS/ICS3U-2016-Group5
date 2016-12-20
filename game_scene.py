# Created by: Rehan and Paul
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the main game.

from scene import *
import ui
import sound

class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.left_button_down = False
        self.right_button_down = False
        self.game_over = False
        self.player_move_speed = 20.0
        self.goalie_move_speed = 1.0
        self.score = 0
        self.pucks = []

        # add rink background
        self.background = SpriteNode('./assets/sprites/rink.JPG',
                                       parent = self,
                                       position = self.size/2,
                                       scale = 1)

        # exit button
        exit_button_position = Vector2()
        exit_button_position.x = 75
        exit_button_position.y = 949
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
        net_position.x = 384
        net_position.y = 901.5
        self.net = SpriteNode('./assets/sprites/net.PNG',
                                      parent = self,
                                      position = net_position,
                                      scale = 0.249)

        # player
        player_position = Vector2()
        player_position.x = self.screen_center_x
        player_position.y = 240
        self.player = SpriteNode('./assets/sprites/player.PNG',
                                    parent = self,
                                    position = player_position,
                                    scale = 0.15)

        # goalie
        goalie_start_position = Vector2()
        goalie_start_position.x = 205
        goalie_start_position.y = 725

        goalie_end_position = Vector2()
        goalie_end_position.x = 565
        goalie_end_position.y = 725

        self.goalie = SpriteNode('./assets/sprites/goalie.PNG',
                                    parent = self,
                                    position = goalie_start_position,
                                    scale = 0.15)

        # make goalie move
        goalieMoveAction = Action.move_to(goalie_end_position.x, 
                                         goalie_end_position.y,  
                                         self.goalie_move_speed)
        self.goalie.run_action(goalieMoveAction)

        # game over scene "illusion"
        self.game_over_background = SpriteNode('./assets/sprites/background.JPG',
                                       parent = self,
                                       position = self.size/2,
                                       alpha = 0)

        # game over label
        game_over_label_position = Vector2()
        game_over_label_position.x = 384
        game_over_label_position.y = 612
        self.game_over_label = LabelNode(text = 'Game Over!',
                                      font=('Avenir Next Condensed', 100),
                                      parent = self,
                                      position = game_over_label_position,
                                      alpha = 0)

        # main menu button
        menu_button_position = Vector2()
        menu_button_position.x = 384
        menu_button_position.y = 412
        self.menu_button = SpriteNode('./assets/sprites/main_menu.PNG',
                                       parent = self,
                                       position = menu_button_position,
                                       scale = 0.5,
                                       alpha = 0)

        # score label
        self.score_position = Vector2()
        self.score_position.x = 384
        self.score_position.y = 30
        self.score_label = LabelNode(text = 'Score: 0',
                                     font=('Avenir Next Condensed', 40),
                                     parent = self,
                                     position = self.score_position)

    def update(self):
        # this method is called, hopefully, 60 times a second

        # move the player if the button is down
        if (self.player.position.x - self.player_move_speed)> 80:
            if self.left_button_down == True:
                playerMove = Action.move_by(-1*self.player_move_speed, 
                                           0.0, 
                                           0.1)
                self.player.run_action(playerMove)

        if (self.player.position.x + self.player_move_speed) < self.size_of_screen_x-80:
            if self.right_button_down == True:
                playerMove = Action.move_by(self.player_move_speed, 
                                           0.0, 
                                           0.1)
                self.player.run_action(playerMove)

        # check every update if a puck is off the screen
        for puck in self.pucks:
            if puck.position.y > self.size_of_screen_y + 50:
                puck.remove_from_parent()
                self.pucks.remove(puck)

        # check every update to see if a puck has entered the net
        for puck in self.pucks:
            if self.net.frame.contains_rect(puck.frame):
                puck.remove_from_parent()
                self.pucks.remove(puck)
                self.score = self.score + 1

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

        else:
            pass

        # show the score
        self.score_label.text = 'Score: ' + str(self.score)

    def touch_began(self, touch):
        # this method is called, when user touches the screen

        # # creating a pop effect when a button(s) is clicked

        # exit button
        if self.exit_button.frame.contains_point(touch.location):
            self.exit_button.scale = 0.09

        # controls
        if self.left_button.frame.contains_point(touch.location):
            self.left_button.scale = 0.09
            self.left_button_down = True

        if self.right_button.frame.contains_point(touch.location):
            self.right_button.scale = 0.09
            self.right_button_down = True

        if self.shoot_button.frame.contains_point(touch.location):
            self.shoot_button.scale = 0.09

        # main menu button
        if self.menu_button.frame.contains_point(touch.location):
            self.menu_button.scale = 0.45

    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen

        # if the exit button is pressed, go to the main menu scene
        if self.exit_button.frame.contains_point(touch.location):
            self.exit_button.scale = 0.1
            sound.play_effect('./assets/sounds/click.wav')
            self.dismiss_modal_scene()

        # controls
        if self.left_button.frame.contains_point(touch.location):
            self.left_button.scale = 0.1

        if self.right_button.frame.contains_point(touch.location):
            self.right_button.scale = 0.1

        if self.shoot_button.frame.contains_point(touch.location):
            sound.play_effect('./assets/sounds/puck.wav')
            self.shoot_button.scale = 0.1

        # main menu button
        if self.game_over == True: 
            if self.menu_button.frame.contains_point(touch.location):
                sound.play_effect('./assets/sounds/click.wav')
                self.menu_button.scale = 0.5
                self.dismiss_modal_scene()

        # shoot the puck
        if self.shoot_button.frame.contains_point(touch.location):
            # only shoot if it is not game over
            if self.game_over == False:
                self.create_new_puck()

        # if finger is removed, the player should not be moving anymore
        else:
            self.left_button_down = False
            self.right_button_down = False

    def create_new_puck(self):
        # creating the puck
        puck_start_position = Vector2()
        puck_start_position.x = self.player.position.x
        puck_start_position.y = 270

        puck_end_position = Vector2()
        puck_end_position.x = puck_start_position.x
        puck_end_position.y = self.size_of_screen_y + 270

        self.pucks.append(SpriteNode('./assets/sprites/puck.png',
                             position = puck_start_position,
                             parent = self,
                             scale = 0.05))

        # make the puck move forward
        puckMoveAction = Action.move_to(puck_end_position.x, 
                                           puck_end_position.y + 100, 
                                           5.0)
        self.pucks[len(self.pucks)-1].run_action(puckMoveAction)
