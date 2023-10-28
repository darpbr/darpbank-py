class Conta:

    def __init__(self, numero, titular, saldo, limite=0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    @property
    def limite(self):
        return self.__limite
    
    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB':'001','Caixa':'104','Bradesco':'237'}
    
    def extrato(self):
        print('Saldo R$ {} do titular {}'.format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor
    
    def __pode_sacar_transferir(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel
    
    def saca(self, valor):
        if self.__pode_sacar_transferir(valor):
            self.__saldo -= valor
        else:
            print('Saldo insuficiente para sacar! Saldo: R$ {} + limite: R$ {}'.format(self.__saldo,self.__limite))
    
    def transfere(self, conta_destino, valor):
        if self.__pode_sacar_transferir:
            conta_destino.deposita(valor)
        else:
            print('Saldo insuficiente para realizar transferência!')
    
    def __str__(self):
        return 'Número: {}, Titular: {}, Saldo: {}'.format(self.__numero, self.__titular, self.__saldo)