a, b, c = map(int, input().split())

# função abs() em Python retorna o valor absoluto de um número retirando os sinais
maior_ab = (a + b + abs(a - b)) // 2
maior_abc = (maior_ab + c + abs(maior_ab - c)) // 2

print(f"{maior_abc} eh o maior")