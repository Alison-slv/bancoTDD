class Banco:
    _numeroContas = 1000000
    def __init__(self):
        self.contas = {}
        self.historicos = {}

    def abrirConta(self, usuario, senha):
        if senha and usuario:
            for k in self.contas:
                if k == self._numeroContas:
                    raise ValueError("ja existe outra conta com este numero")
                    break
            self.contas.update({
                self._numeroContas: {
                    "cliente": usuario.nome,
                    "cpf": usuario.cpf,
                    "senha": senha,
                    "saldo": 0,
            }})
            self.historicos.update({self._numeroContas: []})
            self._numeroContas += 1

    def depositar(self, numeroConta, valor):
        if valor > 0:
            self.contas[numeroConta]["saldo"] += valor
            self.historicos[numeroConta].append(f"depoisto de {valor}")
        else:
            raise ValueError("valor incorreto! correto seria maior que 0")

    def sacar(self, numeroConta, senha, valor):
        if valor > 0:
            if senha == self.contas[numeroConta]["senha"] == senha:
                self.contas[numeroConta]["saldo"] -= valor
                self.historicos[numeroConta].append(f"saque de {valor}")
            else:
                raise Exception("senha incorreta")
        else:
            raise ValueError("valor precisa ser maior que zero")

    def historico(self, numeroConta, senha):
        if senha == self.contas[numeroConta]["senha"]:
            if self.historicos[numeroConta]:
                for h in self.historicos[numeroConta]:
                    print(f"-- {h}")
        else:
            raise Exception("senha incorreta")