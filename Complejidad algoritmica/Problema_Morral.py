def morral(tamano_morral, pesos, valores, n):

    if n == 0 or tamano_morral == 0:
        return 0

    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n - 1)
    a=valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1)
    b=morral(tamano_morral, pesos, valores, n - 1)
    return max(a,b)
                


if __name__ == '__main__':
    valores = [60, 100, 40]
    pesos = [30, 10, 20]
    tamano_morral = 50
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)