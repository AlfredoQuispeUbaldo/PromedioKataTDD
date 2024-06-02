def calcular_promedio_ponderado(numeros, pesos):
    if not numeros or not pesos:
        raise ValueError("Las listas de números y pesos no pueden estar vacías.")
    if len(numeros) != len(pesos):
        raise ValueError("Las listas de números y pesos deben tener la misma longitud.")
    if any(p <= 0 for p in pesos):
        raise ValueError("Los pesos deben ser positivos.")

    suma_ponderada = sum(n * p for n, p in zip(numeros, pesos))
    suma_pesos = sum(pesos)
    return suma_ponderada / suma_pesos