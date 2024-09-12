N = float(input())

# Convertendo o valor de N para centavos
N = int(N * 100)

notas_100 = N // 10000
N = N % 10000
notas_50 = N // 5000
N = N % 5000
notas_20 = N // 2000
N = N % 2000
notas_10 = N // 1000
N = N % 1000
notas_5 = N // 500
N = N % 500
notas_2 = N // 200
N = N % 200
moedas_1 = N // 100
N = N % 100
moedas_50 = N // 50
N = N % 50
moedas_25 = N // 25
N = N % 25
moedas_10 = N // 10
N = N % 10
moedas_05 = N // 5
N = N % 5
moedas_01 = N

print("NOTAS:")
print(f"{notas_100} nota(s) de R$ 100.00")
print(f"{notas_50} nota(s) de R$ 50.00")
print(f"{notas_20} nota(s) de R$ 20.00")
print(f"{notas_10} nota(s) de R$ 10.00")
print(f"{notas_5} nota(s) de R$ 5.00")
print(f"{notas_2} nota(s) de R$ 2.00")

print("MOEDAS:")
print(f"{moedas_1} moeda(s) de R$ 1.00")
print(f"{moedas_50} moeda(s) de R$ 0.50")
print(f"{moedas_25} moeda(s) de R$ 0.25")
print(f"{moedas_10} moeda(s) de R$ 0.10")
print(f"{moedas_05} moeda(s) de R$ 0.05")
print(f"{moedas_01} moeda(s) de R$ 0.01")
