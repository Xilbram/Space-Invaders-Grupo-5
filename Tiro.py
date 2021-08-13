import pygame
from pygame.locals import *

display_largura = 750 
display_altura = 600
DisplayJogo = pygame.display.set_mode((display_largura,display_altura))

class Tiro(pygame.sprite.Sprite):
    def __init__(self, posix, posiy):
        super().__init__()
        self.__tiro = pygame.image.load("retangulotiro.png")
        self.__rect = self.__tiro.get_rect()
        self.mask = pygame.mask.from_surface(self.__tiro)
        self.__rect.center = (posix+15, posiy-15)
        self.__velocidade = -6
    
    @property
    def tiro(self):
        return self.__tiro

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, rect):
        self.__rect = rect
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade
    
    def movimento(self):
        if self.__velocidade == -6:
            if self.__rect.y > -50:
                self.__rect.y += self.__velocidade
        else:
            if self.__rect.y < display_altura:
                self.__rect.y += self.__velocidade
    
    def geracao(self):
        DisplayJogo.blit(self.__tiro, (self.__rect.x,self.__rect.y))