import unittest
from conta import ContaBancaria


class TestContaBancaria(unittest.TestCase):

    def setUp(self):
        # Cria uma nova conta antes de CADA teste (estado limpo)
        self.conta = ContaBancaria("Ana", saldo_inicial=100.0)

    def test_depositar_incrementa_saldo(self):
        self.conta.depositar(50.0)       # Act
        self.assertEqual(self.conta.saldo, 150.0)  # Assert

    def test_sacar_decrementa_saldo(self):
        self.conta.sacar(40.0)
        self.assertEqual(self.conta.saldo, 60.0)

    def test_sacar_maior_que_saldo_lanca_erro(self):
        with self.assertRaises(ValueError):
            self.conta.sacar(999.0)

    def test_depositar_valor_invalido_lanca_erro(self):
        for invalido in [0, -10]:
            with self.subTest(valor=invalido):
                with self.assertRaises(ValueError):
                    self.conta.depositar(invalido)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)