import os
import numpy as np
import cv2
import pygame
pygame.mixer.init()
pygame.mixer.music.load('troll.mp3')
pygame.mixer.music.play(999)

img = cv2.imread('boss.jpg',0)
cv2.imshow('App 1.',img)

print('To change song u need to replace mp3 file and call it troll.mp3')
print('To change imige u need to add file called boss.jpg')


