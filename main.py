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
        self.rect.center = (800, 900)  # May have to tweak these later!

    #moves the player left and right when the left and right arrow keys are pressed
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

class CentipedeSegment(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        #load the image
        self.original_image = pygame.image.load("centipede-sprite.png").convert_alpha()
        #scale it to fit the grid
        self.original_image = pygame.transform.scale(self.original_image, (20, 20))

        self.image = self.original_image
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = 1

    def update(self, mushrooms):
        self.rect.x += 3 * self.direction

        if self.rect.right >= 1600 or self.rect.left <= 0:
            self.direction *= -1
            self.rect.y += 20

        #flip the sprite based on the direction
        if self.direction == -1:
            self.image = pygame.transform.flip(self.original_image, True, False)
        else:
            self.image = self.original_image

            #makes the centipede shift directions and shift down when it hits a mushroom
            for mushroom in mushrooms:
                if self.rect.colliderect(mushroom.rect):
                    self.direction *= -1
                    self.rect.y += 20
                    break


class Mushroom (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("mushroomSprite.png").convert_alpha()
        self.rect = self.image.get_rect()


mushrooms = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
all_sprites.add(mushrooms)

#this loop and the below add statement add random mushrooms on the map
for _ in range(30):
    m = Mushroom()
    m.rect.topleft = (
        random.randrange(0, 1600, 20),
        random.randrange(0, 800, 20)
    )
    mushrooms.add(m)

centipede = pygame.sprite.Group()
for i in range(10):
    centipede.add(CentipedeSegment(i*20, 0))


#MAIN GAME LOOP -- INDENT EVERTHING IN THE MAIN LOOP TO BE INSIDE THE WHILE RUNNING!!
bullets = pygame.sprite.Group()

running = True
while running:
    clock.tick(60)

    #EVENTS IN GAME
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                bullets.add(bullet)

    #This chunk is the cenptipede movement logic
    positions = [seg.rect.topleft for seg in centipede]

    for i, segment in enumerate(centipede):
        if i == 0:
            segment.update(mushrooms)
        else:
            segment.rect.topleft = positions[i - 1]

    #this chunk makes it so if the bullet hits the mushrooms or centipede it 'kills'
    for bullet in bullets:
        if pygame.sprite.spritecollide(bullet, centipede, True):
            bullet.kill()

        if pygame.sprite.spritecollide(bullet, mushrooms, True):
            bullet.kill()

    if pygame.sprite.spritecollide(player, centipede, False):
        print("Game Over")
        running = False

    #UPDATE (no longer includes centipede.update())
    all_sprites.update()
    bullets.update()
    mushrooms.update()


    #DRAWS EVERYTHING
    screen.fill((0, 0, 0)) #Black
    all_sprites.draw(screen)
    bullets.draw(screen)
    mushrooms.draw(screen)
    centipede.draw(screen)

    pygame.display.flip()



