# Leitura do valor em segundos
temp = int(input())

# Calcular horas, minutos e segundos
horas = temp // 3600
temp = temp % 3600
minutos = temp // 60
segundos = temp % 60

# Exibir no formato horas:minutos:segundos
print(f"{horas}:{minutos}:{segundos}")
