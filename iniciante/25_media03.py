n1, n2, n3, n4 = map(float, input().split())

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

print(f'Media: {media:.1f}')

if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    # Cálculo da nova média após o exame
    mediaFinal = (media + exame) / 2
    if mediaFinal >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {mediaFinal:.1f}')