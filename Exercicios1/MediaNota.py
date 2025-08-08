print('CALCULA MEDIA 2 NOTAS')

nome_aluno = input('Digite o nome do aluno: ')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7:
    print('Aluno(a) {} foi aprovado com média {:.2f}'.format(nome_aluno, media))
    
elif 5 >= media < 7:
    print('Aluno(a) {} ficou em recuperação com média {:.2f}'.format(nome_aluno, media))
    
else:
    print('Aluno(a) {} foi reprovado com média {:.2f}'.format(nome_aluno, media))