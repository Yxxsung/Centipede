#Sophia Alexander
#Centipede Atari 2600 recreation

import pygame
import random

pygame.init()

#establishes the screen for gameplay and its size h,v
screen = pygame.display.set_mode((1600, 1000)) #may have to be tweaked

#establishes the game clock
clock = pygame.time.Clock()

#The class that establishes the bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #loads the sprite and optimizes it for pygame
        self.image = pygame.image.load("bulletsprite.png").convert_alpha()
        #sets the starting position using the image's dimensions
        self.rect = self.image.get_rect()
        self.rect.center = (400,300) #may have to be tweaked

#The class that establishes the player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # loads the sprite and optimizes it for Pygame
        self.image = pygame.image.load("centipede-sprite.png").convert_alpha()
        # sets the starting position using the image's dimensions
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)  # May have to tweak these later!

class Centipede(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # it also needs to store its position and horozontal direction (+1 or -1)
        # The following 4 lines keep an 'original' version of the sprite to reverse horozontally (Switching directions)
        self.original_image = pygame.Surface((30, 50))
        self.original_image.fill((255, 0, 0))  # Red NPC
        self.image = self.original_image
        self.rect = self.image.get_rect()

        #Stores the position as a Vector2 for smoother movement
        self.pos = pygame.math.Vector2(x, y)
        self.rect.center = self.pos

        #Stores the horozontal position (1 = right, -1 = left)
        self.direction = 1
        self.speed = 3 #May need to be tweaked a bit!

class Mushroom (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("mushroomSprite.png").convert_alpha()
        for _ in range(30):
            x = random.randrange(0, screen.get_width(), 20)
            y = random.randrange(0, screen.get_height(), 20)


    #updates the direction of movement
    def update(self):
        self.pos.x += self.speed * self.direction
        self.rect.center = self.pos

        #flips the image when the direction changes
        if self.direction == -1:
            self.image = pygame.transform.flip(self.original_image, True, False)
        else:
            self.image = self.original_image

    def change_direction(selfself):
        self.direction *= -1



#MAIN GAME LOOP
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
while running:
    clock.tick(60)
    screen.fill((255, 255, 255)) #Black

    #EVENTS IN GAME
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:


#Draws the sprites on screen so the player can see them
all_sprites.draw(screen)
