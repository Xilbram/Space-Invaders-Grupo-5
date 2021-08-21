import JogadorNave

#Ainda não implementada
class Loja:
    def __init__(self, jogador:JogadorNave.Jogador):
        self.jogador = jogador
        self.__pontos_jogador = self.jogador.poder_de_compra()


    #defini o preço de compra para 50 de escudo como 500 pontos, pode ser alterado
    def comprar_escudo(self):
        if self.__pontos_jogador >= 500:
            self.jogador.escudo += 50

    #defini o preço para aumentar o dano em 25 como 750 pontos, pode ser alterado
    def aumentar_dano(self):
        if self.__pontos_jogador >= 750:
            self.jogador.dano += 25

    #defini o preço para aumentar a velocidade em 2 como 500 pontos, pode ser alterado
    def aumentar_velocidade(self):
        if self.__pontos_jogador >= 500:
            self.jogador.velocidade += 2