import pygame, sys
from pygame.locals import *

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 128, 0)
sqs = 70
bs = 8*sqs


pygame.init()
screen = pygame.display.set_mode((bs, bs))
screen.fill(green)
for y in range(8):
	for x in range(8):
		pygame.draw.rect(screen, black, (y*sqs, x*sqs, sqs,sqs), 2)

pygame.display.set_caption('Othello ala Linus och Kasper!')
pygame.mouse.set_visible(True)
while True:
	if pygame.mouse.get_pressed():
		x,y = pygame.mouse.get_pos()
		print x,y
	pygame.display.update()