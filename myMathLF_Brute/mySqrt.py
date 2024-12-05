def mySqrt(x: float, epsilon=1e-6):
    if x < 0:
        # Para números negativos, calculamos o módulo de x e adicionamos 'j' para indicar a raiz imaginária
        x = abs(x)
        L, R = (0, x) if x >= 1 else (x, 1)
        while (R - L) > epsilon:
            M = (L + R) / 2
            M_squared = M * M
            if abs(M_squared - x) < epsilon:
                return complex(0, M)  # Retorna a raiz imaginária
            elif M_squared < x:
                L = M
            else:
                R = M
        return complex(0, (L + R) / 2)  # Retorna o ponto médio como raiz imaginária

    # Para números não-negativos, mantém o cálculo usual
    L, R = (0, x) if x >= 1 else (x, 1)
    while (R - L) > epsilon:
        M = (L + R) / 2
        M_squared = M * M
        if abs(M_squared - x) < epsilon:
            return M
        elif M_squared < x:
            L = M
        else:
            R = M

    return (L + R) / 2

user_input = float(input("Type a number: "))
print(mySqrt(user_input))