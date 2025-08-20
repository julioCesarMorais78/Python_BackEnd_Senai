# Verifica se a temperatura de um paciente está dentro dos limites normais.

print('PROGRAMA TEMPERATURA PACIENTE')
temperatura = float(input('Digite a temperatura do paciente: '))

if 36.0 <= temperatura <= 37.5:
    print('Temperatura normal: A temperatura está dentro dos limites normais.')
elif 37.5 < temperatura <= 38.0:
    print('Estado Febril: A temperatura está um pouco elevada.')   
elif 38.0 < temperatura <= 39.5:
    print('Com febre: A temperatura está elevada.')        
else:
    print('Febre alta: A temperatura está muito elevada.')  

# mostrando estatisticas da medição
print(f'Temperatura medida: {temperatura}°C')