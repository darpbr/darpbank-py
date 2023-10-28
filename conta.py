class Conta:

    def __init__(self, numero, titular, saldo, limite=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print('Saldo R$ {} do titular {}'.format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        if (self.saldo + self.limite) >= valor:
            self.saldo -= valor
        else:
            print('Saldo insuficiente para sacar! Saldo: R$ {} + limite: R$ {}'.format(self.saldo,self.limite))