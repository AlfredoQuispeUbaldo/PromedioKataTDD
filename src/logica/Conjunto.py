def calcular_promedio_ponderado(numeros, pesos):
    if len(numeros) != len(pesos):
        raise ValueError("Las listas de números y pesos deben tener la misma longitud.")

    suma_ponderada = sum(n * p for n, p in zip(numeros, pesos))
    suma_pesos = sum(pesos)
    return suma_ponderada / suma_pesos