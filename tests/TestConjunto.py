import unittest
from src.logica.Conjunto import calcular_promedio_ponderado

class TestConjunto(unittest.TestCase):
    def test_promedio_ponderado_cp0(self):
        numeros = [10, 12, 14]
        pesos = [3, 4, 2]
        resultado_esperado = 11.78
        self.assertAlmostEqual(calcular_promedio_ponderado(numeros, pesos), resultado_esperado, places=2)

    def test_promedio_ponderado_cp1(self):
        numeros = [15, 15, 17]
        pesos = [3, 4, 2]
        resultado_esperado = 15.44
        self.assertAlmostEqual(calcular_promedio_ponderado(numeros, pesos), resultado_esperado, places=2)

    def test_pesos_contienen_cero(self):
        numeros = [10, 20, 30]
        pesos = [0, 1, 1]
        with self.assertRaises(ValueError):
            calcular_promedio_ponderado(numeros, pesos)

    def test_listas_diferentes_longitudes(self):
        numeros = [10, 20]
        pesos = [1]
        with self.assertRaises(ValueError):
            calcular_promedio_ponderado(numeros, pesos)

    def test_lista_numeros_vacia(self):
        numeros = []
        pesos = [1, 2, 3]
        with self.assertRaises(ValueError):
            calcular_promedio_ponderado(numeros, pesos)

    def test_lista_pesos_vacia(self):
        numeros = [10, 20, 30]
        pesos = []
        with self.assertRaises(ValueError):
            calcular_promedio_ponderado(numeros, pesos)

if __name__ == '__main__':
    unittest.main()