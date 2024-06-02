import unittest
from src.logica.Conjunto import calcular_promedio_ponderado

class TestConjunto(unittest.TestCase):
    def test_promedio_ponderado_cp0(self):
        numeros = [10, 12, 14]
        pesos = [3, 4, 2]
        resultado_esperado = 11.78
        self.assertAlmostEqual(calcular_promedio_ponderado(numeros, pesos), resultado_esperado, places=2)

if __name__ == '__main__':
    unittest.main()