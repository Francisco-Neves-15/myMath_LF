from myMathLF import mySqrt
import numpy as np
import matplotlib.pyplot as plt

def getEntrys():
    a = int(input("Entry with 'a': "))
    b = int(input("Entry with 'b': "))
    c = int(input("Entry with 'c': "))
    return a, b, c

def getBhakara(a, b, delta):
    sqrtPre = delta
    sqrtTrue = mySqrt(sqrtPre)
    x1, x2 = -b + (sqrtTrue / (2*a)), -b - (sqrtTrue / (2*a))
    return x1, x2

def getDelta(a, b, c):
    delta = b**2 - (4*a*c)
    return delta

def getVertices(a, b, delta):
    yv, xv = -(delta / (4*a)), -b / (2*a)
    if a > 0:
        parabolaDirection = "u"
        valueType = "Minimum Value"
    elif a < 0:
        parabolaDirection = "∩"
        valueType = "Maximum Value"
    v = f"V({xv},{yv})"
    return v, xv, yv, parabolaDirection, valueType

def printThis(a, b, c, delta, x1, x2, v, xv, yv, valueType, parabolaDirection):
    print(f"'a': {a}")
    print(f"'b': {b}")
    print(f"'c': {c}")
    print(f"'Δ': {delta}")
    print(f"'x1','x2': {x1},{x2}")
    print(f"Direction of the Parabola: {parabolaDirection}")
    print(f"{valueType}: {v}")

# Função para plotar o gráfico da função quadrática
def plotQuadratic(a, b, c):
    # Cria um vetor de valores de x
    x = np.linspace(-10, 10, 400)  # Valores de x variando de -10 a 10
    y = a * x**2 + b * x + c  # A equação da função quadrática

    # Criação do gráfico
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'Y = {a}x² + {b}x + {c}')
    plt.title(f'f(x) = {a}x² + {b}x + {c}')
    plt.xlabel('x')
    plt.ylabel('y')
    
    # Marcando o vértice
    delta = b**2 - 4*a*c
    x_vertice = -b / (2 * a)
    y_vertice = -(delta / (4 * a))
    plt.scatter(x_vertice, y_vertice, color='red', zorder=5)
    plt.text(x_vertice, y_vertice, f'V({x_vertice:.2f},{y_vertice:.2f})', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
    
    # Mostrando o gráfico
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    a, b, c = getEntrys()
    delta = getDelta(a, b, c)
    x1, x2 = getBhakara(a, b, delta)
    v, xv, yv, parabolaDirection, valueType = getVertices(a, b, delta)
    printThis(a, b, c, delta, x1, x2, v, xv, yv, valueType, parabolaDirection)
    # Plotar o gráfico da função quadrática
    plotQuadratic(a, b, c)

if __name__ == "__main__":
    main()

# Exemplos de funções quadráticas:
# 1) Função com valor mínimo: y = 2x² + 3x - 5 (a > 0)
# 2) Função com valor mínimo: y = x² - 4x + 3 (a > 0)
# 3) Função com valor máximo: y = -2x² + 4x - 1 (a < 0)
# 4) Função com valor máximo: y = -x² + 6x - 9 (a < 0)