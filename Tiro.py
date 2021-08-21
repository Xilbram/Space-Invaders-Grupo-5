import pygame

class Tiro(pygame.sprite.Sprite):
    def __init__(self, posicao, velocidade, tamanho_janela):
        super().__init__()
        self.image = pygame.Surface((4,20))
        self.image.fill('white')
        self.rect = self.image.get_rect(center = posicao)
        self.__velocidade = velocidade
        self.tamanho_janela = tamanho_janela

    def destruir(self):
        if self.rect.y <= -50 or self.rect.y >= self.tamanho_janela + 50:
            self.kill()

    def update(self):
        self.rect.y += self.__velocidade
        self.destruir()

    @property
    def velocidade(self):
        return self.__velocidade