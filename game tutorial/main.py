import pygame

WIDTH, HEIGHT = 900, 500
DISPLAY = pygame.display
WIN = DISPLAY.set_mode((WIDTH, HEIGHT))
DISPLAY.set_caption('Space Battle!')
COLOR = (167, 142, 219)
WHITE = (255, 255, 255)
FPS = 60
BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)
VEL = 5
B_VEl = 7
MAX_BULLETS=5

S_WIDTH, S_HEIGHT = 55, 40

YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(
        pygame.image.load('Assets\spaceship_yellow.png'), (S_WIDTH, S_WIDTH)), 90)

RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(
        pygame.image.load('Assets\spaceship_red.png'), (S_WIDTH, S_WIDTH)), 270)


def draw_win(red, yellow):
    WIN.fill(COLOR)
    pygame.draw.rect(WIN, WHITE, BORDER, )
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    DISPLAY.update()  # to update the display


def yellow_move(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x >= 0:  # left-yellow
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + yellow.width < BORDER.x:  # right-yellow
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # up-yellow
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + yellow.height < HEIGHT:  # down-yellow
        yellow.y += VEL


def red_move(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x > BORDER.x + BORDER.width:  # left-red
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + red.width < WIDTH:  # right-red
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # up-red
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + red.height < 500:  # down-red
        red.y += VEL


def main():
    red = pygame.Rect(675, 200, S_WIDTH, S_WIDTH)
    yellow = pygame.Rect(225, 200, S_WIDTH, S_WIDTH)
    clock = pygame.time.Clock()

    y_bullets = []
    r_bullets = []

    run = True
    while run:  # will run throught game and terminate at the end of game
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:  # KEYDOWN means pressing key and KEYUP means realeasing key
                if event.key == pygame.K_LCTRL and len(y_bullets) <= MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x+yellow.width, yellow.y + yellow.height/2, 10, 5)
                    y_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(r_bullets) <= MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height/2, 10, 5)
                    r_bullets.append(bullet)

        print(y_bullets,r_bullets)
        keys_pressed = pygame.key.get_pressed()  # for positioning

        yellow_move(keys_pressed, yellow)
        red_move(keys_pressed, red)
        # pending from handle bullets  https://youtu.be/jO6qQDNa2UY?t=3743
        draw_win(red, yellow)

    pygame.quit()


if __name__ == '__main__':
    """makes sure that the program runs only when original file is complied, 
    and not when imported in some other project and compiled(kinda)"""
    main()
