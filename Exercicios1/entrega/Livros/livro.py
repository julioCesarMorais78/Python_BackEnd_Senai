
class Livro:
    def __init__(self, titulo: str, autor: str, isbn: str, preco: float, quantidade_em_estoque: int):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque
    
    def adicionar_ao_estoque(self, quantidade):
        self.quantidade_em_estoque += quantidade
    
    def remover_do_estoque(self, quantidade):
        if self.quantidade_em_estoque >= quantidade:
            self.quantidade_em_estoque -= quantidade
        else:
            print("Não há livros suficientes em estoque para remover essa quantidade.")
    
    def getNome(self):
        return self.titulo
    
    def getIsbn(self):
        return self.isbn
    

    def exibir_informacoes(self):
        text = f"""Nome: {self.titulo}
Autor: {self.autor}
ISBN: {self.isbn}
Preço: R${self.preco:.2f}
Quantidade em estoque: {self.quantidade_em_estoque}
""" 
        print(text)
