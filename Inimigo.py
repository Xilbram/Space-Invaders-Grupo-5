import pygame
from pygame.locals import *
from abc import ABC, abstractmethod
import random
from Tiro import Tiro

posicoesx = [0,50,100,150,200,250,300,350,400,450,500,550,600,650,700]
posicoesy = [80,160,240]

class Inimigo(pygame.sprite.Sprite, ABC):
    @abstractmethod
    def __init__(self):
        super().__init__()
        self.__velocidade = 5
        self.__dano = 5
        self.__altura = 70
        self.__largura = 30
        self.__cor = (0,255,0)
        self.__vida = 50
        self.__formato_geometrico = pygame.image.load("retanguloinimigo.png")
        self.__rect = self.__formato_geometrico.get_rect()
        self.mask = pygame.mask.from_surface(self.__formato_geometrico)
        self.__rect.center = (0, posicoesy[random.randint(0,len(posicoesy)-1)])

    @property
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade

    @property
    def dano(self):
        return self.__dano
    
    @dano.setter
    def dano(self, dano):
        self.__dano = dano

    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    @property
    def largura(self):
        return self.__largura
    
    @largura.setter
    def largura(self, largura):
        self.__largura = largura

    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, cor):
        self.__cor = cor
    
    @property
    def formato_geometrico(self):
        return self.__formato_geometrico
    
    @formato_geometrico.setter
    def formato_geometrico(self, formato):
        self.__formato_geometrico = formato
    
    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    def movimento(self):
        pass
    
    def geracao(self, display):
        display.blit(self.__formato_geometrico, (self.__rect.x,self.__rect.y))

class Nave(Inimigo, pygame.sprite.Sprite, ABC):
    @abstractmethod
    def __init__(self, largura):
        super().__init__()
        self.__frequencia_tiro = 2
        self.__direcao = random.randint(0,1)
        if self.__direcao == 0:
            self.rect.x = random.randint(-500, -10)
        else:
            self.rect.x = random.randint(largura+10, largura+500)
        self.__maxiposi = posicoesx[random.randint(0,len(posicoesx)-1)]
        self.tiros = pygame.sprite.Group()
        self.__tiro_temporizador = 0
        self.__cooldown_tiro = 2
    
    @property
    def tiro_temporizador(self):
        return self.__tiro_temporizador
    
    @tiro_temporizador.setter
    def tiro_temporizador(self, tiro_temporizador):
        self.__tiro_temporizador = tiro_temporizador

    @property
    def maxiposi(self):
        return self.__maxiposi
    
    @property
    def direcao(self):
        return self.__direcao

    def disparar(self, janela):
        if self.__tiro_temporizador >= self.__cooldown_tiro:
            self.tiros.add(Tiro(self.rect.center, 6, janela))
            self.__tiro_temporizador = 0

    def movimento(self):
        if self.__direcao == 0:
            if self.rect.x < self.__maxiposi:
                self.rect.x += self.velocidade
        else:
            if self.rect.x > self.__maxiposi:
                self.rect.x -= self.velocidade

class NaveComum(Nave, pygame.sprite.Sprite):
    def __init__(self, largura):
        super().__init__(largura)

class Kamikaze(Nave, pygame.sprite.Sprite):
    def __init__(self, largura):
        super().__init__(largura)
        self.formato_geometrico = pygame.image.load("retangulokamikaze.png")
        self.__dano_explosao = 20
    
    @property
    def dano_explosao(self):
        return self.__dano_explosao

    @dano_explosao.setter
    def dano_explosao(self, dano_explosao):
        self.__dano_explosao = dano_explosao
    
    def explodir(self, jogador):
        if jogador.rect.x <= self.rect.x+self.largura/2:
            jogador.rect.x -= 50
        else:
            jogador.rect.x += 50
        if jogador.rect.y+jogador.rect.bottom <= self.rect.y+self.altura/2:
            jogador.rect.y -= 100
        else:
            jogador.rect.y += 100

    def movimento(self, inimigos, altura):
        super().movimento()
        if self.direcao == 0:
            if self.rect.x >= self.maxiposi:
                if self.rect.y <= altura:
                    self.rect.y += self.velocidade
                else:
                    inimigos.remove(self)
        else:
            if self.rect.x <= self.maxiposi:
                if self.rect.y <= altura:
                    self.rect.y += self.velocidade
                else:
                    inimigos.remove(self)

class Meteoro(Inimigo, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.formato_geometrico = pygame.image.load("retangulometeoro.png")
        self.rect = self.formato_geometrico.get_rect()
        self.mask = pygame.mask.from_surface(self.formato_geometrico)
        self.altura = 40
        self.__recompensa = random.randint(0,10)
        self.rect.x = posicoesx[random.randint(0,len(posicoesx)-1)]
        self.rect.y = random.randint(-500,-10)

    @property
    def recompensa(self):
        return self.__recompensa

    @recompensa.setter
    def recompensa(self, recompensa):
        self.__recompensa = recompensa
    
    def movimento(self, inimigos, altura):
        if self.rect.y < altura+10:
            self.rect.y += self.velocidade
        else:
            inimigos.remove(self)
