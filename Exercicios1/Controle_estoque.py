#criação de produto de forma procedural

def cria_produto(codigo: int, descricao: str,preco: float, quantidade_estoque: int)->None:
     produto = {
        'codigo': codigo,
        'descricao': descricao,
        'preco': preco,
        'quantidade_estoque': quantidade_estoque
     } 
     return produto

def entrada_estoque(produto: dict, quantidade: int)->None:
     produto['quantidade_estoque'] += quantidade

def saida_estoque(produto: dict, quantidade: int)->None:
     produto['quantidade_estoque'] -= quantidade

def visualizar_quantidade_em_estoque(produto: dict):
     print(f'A quantidade em estoque e {produto['quantidade_estoque']}')

# teste
produto1 = cria_produto(1, 'Som Automotivo', 54.20, 8)
entrada_estoque(produto1, 2)
visualizar_quantidade_em_estoque(produto1)