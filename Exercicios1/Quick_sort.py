# programa demonstrador do Quick sort

def quick_sort(lista):  # define a função quick_sort que recebe uma lista
    if len(lista) <= 1:  # verifica se a lista tem 1 ou nenhum elemento (caso base)
        return lista  # retorna a lista se ela já está ordenada (ou vazia)
    else:  # caso a lista tenha mais de um elemento
        pivot = lista[len(lista) // 2]  # escolhe o elemento do meio como pivô
        menores = [x for x in lista if x < pivot]  # cria lista com elementos menores que o pivô
        iguais = [x for x in lista if x == pivot]  # cria lista com elementos iguais ao pivô
        maiores = [x for x in lista if x > pivot]  # cria lista com elementos maiores que o pivô
        return quick_sort(menores) + iguais + quick_sort(maiores)  # ordena recursivamente e concatena os resultados

lista_valores = [5, 3, 8, 6, 2, 9, 1, 7, 4]  # define uma lista de valores desordenados

print(quick_sort(lista_valores))  # imprime a lista ordenada usando quick_sort