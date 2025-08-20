print('PROGRAMA TABUADA')

numero_tabuada = int(input('Digite um número de 1 a 10 para ver sua tabuada: '))

print(f'Tabuada do {numero_tabuada}:')

if numero_tabuada < 1 or numero_tabuada > 10:
    print('Número inválido. Por favor, digite um número entre 1 e 10.')
else:
    for i in range(1, 11):
        resultado = numero_tabuada * i
        print(f'{numero_tabuada} x {i} = {resultado}')
    print(f'Fim da tabuada do {numero_tabuada}.')