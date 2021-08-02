import sys
import pygame


if __name__ == "__main__":
    pygame.init()
    size = (200, 200)
    screen = pygame.display.set_mode(size)
    fanfare_sound = pygame.mixer.Sound("../sound/fanfare.wav")
    warning_sound = pygame.mixer.Sound("../sound/warning.wav")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print ("clicked Ctrl+a")
                    print("play s music")
                    empty_channel = pygame.mixer.find_channel()
                    empty_channel.play(fanfare_sound, -1)
                if event.key == pygame.K_b:
                    print ("click Ctrl+b")
                    print("play s2 music")
                    empty_channel2 = pygame.mixer.find_channel()
                    empty_channel2.play(warning_sound, -1)
                if event.key == pygame.K_d:
                    print("click Ctrl+b")
                    if empty_channel2:
                        print("stoppped s2 music")
                        empty_channel2.stop()
