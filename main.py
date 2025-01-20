import pygame
from pygame.locals import *
from constants import *


def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	bg_color = (0,0,0)
	while 1:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
		    	   	return
		screen.fill((0,0,0))
		pygame.display.flip()

if __name__ == "__main__":
	main()
