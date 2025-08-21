# calcula fatorial com while
print('CALCULA FATORIAL')
numero = int(input('Digite um número inteiro não negativo para calcular o fatorial: '))

if numero < 0:
    print('Número inválido. O fatorial só é definido para números não negativos.')

else:
    fatorial = 1
    contador = 1
    while contador <= numero:
        fatorial *= contador
        contador += 1
    print(f'O fatorial de {numero} é {fatorial}.')
