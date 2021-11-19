import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('desafio21.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.7)
pygame.event.wait()


