print('PROGRAMA GOSTA DE PYTHON')

decisao = True

while True:
    resposta = input('Você gosta de Python? (sim/nao): ').strip().lower()
    if resposta == 'sim':
        print('Resposta Correta. Que bom que você gosta de Python!')
        decisao = False
        break
    elif resposta == 'nao':
        print('Esta não é a resposta correta, tente novamente.')

    else:
        print('Resposta inválida. Por favor, responda com "sim" ou "nao".')