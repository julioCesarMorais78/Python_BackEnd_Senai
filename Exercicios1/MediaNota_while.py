print('CALCULA MEDIA NOTAS')

while True:
    nome_aluno = input('Digite o nome do aluno: ')

    num_notas = int(input('Quantas notas deseja inserir para {}? '.format(nome_aluno)))
    notas = []
    for i in range(num_notas):
        nota = float(input(f'Digite a nota {i+1}: '))
        notas.append(nota)
    media = sum(notas) / num_notas

    if media >= 7:
        print('Aluno(a) {} foi aprovado com média {:.2f}'.format(nome_aluno, media))
    elif 5 <= media < 7:
        print('Aluno(a) {} ficou em recuperação com média {:.2f}'.format(nome_aluno, media))
    else:
        print('Aluno(a) {} foi reprovado com média {:.2f}'.format(nome_aluno, media))

    continuar = input('Deseja calcular a média de outro aluno? (s/n): ').strip().lower()
    if continuar != 's':
        print('Encerrando o programa.')
        break