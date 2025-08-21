class Livro:
    def __init__(self, nome, autor, isbn, preco, quantidade_em_estoque):
        self.__nome = nome
        self.__autor = autor
        self.__isbn = isbn
        self.__preco = preco
        self.__quantidade_em_estoque = quantidade_em_estoque

    def get_nome(self):
        return self.__nome

    def get_autor(self):
        return self.__autor

    def get_isbn(self):
        return self.__isbn

    def get_preco(self):
        return self.__preco

    def get_quantidade_em_estoque(self):
        return self.__quantidade_em_estoque

    def adicionar_ao_estoque(self, quantidade):
        self.__quantidade_em_estoque += quantidade

    def remover_do_estoque(self, quantidade):
        if quantidade <= self.__quantidade_em_estoque:
            self.__quantidade_em_estoque -= quantidade
        else:
            print("Quantidade a remover é maior que a disponível em estoque.")

    def exibir_informacoes(self):
        print(f"Nome: {self.__nome}, Autor: {self.__autor}, ISBN: {self.__isbn}, Preço: {self.__preco}, Estoque: {self.__quantidade_em_estoque}")