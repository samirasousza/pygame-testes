import pygame, sys, random


class Crosshair(pygame.sprite.Sprite):

    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("assets/gunshot.mp3")

    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Target(pygame.sprite.Sprite):

    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 1300
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("assets/BG.png")
pygame.mouse.set_visible(False)

# Crosshair
crosshair = Crosshair("assets/crosshair.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

# Target
target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target("assets/target.png", random.randrange(0, screen_width),
                        random.randrange(0, screen_height))
    target_group.add(target_group)

target_group.draw(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()
    target_group.draw(screen)
    pygame.display.flip()
    target_group.draw(screen)
    screen.blit(background, (0, 0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    target_group.draw(screen)
    crosshair_group.update()
    target_group.draw(screen)
    clock.tick(80)
