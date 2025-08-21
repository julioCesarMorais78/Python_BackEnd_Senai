from livro import Livro

LOOP_PARAMETER = True

menu = """
1 - Cadastrar livro
2 - Busca livro (Título ou ISBN)
3 - Atualizar o estoque
4 - Remover Livro
5 - Sair
"""

LISTA_LIVROS = []

def cadastrar_livro():
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    isbn = input("Digite o ISBN do livro: ")
    preco = float(input("Digite o preço do livro: "))
    quantidade_em_estoque = int(input("Digite a quantidade em estoque: "))
    livro = Livro(nome, autor, isbn, preco, quantidade_em_estoque)
    LISTA_LIVROS.append(livro)
    print("Livro cadastrado com sucesso!")

def buscar_livro():
    if int(input("1:Buscar por nome\n2:Buscar por ISBN\n")) == 1:
        nome = input("Digite o nome do livro: ")
        for livro in LISTA_LIVROS:
            if livro.getNome() == nome:
                livro.exibir_informacoes()
    else:
        isbn = input("Digite o ISBN do livro: ")
        for livro in LISTA_LIVROS:
            if livro.getIsbn() == isbn:
                livro.exibir_informacoes()
    

def atualizar_estoque():
    if int(input("1:Adicionar ao estoque\n2:Remover do estoque\n")) == 1:
        nome = input("Digite o nome do livro: ")
        for livro in LISTA_LIVROS:
            if livro.getNome() == nome:
                quantidade = int(input("Digite a quantidade a ser adicionada: "))
                livro.adicionar_ao_estoque(quantidade)
    else:
        nome = input("Digite o nome do livro: ")
        for livro in LISTA_LIVROS:
            if livro.getNome() == nome:
                quantidade = int(input("Digite a quantidade a ser removida: "))
                livro.remover_do_estoque(quantidade)    
            

def remover_livro():
    if int(input("1:Remover por nome\n2:Remover por ISBN\n")) == 1:
        nome = input("Digite o nome do livro: ")
        for livro in LISTA_LIVROS:
            if livro.getNome() == nome:
                LISTA_LIVROS.remove(livro)
                print("Livro removido com sucesso!")

def set_LOOP_PARAMETER():
    #tem que ser colocar o global pq loop parameter é uma
    #variável global
    global LOOP_PARAMETER
    LOOP_PARAMETER = False


while LOOP_PARAMETER:
    user_choice = int(input(menu))
    choice_switch = {
        1: cadastrar_livro,
        2: buscar_livro,
        3: atualizar_estoque,
        4: remover_livro,
        5: set_LOOP_PARAMETER,
    }
    #Estrutura que opera a escolha do usuário
    #e atrela a uma das funções
    choice_switch[user_choice]()

