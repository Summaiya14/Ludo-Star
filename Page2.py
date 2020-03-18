import pygame, sys
import pygame.gfxdraw
import pygame.draw
import random
pygame.init()
pygame.font.init()

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

size = width, height = 800, 650
win = pygame.display.set_mode((size))
pygame.display.set_caption("Ludo Star")

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

player_list = []

def message_to_screen(msg,color,font_size,display_width,display_height):
	font = pygame.font.Font('freesansbold.ttf',font_size)
	text = font.render(msg,True,color)
	win.blit(text,[display_width,display_height])

def button(x, y, width, height, active_color, inactive_color, text, text_size, text_color):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(win, active_color, [x, y, width, height])
        message_to_screen(text, text_color, text_size, x + 10, y + 10)
        if click[0] == 1:
            return True
        else:
            return False
    else:
        pygame.draw.rect(win, inactive_color, [x, y, width, height])
        message_to_screen(text, text_color, text_size, x+10, y+10)
        return False


def name(color, wdt, ht, n):
    name = "NONE"
    s = True
    text = "PLAYER_" + str(n)
    font = pygame.font.Font(None, 50)
    pygame.draw.rect(win, color, [800 / 10, ht, 200, 50])
    message_to_screen(text, black, 30, 800 / 10 + 25 , ht + 10)
    pygame.draw.rect(win, white, [700/2, ht, 200, 50])

    pygame.draw.rect(win, black, [800-200, ht, 100, 50])
    message_to_screen("SUBMIT", white, 20, 800 - 200 + 10, ht+10)

    while s:
        for evt in pygame.event.get():
            if evt.type == pygame.KEYDOWN:
                if evt.unicode.isalpha():
                    name += evt.unicode
                elif evt.key == pygame.K_BACKSPACE:
                    name = name[:-1]
            if evt.type == pygame.QUIT: quit()
        if button(800 - 200, ht , 100, 50, red, black, "SUBMIT", 20, white) == True:
            s = False

        pygame.draw.rect(win, white, [700 / 2, ht, 200, 50])
        block = font.render(name, True, color)
        win.blit(block, [700 / 2 + 25, ht + 10])
        pygame.display.update()
    return name

def page2():
	flag = True
	page2 = True
	win.fill(purple)
	while page2:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: quit()
		message_to_screen("Enter Player Names", white, 45, 180, 50)
		if(flag):
			player_list.append(name(red, 700, 140, 1))
			player_list.append(name(green, 700, 210, 2))
			player_list.append(name(blue, 700, 280, 3))
			player_list.append(name(yellow, 700, 350, 4))
			flag = False
		pygame.draw.rect(win,white,[700-350,650-200,100,50])
		message_to_screen("PLAY",white,30,700-350+10,650-200+10)
		if(button(700-350,650-200,100,50,red,black,"PLAY",30,white)==True):
			page2 = False
		pygame.display.update()
		if(page2 == False):
			return player_list

if __name__ =="__main__":
	page2()




