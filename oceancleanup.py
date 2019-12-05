#imports the files (arcade files and the random interger files)
import arcade
import random

#Sprite Sizes
SPRITE_SCALING_TRASHCAN = .15
SPRITE_SCALING_BOTTLE = .1
SPRITE_SCALING_CHEM = .05
SPRITE_SCALING_BAG = .1
SPRITE_SCALING_SODA = .06
SPRITE_SCALING_STRAW = .1

#Amount of trash present on the game screen
TRASH_COUNT = random.randint(0,300)

#Size of the screen and title of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "CLEAN THE OCEAN! | USE YOUR MOUSE TO COLLECT THE TRASH!"

#The states of the game (intro, begin to play, play game, and game over screens)
INTRO_SCREEN = 0
BEGIN_TO_PLAY_SCREEN = 1
GAME_RUNNING_SCREEN = 2
GAME_OVER_SCREEN = 3

#the game class that has different functions inside of it
#This function is the main application class
class OceanGame(arcade.Window):
    def __init__(self, screen_width, screen_height, title):
        #Calls the parent constructor. Required and must be the first line.
        super().__init__(screen_width, screen_height, title)

        #Sets the background color
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

        #Queues the intro screen
        self.current_state = INTRO_SCREEN

        self.TRASHCAN_list = None
        self.trash_list = None

        #Set up the trash can sprite
        self.score = 0
        self.TRASHCAN_sprite = None

        #Instructions page
        self.instructions = []
        texture = arcade.load_texture("images/instructions_0.png")
        self.instructions.append(texture)

        texture = arcade.load_texture("images/instructions_1.png")
        self.instructions.append(texture)

    #This function sets the game up.
    def setup(self):
        #Sprite lists
        self.TRASHCAN_list = arcade.SpriteList()
        self.trash_list = arcade.SpriteList()

        #Sets up the player
        self.score = 0
        self.TRASHCAN_sprite = arcade.Sprite("images/sprites/trashcan.png", SPRITE_SCALING_TRASHCAN)
        self.TRASHCAN_sprite.center_x = 50
        self.TRASHCAN_sprite.center_y = 50
        self.TRASHCAN_list.append(self.TRASHCAN_sprite)

        #Places the item on the game screen, in a random postion, and adds it to the trash list.
        for a_sprite in range(TRASH_COUNT):
            #Adds the water bottle to the game screen and to the trash list
            BOTTLE = arcade.Sprite("images/sprites/water.png", SPRITE_SCALING_BOTTLE)
            BOTTLE.center_x = random.randrange(SCREEN_WIDTH)
            BOTTLE.center_y = random.randrange(SCREEN_HEIGHT)
            self.trash_list.append(BOTTLE)

            #Adds the chemical bottle to the game screen and to the trash list
            CHEM = arcade.Sprite("images/sprites/chemicals.png", SPRITE_SCALING_CHEM)
            CHEM.center_x = random.randrange(SCREEN_WIDTH)
            CHEM.center_y = random.randrange(SCREEN_HEIGHT)
            self.trash_list.append(CHEM)

            #Adds the bag to the game screen and to the trash list
            BAG = arcade.Sprite("images/sprites/bag.png", SPRITE_SCALING_BAG)
            BAG.center_x = random.randrange(SCREEN_WIDTH)
            BAG.center_y = random.randrange(SCREEN_HEIGHT)
            self.trash_list.append(BAG)

            #Adds the soda can to the game screen and to the trash list
            SODA = arcade.Sprite("images/sprites/sodacan.png", SPRITE_SCALING_SODA)
            SODA.center_x = random.randrange(SCREEN_WIDTH)
            SODA.center_y = random.randrange(SCREEN_HEIGHT)
            self.trash_list.append(SODA)

            #Adds the straw to the game screen and to the trash list
            STRAW = arcade.Sprite("images/sprites/straw.png", SPRITE_SCALING_STRAW)
            STRAW.center_x = random.randrange(SCREEN_WIDTH)
            STRAW.center_y = random.randrange(SCREEN_HEIGHT)
            self.trash_list.append(STRAW)

    #Makes the mouse disappear
        self.set_mouse_visible(False)

    #Draws the instructions page as an image
    def draw_instructions_page(self, page_number):
        page_texture = self.instructions[page_number]
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, page_texture.width, page_texture.height, page_texture, 0)


    #Draws the game over screen or the last screen.
    def draw_game_over(self):
        output = "You cleaned up the ocean!"
        arcade.draw_text(output, 130, 400, arcade.color.WHITE, 38)

        output = "Click to Play Again"
        arcade.draw_text(output, 280, 300, arcade.color.WHITE, 24)

    #Takes the code in the on_draw function and moves it to the draw_game fuction. This occurs after arcade.start_render() is called.
    #This function draws all of the sprites and displays the total amount of trash collected.
    def draw_game(self):
        self.TRASHCAN_list.draw()
        self.trash_list.draw()

        #This is for the score.
        total = f"# of Trash Collected: {self.score}"
        arcade.draw_text(total, 10, 20, arcade.color.WHITE, 14)

    #Draws the different screens depending on the current screen it is in.
    def on_draw(self):

        arcade.start_render()

        if self.current_state == INTRO_SCREEN:
            self.draw_instructions_page(0)

        if self.current_state == BEGIN_TO_PLAY_SCREEN:
            self.draw_instructions_page(1)

        if self.current_state == GAME_RUNNING_SCREEN:
            self.draw_game()

        else:
            self.draw_game()
            self.draw_game_over()


    #Allows the screen to change when you click the mouse
    def on_mouse_press(self, x, y, button, modifiers):
        #Change states as needed.

        if self.current_state == INTRO_SCREEN:
            #Next screen.
            self.current_state = BEGIN_TO_PLAY_SCREEN

        if self.current_state == BEGIN_TO_PLAY_SCREEN:
            #Intro Screen
            self.setup()
            self.current_state = GAME_RUNNING_SCREEN

        if self.current_state == GAME_OVER_SCREEN:
            #Restart Game
            self.setup()
            self.current_state = GAME_RUNNING_SCREEN

    def on_mouse_motion(self, x, y, dx, dy):
        #Only moves the user if the game is running.

        if self.current_state == GAME_RUNNING_SCREEN:
            self.TRASHCAN_sprite.center_x = x
            self.TRASHCAN_sprite.center_y = y

    #Updates if the game screen is GAME_RUNNING_SCREEN
    def update(self, delta_time):

        #Only moves and does things if the game is running.
        if self.current_state == GAME_RUNNING_SCREEN:
            # Call update on all sprites
            self.trash_list.update()
            self.TRASHCAN_list.update()

            #Generates a list of all sprites that collide with the trash can.
            trash_hit_list = arcade.check_for_collision_with_list(self.TRASHCAN_sprite, self.trash_list)

            #Loops through each colliding sprite (if the trash can collects and item), removes it, and adds to the score
            for aTrash in trash_hit_list:
                aTrash.kill()
                self.score = self.score + 1

            #If all of the trash is collected, then move to a "GAME_OVER" screen
            if len(self.trash_list) == 0:
                self.current_state = GAME_OVER_SCREEN
                self.set_mouse_visible(True)

def main():
    OceanGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()