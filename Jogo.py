from Controlador import ControladorNivel
from Inimigo import Inimigo
import pygame
import os
import time
import random
import HUD
from JogadorNave import Jogador
from Inimigo import *


class Jogo:
    def __init__(self):
        self.is_rodando = True
        self.is_pausado = False
        self.tempo_fase = 0
        self.tempo_maximo = 240
        self.nivel = 0
        self.FPS = 60
        self.tempo = pygame.time.Clock()
        self.hud = HUD.HUD()
        self.jogador = Jogador((self.hud.largura_tela/2,self.hud.altura_tela),self.hud.largura_tela, self.hud.altura_tela, 5, 100, 0, 0)
        #jogador_sprite = self.jogador #Não precisa escrever tudo de novo, pode só colocar self.jogador em baixo
        self.jogador_sprite = pygame.sprite.GroupSingle(self.jogador)
        self.inimigo_sprite = pygame.sprite.Group()
        self.controle = ControladorNivel()

    def pausar(self):
        self.is_pausado = True

        while self.is_pausado:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                            self.is_pausado = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.is_rodando = False

    #Não precisa desse método, pode despausar no próprio pausar
    # def despausar(self):
    #     self.is_pausado = False

    def loop_jogo(self):
        while self.is_rodando:
            self.tempo.tick(self.FPS)
            self.hud.mostrar_fundo()
            self.hud.mostrar_nivel(self.nivel)
            self.hud.mostrar_vida(self.jogador) #.vida já está em HUD
            self.hud.mostrar_inimigos_restantes(len(self.inimigo_sprite))
            self.hud.mostrar_tempo(self.tempo_maximo, self.tempo_fase)
            self.jogador_sprite.update()
            self.jogador_sprite.draw(surface=self.hud.janela)
            self.jogador_sprite.sprite.tiros.draw(self.hud.janela)


            #sair do jogo quando usuario quitar
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pausar()
                if event.type == pygame.QUIT:
                    self.is_rodando = False

            if len(self.inimigo_sprite) == 0:
                self.nivel += 1
                self.tempo_fase = 0
                #Coloquei quantidade e tipo de inimigos aleatórios por fase
                #Se preferirem, a gente pode deixar definido
                for _ in range(0,(self.nivel*2)+3):
                    escolha_inimigo = random.randint(1,3)
                    if escolha_inimigo == 1:
                        novo_inimigo = NaveComum(self.hud.largura_tela)
                    elif escolha_inimigo == 2:
                        novo_inimigo = Kamikaze(self.hud.largura_tela)
                    else:
                        novo_inimigo = Meteoro()
                    self.inimigo_sprite.add(novo_inimigo)

            for inimigo in self.inimigo_sprite:
                inimigo.geracao(self.hud.janela)
                if isinstance(inimigo, Meteoro):
                    inimigo.movimento(self.inimigo_sprite, self.hud.altura_tela)
                else:
                    inimigo.tiro_temporizador += 1/self.FPS
                    if isinstance(inimigo, Kamikaze):
                        inimigo.movimento(self.inimigo_sprite, self.hud.altura_tela)
                    
                    else:
                        inimigo.movimento()
                    inimigo.disparar(self.hud.altura_tela)
                    inimigo.tiros.draw(self.hud.janela)
                    inimigo.tiros.update()
                    if self.jogador.colisao(self.jogador_sprite, inimigo.tiros):
                        self.jogador_sprite.sprite.vida -= inimigo.dano
            
            #Criei um método de colisão p/ jogador
            #Caso queira adicionar:
            #def colisao(self, grupo1, grupo2):
                #return pygame.sprite.groupcollide(grupo1, grupo2, False, True, pygame.sprite.collide_mask)
            
            for inimigo_acertado in self.jogador.colisao(self.inimigo_sprite, self.jogador.tiros):
                inimigo_acertado.vida -= self.jogador_sprite.sprite.dano
                if inimigo_acertado.vida == 0:
                    self.inimigo_sprite.remove(inimigo_acertado)

            for inimigo_colidido in self.jogador.colisao(self.jogador_sprite, self.inimigo_sprite).values():
                if isinstance(inimigo_colidido[0], Kamikaze):
                    inimigo_colidido[0].explodir(self.jogador)
                    self.jogador.vida -= inimigo_colidido[0].dano_explosao
                elif isinstance(inimigo_colidido[0], NaveComum) or isinstance(inimigo_colidido[0], Meteoro):
                    self.jogador.vida -= inimigo_colidido[0].dano * 2
            
            if self.tempo_fase >= self.tempo_maximo or self.jogador.vida <= 0:
                self.nivel = 0
                self.jogador.tiros.empty()
                self.inimigo_sprite.empty()
                self.controle.fim_de_jogo(self.jogador, self.hud)

            self.tempo_fase += 1/self.FPS
            pygame.display.update()

jogo1 = Jogo()
jogo1.loop_jogo()