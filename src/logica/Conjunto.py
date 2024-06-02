def calcular_promedio_ponderado(numeros, pesos):
    if len(numeros) != len(pesos):
        raise ValueError("Las listas de números y pesos deben tener la misma longitud.")
    if len(numeros) == 0 or len(pesos) == 0:
        raise ValueError("Las listas de números y pesos no pueden estar vacías.")
    if any(p == 0 for p in pesos):
        raise ValueError("Los pesos no pueden contener valores cero.")

    suma_ponderada = sum(n * p for n, p in zip(numeros, pesos))
    suma_pesos = sum(pesos)
    return suma_ponderada / suma_pesos