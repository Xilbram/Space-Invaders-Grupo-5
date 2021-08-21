import pygame
from pygame.locals import *
from Jogador import Jogador

display_largura = 750 
display_altura = 600
DisplayJogo = pygame.display.set_mode((display_largura,display_altura))

class HUD(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.fundo_tela = (0,0,0)
    
    def mostrar_vida(self, jogador: Jogador):
        if isinstance(jogador, Jogador):
            fonte = pygame.font.SysFont(None, 30)
            mensagem = fonte.render("Vida: "+str(jogador.vida), True, (255,255,255))
            DisplayJogo.blit(mensagem,(0,10))

    def mostrar_tempo(self, tempo_tela, contagem):
        fonte = pygame.font.SysFont(None, 30)
        mensagem = fonte.render("Tempo: "+str(tempo_tela-int(contagem)), True, (255,255,255))
        DisplayJogo.blit(mensagem,(90,10))

    def mostrar_inimigos_restantes(self, qtd_inimigos):
        fonte = pygame.font.SysFont(None, 30)
        mensagem = fonte.render("Inimigos: "+str(qtd_inimigos), True, (255,255,255))
        DisplayJogo.blit(mensagem,(210,10))

    def mostrar_fundo(self):
        DisplayJogo.fill(self.fundo_tela)