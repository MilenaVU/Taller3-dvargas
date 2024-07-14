import unittest
from Animal import Huron, Boa_Constrictor

class TestHurones(unittest.TestCase):
    def setUp(self):
        self.huron = Huron("Huron", 5, "Colombia", 10)

    def test_hacer_sonido(self):
        self.assertEqual(self.huron.hacer_sonido(), "¡Eek Eek!")

    def test_calcular_flete(self):
        self.assertEqual(self.huron.calcular_flete(), 50.0)

class TestBoasConstrictor(unittest.TestCase):
    def setUp(self):
        self.boa = Boa_Constrictor("Boa", 20, "Brasil", 15)

    def test_hacer_sonido(self):
        self.assertEqual(self.boa.hacer_sonido(), "¡Tsss!")

    def test_calcular_flete(self):
        self.assertEqual(self.boa.calcular_flete(), 300.0)

    def test_alimentar(self):
        for _ in range(10):
            self.boa.alimentar()
        with self.assertRaises(ValueError):
            self.boa.alimentar()

if __name__ == '__main__':
    unittest.main()
