import pygame, sys
import pygame.gfxdraw
import pygame.draw

pygame.init()
pygame.font.init()

img = pygame.image.load('image.jpg')
imgX = 280
imgY = 70
white = (255, 255, 255)
purple = (51, 0, 51)
black = (0, 0, 0)
yellow = (255, 255, 0)
light_yellow = (255, 255, 0)
red = (255, 0, 0)
light_red = (255, 0, 0)
green = (0, 153, 0)
blue = (0, 0, 255)
l_red = (153, 0, 0)
l_green = (0, 153, 0)
l_blue = (0, 0, 153)
l_yellow = (204, 204, 0)

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)

screen = pygame.display.set_mode((800, 650))
pygame.display.set_caption("Ludo Star")

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)


def image():
    screen.blit(img, (imgX, imgY))


def text_objects(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
    screen.blit(textSurf, textRect)


def message_to_screen(msg, color, font_size, display_width, display_height):
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render(msg, True, color)
    screen.blit(text, [display_width, display_height])


def Play():
    pass


def Quit():
    pygame.quit()


def Instructions():
    # gameIns = True

    # while gameIns:
    #   for event in pygame.event.get():
    #      if event.type == pygame.QUIT:
    #         pygame.quit()
    #        quit()

    screen.fill(green)
    message_to_screen("Instructions", black, 70, 180, 50)
    message_to_screen("1. Press the space bar button to roll the dice.", black, 20, 10, 140)
    message_to_screen("2. Unless you get a '6' when rolling the dice, your planes can't take off.", black, 20, 10, 170)
    message_to_screen("3. You won't get an extra turn for rolling a six nor for killing other players.", black, 20, 10,
                      200)
    message_to_screen("4. If there are two planes of the same color on top of each other than that", black, 20, 10, 230)
    message_to_screen("plane cannot be killed.", black, 20, 10, 260)
    message_to_screen("5. To win the game, your planes have to traverse around the board and come", black, 20, 10, 290)
    message_to_screen("into the home lane.", black, 20, 10, 320)
    message_to_screen("6. If the plane lands on stop, it cannot be killed.", black, 20, 10, 350)
    message_to_screen("7. To kill another color’s plane, you have to make your plane land on that", black, 20, 10, 380)
    message_to_screen("box where other colored plane is.", black, 20, 10, 410)

    # button("Play", 130, 520, 100, 50, red, light_red, Play)
    # button("Main", 240, 500, 100, 50, yellow, light_yellow, gameIntro)
    # button("Quit", 440, 500, 100, 50, red, light_red,Quit)

    pygame.display.update()
    pygame.time.delay(7000)
    # clock.tick(15)


def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            action()
            return False
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))
    text_to_button(text, black, x, y, width, height)
    return True


def gameIntro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(purple)

        image()
        button("Play", 300, 320, 180, 50, red, light_red, Play)
        button("Instructions", 300, 390, 180, 50, yellow, light_yellow, Instructions)
        button("Quit", 300, 460, 180, 50, red, light_red, Quit)

        clock.tick(15)
        pygame.display.update()


def initial():
    page = True
    while page:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill(purple)
        image()
        x = button("Play", 300, 320, 180, 50, red, light_red, Play)
        y = button("Instructions", 300, 390, 180, 50, yellow, light_yellow, Instructions)
        z = button("Quit", 300, 460, 180, 50, red, light_red, Quit)
        if (x and z) == False:
            page = False

        pygame.display.update()


if __name__ == "__main__":
    initial()
