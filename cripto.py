from binance.client import Client
from secret import api_key, api_secret
import re


class Ativo:

    def __init__(self, nome):
        self.__nome = nome
        self.__valor_compra = self.valor_compra()
        self.__quantidade = self.quantidade_comprada()

    def __str__(self):
        return f'Nome: {self.nome} Valor Compra: {self.valor_compra()} Total: {self.total_compra()}'

    @property
    def nome(self):

        return str(self.__nome)

    def valor_compra(self):

        if len(self.nome) >= 6:
            cliente = Client(api_key, api_secret)
            dados_completo_ativo_carteira = cliente.get_my_trades(symbol=self.nome)
            preco_compra = dados_completo_ativo_carteira[-1]['price']

            return float(preco_compra)

    def quantidade_comprada(self):

        if len(self.nome) >= 6:
            cliente = Client(api_key, api_secret)
            dados_completo_ativo_carteira = cliente.get_my_trades(symbol=self.nome)
            quantidade = dados_completo_ativo_carteira[-1]['qty']

            return float(quantidade)

    def total_compra(self):
        return self.quantidade_comprada() * self.valor_compra()


if __name__ == '__main__':
    nome = 'ADABRL'
    ativo = Ativo(nome)
    print(ativo)


