from gtts import gTTS
import os
import pygame

pygame.mixer.init()

inp = ' '

language = 'en'

while(True):
    inp = input()
    obj = gTTS(text = inp, lang = language, slow = False)
    obj.save('output.mp3')
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
