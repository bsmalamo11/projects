import pygame
import os
import time
import random

pygame.font.init()  # it will control the font of the text in the game

# Initialize the mixer module
pygame.init()

# Load the audio file
# audio_file = "laser_sound_effect.wav"  # Adjust the file name and path as needed
# pygame.mixer.music.load(audio_file)

# To adjust the window of the game and it's caption
WIDTH, HEIGHT = 600, 580
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space shooter game")

# Load images that will be used in the game using image.load method in pygame

# PLAYER SHIP
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# OPPONENTS SHIPS
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))

# LASERS
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))

# BACKGROUND
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))
# we used pygame.transform.scale method to control the width and the height
# of the background to be the full of game's screen

# importing sound effect
ship_laser_sound = pygame.mixer.Sound(r"C:\Users\NoteBook\Desktop\Space_game\assets\laser_sound_effect.wav")
# C:\Users\NoteBook\Desktop\Space_game\assets\laser_sound_effect.wav


# initializing the class of the lasers
class Laser:
    def __init__(self, x, y, img):
        self.x = x  # x's position of the laser
        self.y = y  # y's position of the laser
        self.img = img  # it will adjust which laser we are going to use
        self.mask = pygame.mask.from_surface(self.img)  # determine all pixels of the laser

    # initializing a function to display the laser
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))  # blit method is used to draw one img into another

    # A function to control the lasers' movement
    def move(self, vel):
        self.y += vel  # increase the laser's y position by val

    # Initializing a function to return the result of the operation
    def off_screen(self, height):
        return not ((self.y <= height) and (self.y >= 0))  # checking if the laser is on the screen or not

    def collision(self, obj):
        return collide(self, obj)  # check if the object is colliding to myself


# initializing the class of the ship
class Ship:

    COOLDOWN = 30  # initializing cooldown counter by 30 second

    def __init__(self, x, y, health=100):
        # initializing the objects of the class
        self.x = x  # x's position of the ship
        self.y = y  # y's position of the ship
        self.health = health  # the ship's health
        self.ship_img = None  # it will adjust which ship we are going to use
        self.laser_img = None  # it will adjust which laser we are going to use
        self.lasers = []
        self.cool_down_counter = 0  # to control the lasers which will be shot by the player

    # A function display the ship on the window in positions x and y
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:  # to add each laser to the list
            laser.draw(window)  # the laser will be drawn(displayed/ shown) in the window

    # A function to control laser movement
    def move_lasers(self, vel, obj):
        self.cooldown()  # checking the cooldown function first
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)  # remove the laser which is outside the window
            elif laser.collision(obj):  # if the laser hits the player
                obj.health -= 10  # player's health will be decreased by 10
                self.lasers.remove(laser)  # remove the laser after the hitting

    # A function to handle the cooldown counting to determine the limit of time between shooting laser
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:  # check if the counter reaches 30 == COOLDOWN
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:  # it will be applied first
            self.cool_down_counter += 1  # increasing the counter of the cool down counter

    # A function to control lasers
    def shoot(self):
        if self.cool_down_counter == 0:  # if we are not in the counting process
            laser = Laser(self.x, self.y, self.laser_img)  # create a new laser
            self.lasers.append(laser)  # it will show the laser and add it to the lasers' list
            self.cool_down_counter = 1  # start counting up

    # A function to calculate the width of any image
    def get_width(self):
        return self.ship_img.get_width()  # return the width of the ship

    # A function to calculate the height of any image
    def get_height(self):
        return self.ship_img.get_height()  # return the height of the ship


class Player(Ship):
    def __init__(self, x, y, health=100):  # inheritance from the Ship class
        super().__init__(x, y, health)  # call the info from the Ship class
        self.ship_img = YELLOW_SPACE_SHIP  # choose the ship's image
        self.laser_img = YELLOW_LASER  # choose the laser's image
        self.mask = pygame.mask.from_surface(self.ship_img)  # determine all pixels of the ship
        self.max_health = health

    # A function to control laser movement
    def move_lasers(self, vel, objs):
        self.cooldown()  # checking the cooldown function first
        for laser in self.lasers:
            # ship_laser_sound.play()
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)  # remove the laser which is outside the window
            else:
                for obj in objs:
                    if laser.collision(obj):  # if the laser hits the player
                        objs.remove(obj)  # remove the enemy ship which was hit by the player
                        if laser in self.lasers:  # Checking if the laser is in the list
                            self.lasers.remove(laser)  # remove the laser after the hitting

    # A function to make the health bar appear in the window
    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        # the red bar of the ship's health
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.ship_img.get_height() + 10,
                          self.ship_img.get_width(), 10))
        # the green bar of the ship's health
        pygame.draw.rect(window, (0, 255, 0),
                         (self.x, self.y + self.ship_img.get_height() + 10,
                          self.ship_img.get_width() * (self.health/self.max_health), 10))


class Enemy(Ship):
    # Creating a dictionary for the color of the ships and lasers
    COLOR_MAP = {
                "red": (RED_SPACE_SHIP, RED_LASER),
                "green": (GREEN_SPACE_SHIP, GREEN_LASER),
                "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100):  # inheritance from the Ship class
        super().__init__(x, y, health)  # call the info from the Ship class
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    # A function to control the ships' movement
    def move(self, vel):  # vel => velocity
        self.y += vel  # increase the ship's y position by val

    def shoot(self):
        if self.cool_down_counter == 0:  # if we are not in the counting process
            laser = Laser(self.x-20, self.y, self.laser_img)  # create a new laser
            self.lasers.append(laser)  # it will show the laser and add it to the lasers' list
            self.cool_down_counter = 1  # start counting up


# Initializing a function to determine whether the two objects are collided or not
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x  # determine the distance between the two objects
    offset_y = obj2.y - obj1.y  # determine the distance between the two objects
    # return True if they are collided else return false
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None


def main():
    run = True  # when the game is running
    fps = 60    # frames per second
    level = 0   # the level of the player will be start with level 1
    lives = 5   # the lives of the player before they lose
    main_font = pygame.font.SysFont("comicsans", 50)  # we choose the font of the game (text) and it's size
    lost_font = pygame.font.SysFont("comicsans", 60)
    enemies = []  # Make a list of enemies
    wave_length = 5  # The level time
    enemy_vel = 1  # The enemy ship's velocity
    player_vel = 5
    laser_vel = 5
    player = Player(250, 460)  # call the class Ship and choose the initial position of the ship
    clock = pygame.time.Clock()   # make sure that it runs the same in any computer
    lost = False
    lost_count = 0

    def redraw_window():  # A function that adjust the game actions
        WIN.blit(BG, (0, 0))  # Put the background at the location (0, 0) on the top left
        # draw the text which will be displayed on the game's screen
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))  # the text will be white
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))  # the text will be white
        # set the lives label on the top left of the game's screen
        WIN.blit(lives_label, (20, 10))
        # set the levels label on the top right of the game's screen
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 20, 10))
        # Make enemies appear in the window
        for en in enemies:
            en.draw(WIN)
        # Make player appear in the window
        player.draw(WIN)
        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 280))  # adjusting the text to appear in mid
        pygame.display.update()

    while run:   # check if the game is running or not and if it is the code inside the loop will work
        clock.tick(fps)   # run the game with the fps that we have set (the clock speed)

        redraw_window()  # call the redraw function

        if lives <= 0 or player.health <= 0:  # check the conditions if the player loses
            lost = True  # set the lost with True
            lost_count += 1  # increase the lost_count by 1

        if lost:  # check if the lost variable is true (the player lost)
            if lost_count > fps * 2:  # checking how many seconds has passed since the player lost
                run = False  # stop the game
            else:
                continue

        keys = pygame.key.get_pressed()  # use dictionary of all the keys which will be pressed or not at the moment

        if len(enemies) == 0:
            level += 1  # when the player hit all the enemies their level increases by one
            wave_length += 5  # each level the number of enemies will be increased by 5
            for e in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH - 100),  # Put a random x for each enemy ship
                              random.randrange(-1500, -100),  # Put a random y for each enemy ship
                              random.choice(["red", "blue", "green"]))  # Put a random color for each enemy ship
                enemies.append(enemy)  # add each enemy to the enemies list, so I can access on it later

        for event in pygame.event.get():   # check whether the player is pressing a button or not
            # check if the player preses the x on the top right left by mouse
            # or escape button by keyboard
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                quit()   # the game window will be closed

        # left or a, checking the position not to go out of window
        if keys[pygame.K_LEFT] and player.x - player_vel > 0\
                or keys[pygame.K_a] and player.x - player_vel > 0:
            player.x -= player_vel  # the ship will move pixels as in player_vel to the left
        # right or d, checking the position not to go out of window
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH\
                or keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH:
            player.x += player_vel  # the ship will move pixels as in player_vel to the right
        # up or w, checking the position not to go out of window
        if keys[pygame.K_UP] and player.y - player_vel > 0\
                or keys[pygame.K_w] and player.y - player_vel > 0:
            player.y -= player_vel  # the ship will move pixels as in player_vel to the top
        # down or s, checking the position not to go out of window
        if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() + 15 < HEIGHT\
                or keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT:
            player.y += player_vel  # the ship will move pixels as in player_vel to the button
        if keys[pygame.K_SPACE]:
            ship_laser_sound.play()  # play the laser sound
            player.shoot()  # calling the shooting method

        for enemy in enemies[:]:      # each enemy will appear and move by enemy_vel value
            enemy.move(enemy_vel)  # by using move function from enemy class
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2*60) == 1:  # Each enemy have 50% chance of shooting every second
                enemy.shoot()  # make the enemy shoot the lasers

            if collide(enemy, player):  # checking if the enemy hit the player
                player.health -= 10  # the player's health will be decreased by 10
                enemies.remove(enemy)  # the enemy will be removed from the window

            elif enemy.y + enemy.get_height() > HEIGHT:  # condition to check if the enemy is out of the game window
                lives -= 1  # if that happened the player's life will be decreased by 1
                enemies.remove(enemy)  # remove the object (enemy) from the enemies list

        player.move_lasers(-laser_vel, enemies)  # The negative sign to make the laser of the player's ship move up


def main_menu():
    keys = pygame.key.get_pressed()  # use dictionary of all the keys which will be pressed or not at the moment
    # Choose the font and the size of the text
    title_font = pygame.font.SysFont("comicsans", 40)
    run = True
    while run:
        WIN.blit(BG, (0, 0))
        # Show the text on the screen
        title_label = title_font.render("Press the mouse to begin..!", 1, (255, 255, 255))
        # Determine the position which the text will be in the window
        WIN.blit(title_label, (WIDTH / 2 - title_label.get_width() / 2, 280))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False  # The game will start again (from the beginning)
            if event.type == pygame.MOUSEBUTTONDOWN:  # use click with the mouse to start the game
                main()
    pygame.quit()


main_menu()
