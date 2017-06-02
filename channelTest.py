import pygame
import sys

pygame.init()
size = (200, 200)
screen = pygame.display.set_mode(size)
LEFT = 1
s = pygame.mixer.Sound("test1.wav")
s2 = pygame.mixer.Sound("test2.wav")

while True:
    for event in pygame.event.get():
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print "click"
                empty_channel = pygame.mixer.find_channel()
                empty_channel.play(s,-1)
            if event.key == pygame.K_b:
                print "click"
                empty_channel2 = pygame.mixer.find_channel()
                empty_channel2.play(s2,-1)
            if event.key == pygame.K_c:
                print "click"
                empty_channel2.stop();
