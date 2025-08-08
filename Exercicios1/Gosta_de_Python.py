print('PROGRAMA GOSTA DE PYTHON')

decisao = True

while True:
    resposta = input('Você gosta de Python? (s/n): ').strip().lower()
    if resposta == 's':
        print('Resposta Correta. Que bom que você gosta de Python!')
        decisao = False
        break
    elif resposta != 's':
        print('Esta não é a resposta correta, tente novamente.')