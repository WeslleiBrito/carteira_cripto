from cripto import Client, api_key, api_secret


class My_account:

    def __init__(self):
        self.__dados = self.minhas_cryptos()

    @property
    def dados(self):
        return self.__dados

    def __str__(self):
        return f'{self.minhas_cryptos()}'

    @staticmethod
    def consulta_dados_conta():
        cliente = Client(api_key, api_secret)
        dados = cliente.get_account()
        return dados

    def minhas_cryptos(self):
        moedas = self.consulta_dados_conta()
        lista_moeda = []
        for moeda in moedas['balances']:
            if float(moeda['free']) >= 1.0:
                par = (moeda['asset'], float(moeda['free']))
                lista_moeda.append(par)

        return lista_moeda

    def moedas(self):
        lista = self.minhas_cryptos()
        moedas = []
        for nome in lista:
            if len(nome[0]) > 3:
                moedas.append((nome[0], nome[1]))
            else:
                moedas.append((nome[0], nome[1]))

        return moedas

    def saldo(self):
        cliente = Client(api_key, api_secret)
        nome = self.moedas()
        for nome in moedas:
            valor = cliente.get_recent_trades(symbol=nome+'BRL')


if __name__ == '__main__':
    conta = My_account()
    print(conta)
    print(conta.moedas())
