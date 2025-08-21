from models.livro import Livro

class Livraria:
    def __init__(self):
        self.lista_livros = []

    def _encontrar_livro(self):
        """Método auxiliar para encontrar um livro por título ou ISBN."""
        try:
            escolha = int(input("Buscar por:\n1 - Título\n2 - ISBN\nSua escolha: "))
            if escolha == 1:
                termo = input("Digite o título do livro: ")
                for livro in self.lista_livros:
                    if livro.get_nome().lower() == termo.lower():
                        return livro
            elif escolha == 2:
                termo = input("Digite o ISBN do livro: ")
                for livro in self.lista_livros:
                    if livro.get_isbn() == termo:
                        return livro
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
        return None

    def cadastrar_livro(self):
        try:
            nome = input("Digite o nome do livro: ")
            autor = input("Digite o nome do autor: ")
            isbn = input("Digite o ISBN do livro: ")
            preco = float(input("Digite o preço do livro: "))
            quantidade = int(input("Digite a quantidade em estoque: "))
            livro = Livro(nome, autor, isbn, preco, quantidade)
            self.lista_livros.append(livro)
            print("\nLivro cadastrado com sucesso!")
        except ValueError:
            print("\nErro: Preço e quantidade devem ser números. Tente novamente.")

    def buscar_livro(self):
        print("\n--- Buscar Livro ---")
        livro = self._encontrar_livro()
        if livro:
            livro.exibir_informacoes()
        else:
            print("\nLivro não encontrado.")

    def atualizar_estoque(self):
        print("\n--- Atualizar Estoque ---")
        livro = self._encontrar_livro()
        if not livro:
            print("\nLivro não encontrado.")
            return
        
        try:
            opcao = int(input("1: Adicionar ao estoque\n2: Remover do estoque\nSua escolha: "))
            quantidade = int(input("Digite a quantidade: "))

            if opcao == 1:
                livro.adicionar_ao_estoque(quantidade)
                print("\nEstoque atualizado com sucesso!")
            elif opcao == 2:
                livro.remover_do_estoque(quantidade)
                print("\nEstoque atualizado com sucesso!")
            else:
                print("Opção inválida.")
        except ValueError:
            print("\nEntrada inválida. A quantidade deve ser um número.")

    def remover_livro(self):
        print("\n--- Remover Livro ---")
        livro_para_remover = self._encontrar_livro()
        if livro_para_remover:
            self.lista_livros.remove(livro_para_remover)
            print("\nLivro removido com sucesso!")
        else:
            print("\nLivro não encontrado.")

    def run(self):
        """Inicia a execução do menu principal da livraria."""
        loop_parameter = True
        menu = """
=========================
      MENU LIVRARIA
=========================
1 - Cadastrar livro
2 - Buscar livro
3 - Atualizar o estoque
4 - Remover Livro
5 - Sair
=========================
Sua escolha: """

        def sair():
            nonlocal loop_parameter
            loop_parameter = False
            print("\nSaindo do sistema...")

        choice_switch = {
            1: self.cadastrar_livro,
            2: self.buscar_livro,
            3: self.atualizar_estoque,
            4: self.remover_livro,
            5: sair,
        }

        while loop_parameter:
            try:
                user_choice = int(input(menu))
                action = choice_switch.get(user_choice)
                if action:
                    action()
                else:
                    print("\nOpção inválida. Por favor, tente novamente.")
            except ValueError:
                print("\nEntrada inválida. Por favor, digite um número de 1 a 5.")