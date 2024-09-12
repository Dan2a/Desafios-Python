import math

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

# Calcular a distância entre os dois pontos usando a biblioteca MATH
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# Calcular a distância entre os dois pontos sem a função sqrt()
# distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Exibir o resultado com 4 casas decimais
print(f"{distancia:.4f}")