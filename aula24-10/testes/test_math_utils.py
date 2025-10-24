import unittest
from math_utils import somar, eh_par

class TestMathUtils(unittest.TestCase):
    def test_somar_basico(self):
        # Arrange & Act
        resultado = somar(2, 2)
        # Assert
        self.assertEqual(resultado, 4)
        self.assertNotEqual(resultado, 5)

    def test_eh_par_exemplos(self):
        # Várias entradas em um único teste
        for n, esperado in [(0, True), (1, False), (2, True), (-3, False)]:
            with self.subTest(n=n):
                self.assertEqual(eh_par(n), esperado)

    def test_asserts_varios(self):
        numeros = [1, 2, 3]
        self.assertTrue(eh_par(2))
        self.assertFalse(eh_par(3))
        self.assertIn(2, numeros)
        self.assertNotIn(4, numeros)

if __name__ == '__main__':
    # Em ambientes interativos (ex.: Jupyter), use:
    unittest.main(argv=[''], exit=False)
    # Em scripts normais, pode ser apenas: unittest.main()