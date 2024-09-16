# CODIGO COM OBJETO
precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

codigo, quantidade = map(int, input().split())

if codigo in precos:
    total = precos[codigo] * quantidade
    print(f"Total: R$ {total:.2f}")
else:
    print("Código inválido")


# CODIGO SEM USAR OBJETO

# a, b = map(int, input().split())

# cachorroQuente = float(4)
# xSalada = float(4.5)
# xBacon = float(5)
# torradaSimples = float(2)
# refrigerante = float(1.5)

# if a == 1:
#     print(f'Total: R$ {b*cachorroQuente:.2f}')
# elif a == 2:
#     print(f'Total: R$ {b*xSalada:.2f}')
# elif a == 3:
#     print(f'Total: R$ {b*xBacon:.2f}')
# elif a == 4:
#     print(f'Total: R$ {b*torradaSimples:.2f}')
# else:
#     print(f'Total: R$ {b*refrigerante:.2f}')