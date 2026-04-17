#Sophia Alexander
#Centipede Atari 2600 recreation

import pygame

pygame.init()

#establishes the screen for gameplay and its size h,v
screen = pygame.display.set_mode((1600, 1000))

#The class that establishes the player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Loads the sprite and optimizes it for Pygame
        self.image = pygame.image.load("HeroSpriteSheet.png").convert_alpha()
        # Sets the starting position using the image's dimensions
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)

#MAIN GAME LOOP
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#Draws the sprites on screen so the player can see them
all_sprites.draw(screen)
