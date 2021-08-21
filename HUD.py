import os
import pygame
pygame.font.init()
from JogadorNave import Jogador


class HUD(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.fonte_letreiros = pygame.font.SysFont('comicssans',25)
        self.__largura_janela = 800
        self.__altura_janela = 600
        self.janela = pygame.display.set_mode((self.__largura_janela, self.__altura_janela))
        self.tempo_fase = 0
        self.fundo_tela = pygame.transform.scale(pygame.image.load('space_background.jpg'), (self.__largura_janela, self.__altura_janela))
        self.display_jogo = pygame.display.set_mode((self.__largura_janela,self.__altura_janela))

    @property
    def altura_tela(self):
        return self.__altura_janela
    @altura_tela.setter
    def altura_tela(self, altura):
        self.__altura_janela = altura
    @property
    def largura_tela(self):
        return self.__largura_janela
    @largura_tela.setter
    def largura_tela(self, largura):
        self.__largura_janela = largura


    #calculo da posição X de onde mostrar a vida é baseado no tamanho da largura da janela, então não tem problema mexer na altura/largura
    def mostrar_nivel(self, nivel):
        nivel_atual_display = self.fonte_letreiros.render("Nível: {}".format(nivel), True, (255,255,255))
        return self.janela.blit(nivel_atual_display, (self.__largura_janela - nivel_atual_display.get_width(), 10))

    #to tentando mesclar o que eu fiz com o da Mariana, pq o dela tem verificação de inserção
    #def mostrar_vida(self, jogador: Jogador):
        #if isinstance(jogador, Jogador):
            #vida_jogador_display = self.fonte_letreiros.render("Vida {}".format(jogador), True, (255, 0, 0))
            #return self.janela.blit(vida_jogador_display, (0, 10))

    def mostrar_vida(self, jogador: Jogador):
        if isinstance(jogador, Jogador):
            fonte = pygame.font.SysFont('comic sans', 30)
            mensagem = fonte.render("Vida: " + str(jogador.vida), True, (255, 0,0))
            self.display_jogo.blit(mensagem, (0, 10))

    def mostrar_tempo(self, tempo_tela, contagem):
        fonte = pygame.font.SysFont('comic sans', 30)
        mensagem = fonte.render("Tempo: " + str(tempo_tela - int(contagem)), True, (255, 255, 255))
        self.display_jogo.blit(mensagem, (100, 10))

    def mostrar_inimigos_restantes(self, qtd_inimigos):
        fonte = pygame.font.SysFont('comic sans', 30)
        mensagem = fonte.render("Inimigos: " + str(qtd_inimigos), True, (255, 255, 255))
        self.display_jogo.blit(mensagem, (220, 10))

    def mostrar_fundo(self):
        return self.janela.blit(self.fundo_tela, (0, 0))