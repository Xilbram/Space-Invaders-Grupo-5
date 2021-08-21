import pygame
import os
from Tiro import Tiro

class Jogador(pygame.sprite.Sprite):
    def __init__(self,posicao,limite_x: int, limite_y: int, velocidade: int, vida: 100, valor_meteoro, valor_nave_inimiga):
        super().__init__()
        self.image = pygame.image.load('Ship_Player_PNG_01.png')
        self.rect = self.image.get_rect(midbottom = posicao)
        self.__velocidade = velocidade
        self.__posicao = posicao
        self.__limite_x = limite_x
        self.__limite_y = limite_y
        self.__tiro_pronto = True
        self.__tiro_temporizador = 0
        self.__cooldown_tiro = 600
        self.tiros = pygame.sprite.Group()
        self.__vida = vida
        self.__dano = 25
        self.__meteoros_destruidos = 0
        self.__naves_destruidas = 0
        self.__escudo = 0
        self.__valor_meteoro = valor_meteoro
        self.__valor_nave_inimiga = valor_nave_inimiga
        #self.__velocidade_tiro = Tiro.velocidade #Não precisa desse atributo

    @property
    def escudo(self):
        return self.__escudo
    @escudo.setter
    def escudo(self, escudo_valor):
        self.__escudo = escudo_valor
    @property
    def dano(self):
        return self.__dano
    @dano.setter
    def dano(self, valor_dano):
        self.__dano = valor_dano
    @property
    def posicao(self):
        return self.__posicao
    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao
    @property
    def velocidade(self):
        return self.__velocidade
    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade
    @property
    def valor_meteoro(self):
        return self.__valor_meteoro
    @valor_meteoro.setter
    def valor_meteoro(self, valor_meteoro):
        self.__valor_meteoro = valor_meteoro
    @property
    def valor_nave_inimiga(self):
        return self.__valor_nave_inimiga
    @valor_nave_inimiga.setter
    def valor_nave_inimiga(self,valor_nave_inimiga):
        self.__valor_nave_inimiga = valor_nave_inimiga
    @property
    def vida(self):
        return self.__vida
    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    def poder_de_compra(self):
        pontos = (self.__naves_destruidas * self.__valor_nave_inimiga) + (self.__meteoros_destruidos* self.__valor_nave_inimiga)
        return pontos

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += self.__velocidade
        elif keys[pygame.K_a]:
            self.rect.x -= self.__velocidade
        elif keys[pygame.K_w]:
            self.rect.y -= self.__velocidade
        elif keys[pygame.K_s]:
            self.rect.y += self.__velocidade

        #tiro
        if keys[pygame.K_SPACE] and self.__tiro_pronto:
            self.atirar()
            self.__tiro_pronto = False
            self.__tiro_temporizador = pygame.time.get_ticks()

    def recarregar(self):
        if not self.__tiro_pronto:
            momento = pygame.time.get_ticks()
            if momento - self.__tiro_temporizador >= self.__cooldown_tiro:
                self.__tiro_pronto = True

    def atirar(self):
        self.tiros.add(Tiro(self.rect.center, -6, self.rect.bottom))

    def limite_x(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.__limite_x:
            self.rect.right = self.__limite_x

    def limite_y(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.__limite_y:
            self.rect.bottom = self.__limite_y

    def colisao(self, grupo1, grupo2):
        return pygame.sprite.groupcollide(grupo1, grupo2, False, True, pygame.sprite.collide_mask)

    def update(self):
        self.get_input()
        self.limite_x()
        self.limite_y()
        self.recarregar()
        self.tiros.update()