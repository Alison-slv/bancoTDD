from banco import Banco
from cliente import Cliente

import pytest

class TestBanco:
    def testSeNumeroDeContasIncrementaAoAbrirNovaConta(self):
        banco = Banco()
        cliente = Cliente("CliemteOne", "111.111.111-00")
        senha = "cliente1"
        banco.abrirConta(cliente, senha)
        assert banco._numeroContas == 1000001

    def testAoAbrirNovaContaSaldoSejaZero(self):
        banco = Banco()
        cliente = Cliente("ClienteOne", "111.111.111-11")
        senha = "cliente1"
        banco.abrirConta(cliente, senha)
        numeroContaAtual = banco._numeroContas - 1
        assert banco.contas[numeroContaAtual]["saldo"] == 0


    def testDepositarDinheiroNaContaSaldoAumenta(self):
        banco = Banco()
        valor = 500
        cliente = Cliente("cli1", "000.000.000-00")
        banco.abrirConta(cliente, "1234")
        numeroConta = banco._numeroContas - 1
        banco.depositar(numeroConta, valor)
        assert banco.contas[numeroConta]["saldo"] == valor

    def testDepositarValorInferiorAZeroRecebeErro(self):
        banco = Banco()
        valor = -1
        cliente = Cliente("cli2", "222.222.222-00")
        banco.abrirConta(cliente, "semha")
        numeroConta = banco._numeroContas - 1
        with pytest.raises(ValueError):
            banco.depositar(numeroConta, valor)

    def testAbrirContaComNumeroContasJaExistenteRecebeErro(self):
        banco = Banco()
        c1 = Cliente("cli1", "111.111.111-11")
        c2 = Cliente("cli1", "222.222.222-22")
        banco.abrirConta(c1, "senha1") # numero conta 1000000
        banco._numeroContas = 1000000
        with pytest.raises(ValueError):
            banco.abrirConta(c2, "senha2")

    def testFazerUmSaqueSubtrairaODinheiro(self):
        banco = Banco()
        c1 = Cliente("cli1", "333.333.333-33")
        banco.abrirConta(c1, "senha1")
        numeroConta = banco._numeroContas - 1
        banco.depositar(numeroConta, 1000)
        banco.sacar(numeroConta, "senha1", 600)
        assert banco.contas[numeroConta]["saldo"] == 400

    def testFazerUmSaqueComSenhaIncorreta(self):
        banco = Banco()
        c1 = Cliente("cli1", "333.333.333-33")
        banco.abrirConta(c1, "senha1")
        numeroConta = banco._numeroContas - 1
        banco.depositar(numeroConta, 1000)
        with pytest.raises(Exception):
            banco.sacar(numeroConta, "senha2", 600)

    def testTentarSacarComValorNegativo(self):
        banco = Banco()
        c1 = Cliente("cli1", "555.555.555-55")
        banco.abrirConta(c1, "senha")
        numeroConta = banco._numeroContas - 1
        banco.depositar(numeroConta, 100)
        with pytest.raises(ValueError):
            banco.sacar(numeroConta, "senha", -1)

    def testSeAoMexerNaContaColocaNoHistorico(self):
        banco = Banco()
        c1 = Cliente("cliente", "888.999.000-11")
        banco.abrirConta(c1, "senha")
        numeroConta = banco._numeroContas - 1
        banco.depositar(numeroConta, 100)
        banco.sacar(numeroConta, "senha", 50)
        assert len(banco.historicos[numeroConta]) == 2

    def testTentarAcessarHistoricoDeUmaContaComSenhaErradaRecebeErro(self):
        banco = Banco()
        c1 = Cliente("cliente", "111.111.111-11")
        banco.abrirConta(c1, "senhaCerta")
        numeroConta = banco._numeroContas - 1
        with pytest.raises(Exception):
            banco.historico(numeroConta, "senhaErrada")