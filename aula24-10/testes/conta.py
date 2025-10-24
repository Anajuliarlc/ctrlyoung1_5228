class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = float(saldo_inicial)

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor do depósito deve ser positivo.")
        self.saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor do saque deve ser positivo.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= valor