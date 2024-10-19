# Example file showing a circle moving on screen
import pygame



class Sprite(pygame.sprite.Sprite):
    # def __init__(self, color, height, width):
    def __init__(self, imgFile = None, color = None, height = None, width = None):
        super().__init__()

        if imgFile != None:
            self.image = pygame.image.load(imgFile)
            self.image.convert()
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            # pygame.draw.circle(self.image, "orange", (self.width//2, self.height//2), 30)
        else:
            self.image = pygame.Surface([width,height])
            self.image.fill(color)
            self.width = width
            self.height = height
        
        self.rect = self.image.get_rect()






# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

ballPos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
catPos = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 3)
# catSprite = pygame.image.load("sprite-blackCat-small.png")
catSprite = Sprite("sprite-blackCat-small.png")
ballSprite = Sprite(None,"blue",100,100)
#catSprite.convert()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("tan")

    #pygame.draw.circle(screen, "rosybrown", ballPos, 40)
    screen.blit(ballSprite.image, (ballPos.x, ballPos.y))

    #pygame.draw.circle(screen, "orange", catPos, 30)
    screen.blit(catSprite.image, (catPos.x, catPos.y))
    # pygame.draw.circle(catSprite.image, "orange", catPos, 30)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        ballPos.y -= 300 * dt
    if keys[pygame.K_s]:
        ballPos.y += 300 * dt
    if keys[pygame.K_a]:
        ballPos.x -= 300 * dt
    if keys[pygame.K_d]:
        ballPos.x += 300 * dt
    
    if keys[pygame.K_UP]:
        ballPos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        ballPos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        ballPos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        ballPos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()