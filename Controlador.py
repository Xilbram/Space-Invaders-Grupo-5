from JogadorNave import Jogador
from HUD import HUD
import pygame
from pygame.locals import *
import sys

class ControladorNivel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def fim_de_jogo(self, jogador: Jogador, hud: HUD):
        if isinstance(jogador, Jogador) and isinstance(hud, HUD):
            jogador.vida = 100
            jogador.rect.center = (hud.largura_tela/2, hud.altura_tela-100)
        
        fonte_letreiros = pygame.font.SysFont('comicssans',100)
        fim_jogo = fonte_letreiros.render("Fim de jogo", True, (255,255,255))
        hud.janela.blit(fim_jogo, (hud.largura_tela/4, hud.altura_tela/2))

        morreu = True

        while morreu:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    morreu = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()