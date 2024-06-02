def calcular_promedio_ponderado(numeros, pesos):
    suma_ponderada = sum(n * p for n, p in zip(numeros, pesos))
    suma_pesos = sum(pesos)
    return suma_ponderada / suma_pesos