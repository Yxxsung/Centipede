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
    def __init__(self, x, y):
        super().__init__()
        #loads the sprite and optimizes it for pygame
        self.image = pygame.image.load("bulletsprite.png").convert_alpha()
        #sets the starting position using the image's dimensions
        self.rect = self.image.get_rect(center=(x,y))

    #moves the bullet downward and makes it go away when it hits the bottom of the screen
    def update(self):
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()

#The class that establishes the player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # loads the sprite and optimizes it for Pygame
        self.image = pygame.image.load("centipede-sprite.png").convert_alpha()
        # sets the starting position using the image's dimensions
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)  # May have to tweak these later!

    #moves the player left and right when the left and right arrow keys are pressed
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x += 5
        if keys[pygame.K_RIGHT]:
            self.rect.x -= 5

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





#MAIN GAME LOOP
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
while running:
    clock.tick(60)
    screen.fill((0, 0, 0)) #Black

    #EVENTS IN GAME
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:


#Draws the sprites on screen so the player can see them
all_sprites.draw(screen)
