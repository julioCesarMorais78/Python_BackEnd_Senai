class Estoque:
    def __init__(self, codigo: int, descricao: str, preco: float, quantidade_estoque: int) -> None:
        # Atributos privados (indicados por __)
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    # Método para adicionar itens ao estoque.
    # O "self" se refere à instância do objeto que está chamando o método.
    def entrada_estoque(self, quantidade: int) -> None:
        if quantidade > 0:
            self.__quantidade_estoque += quantidade
            print(f"Entrada de {quantidade} unidades de '{self.__descricao}'.")
        else:
            print("A quantidade para entrada deve ser maior que zero.")

    # Método para remover itens do estoque.
    def saida_estoque(self, quantidade: int) -> None:
        if 0 < quantidade <= self.__quantidade_estoque:
            self.__quantidade_estoque -= quantidade
            print(f"Saída de {quantidade} unidades de '{self.__descricao}'.")
        else:
            print("Quantidade inválida para saída ou estoque insuficiente.")

    # Método para visualizar a quantidade atual.
    def visualizar_quantidade_em_estoque(self) -> None:
        print(f"A quantidade em estoque de '{self.__descricao}' é: {self.__quantidade_estoque}")

    # --- Getters e Setters (métodos de acesso) ---

    # Getter para o código
    def get_codigo(self) -> int:
        return self.__codigo

    # Getter para a descrição
    def get_descricao(self) -> str:
        return self.__descricao

    # Setter para a descrição
    def set_descricao(self, nova_descricao: str) -> None:
        self.__descricao = nova_descricao

    # Getter para o preço
    def get_preco(self) -> float:
        return self.__preco

    # Setter para o preço (com validação)
    def set_preco(self, novo_preco: float) -> None:
        if novo_preco > 0:
            self.__preco = novo_preco
        else:
            print('O preço deve ser maior que zero.')

    # Getter para a quantidade em estoque
    def get_quantidade_estoque(self) -> int:
        return self.__quantidade_estoque


# --- Teste do Código Corrigido ---
# Criando uma instância do produto
produto1 = Estoque(1, 'Som Automotivo', 54.20, 8)

# Chamando os métodos diretamente do objeto
produto1.entrada_estoque(2)
produto1.visualizar_quantidade_em_estoque()

# Testando outros métodos
print(f"Preço atual: R${produto1.get_preco()}")
produto1.set_preco(60.00)
print(f"Novo preço: R${produto1.get_preco()}")

produto1.saida_estoque(5)
produto1.visualizar_quantidade_em_estoque()