import pygame
import os
import time
import random
import HUD


class Jogo:
    def __init__(self):
        self.is_rodando = True
        self.is_pausado = False
        self.tempo_fase = 0
        self.FPS = 0
        self.tempo = pygame.time.Clock()
        self.hud = HUD.HUD()

    def pausar(self):
        self.is_pausado = True

    def despausar(self):
        self.is_pausado = False

    def loop_jogo(self):
        while self.is_rodando:
            self.tempo.tick(self.FPS)
            self.hud.mostrar_fundo()
            self.hud.mostrar_nivel()
            self.hud.mostrar_vida()
            pygame.display.update()

            #sair do jogo quando usuario quitar
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_rodando = False



jogo1 = Jogo()
jogo1.loop_jogo()




