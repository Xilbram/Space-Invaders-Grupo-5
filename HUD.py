import os
import pygame
from abc import ABC
import time
pygame.font.init()


class HUD(ABC):
    def __init__(self):
        #vida e nível não serão definidos aqui, mas deixei assim para testar
        self.vida_jogador = 5
        self.nivel = 1
        #fonte como arial não é definitivo, só teste
        self.fonte_letreiros = pygame.font.SysFont('Arial',25)
        self.largura_janela = 800
        self.altura_janela = 600
        self.janela = pygame.display.set_mode((self.largura_janela, self.altura_janela))
        self.tempo_fase = 0
        self.fundo_tela = pygame.transform.scale(pygame.image.load(os.path.join('Imagens/space_background.jpg')), (self.largura_janela,self.altura_janela))

    #calculo da posição X de onde mostrar a vida é baseado no tamanho da largura da janela, então não tem problema mexer na altura/largura
    def mostrar_nivel(self):
        nivel_atual_display = self.fonte_letreiros.render("Nível: {}".format(self.nivel), True, (255,255,255))
        return self.janela.blit(nivel_atual_display, (self.largura_janela - nivel_atual_display.get_width(), 5))

    def mostrar_vida(self):
        vida_jogador_display = self.fonte_letreiros.render("Vidas: {}".format(self.vida_jogador), True, (255,0,0))
        return self.janela.blit(vida_jogador_display, (10,5))

    def mostrar_tempo(self):
        pass

    def mostrar_inimigos_restantes(self):
        pass

    def mostrar_fundo(self):
        return self.janela.blit(self.fundo_tela, (0,0))