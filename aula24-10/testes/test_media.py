import unittest
from media import media

class TestMedia(unittest.TestCase):
    def test_media_simples(self):
        self.assertEqual(media([2, 4, 6]), 4)

    def test_media_float(self):
        self.assertEqual(media([2.44, 3.87, 8.67]), 4.99)
        
    def test_media_um_elemento(self):
        self.assertEqual(media([10]), 10.00) 

    def test_media_lista_vazia(self):
        with self.assertRaises(ValueError):
            media([])

if __name__ == "__main__":
    unittest.main()