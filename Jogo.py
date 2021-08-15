import pygame
import os
import time
import random
import HUD
from JogadorNave import Jogador


class Jogo:
    def __init__(self):
        self.is_rodando = True
        self.is_pausado = False
        self.tempo_fase = 0
        self.FPS = 60
        self.tempo = pygame.time.Clock()
        self.hud = HUD.HUD()
        self.jogador = Jogador((self.hud.largura_tela/2,self.hud.altura_tela),self.hud.largura_tela, self.hud.altura_tela, 5, 100, 0, 0)
        jogador_sprite = Jogador((self.hud.largura_tela/2,self.hud.altura_tela),self.hud.largura_tela, self.hud.altura_tela, 5, 100, 0, 0)
        self.jogador_sprite = pygame.sprite.GroupSingle(jogador_sprite)

    def pausar(self):
        self.is_pausado = True

    def despausar(self):
        self.is_pausado = False

    def loop_jogo(self):
        while self.is_rodando:
            self.tempo.tick(self.FPS)
            self.hud.mostrar_fundo()
            self.hud.mostrar_nivel(1)
            self.hud.mostrar_vida(self.jogador.vida)
            self.jogador_sprite.update()
            self.jogador_sprite.draw(surface=self.hud.janela)
            self.jogador_sprite.sprite.tiros.draw(self.hud.janela)
            pygame.display.update()


            #sair do jogo quando usuario quitar
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_rodando = False



jogo1 = Jogo()
jogo1.loop_jogo()



