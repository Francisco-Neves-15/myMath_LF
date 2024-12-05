@staticmethod
def myFibonacci(n: int, resultType: str.lower):
    answer = [0, 1]
    for i in range(2, n + 1):
        answer.append(answer[i - 1] + answer[i - 2])

    if resultType == "all":
        return answer
    elif resultType == "my":
        return answer[n]
    elif resultType == "both":
        return answer, answer[n]
    else:
        return "entry error"

@staticmethod
def myList_primes_up_to(limit: int):
    def is_prime(num):
        if num < 2:
            return False
        for x in range(2, int(num**0.5) + 1):
            if num % x == 0:
                return False
        return True

    return [num for num in range(2, limit + 1) if is_prime(num)]

@staticmethod
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