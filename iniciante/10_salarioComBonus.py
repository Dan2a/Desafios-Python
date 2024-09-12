nome = input()
salario = float(input())
vendas = float(input())

comisão = vendas * 0.15
total = salario +  comisão

print(f'TOTAL = R$ {total:.2f}')