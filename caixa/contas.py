import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

class Conta:

    def __init__(self, cliente, numero, saldo=0):

        self.cliente = cliente
        self.numero = numero
        self.saldo = saldo

        self.operacoes = []

        self.id = id

    def resumo(self):
        print("CC numero: %s Saldo: %10.2f" % (self.numero, self.saldo))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else:
            print("Senhor %s Valor não suficiente, seu saldo é :%10.2f" %
                  (self.cliente.nome, self.saldo))

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPOSITO", valor])

    def extrato(self):
        print("Extrato CC n %s\n" % self.numero)
        for o in self.operacoes:
            print("%10s %10.2f\n" % (o[0], o[1]))
        print("\n   Saldo: %10.2f\n" % self.saldo)






    def localizar_cliente(self, id):
        r = self.db.cursor.execute(
            'SELECT * FROM clientes WHERE id = ?', (id,))
        return r.fetchone()

    def imprimir_cliente(self, id):
        if self.localizar_cliente(id) == None:
            return print('Não existe cliente com o id informado.')
        else:
             return print(self.localizar_cliente(id))
