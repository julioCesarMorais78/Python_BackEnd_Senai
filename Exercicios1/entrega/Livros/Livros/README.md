# Projeto Livros

## Visão Geral
O projeto Livros é uma aplicação Python projetada para gerenciar uma coleção de livros. Ele permite aos usuários cadastrar novos livros, buscar livros existentes por título ou ISBN, atualizar as quantidades em estoque e remover livros da coleção. A aplicação é estruturada usando princípios de orientação a objetos para promover uma melhor organização e manutenibilidade.

## Estrutura do Projeto
```
Livros
├── __init__.py
├── main.py
├── models
│   ├── __init__.py
│   └── livro.py
├── services
│   ├── __init__.py
│   └── livraria.py
└── README.md
```

## Componentes

### 1. `Livros/__init__.py`
Este arquivo marca o diretório como um pacote Python. Pode ser usado para inicializar o pacote ou definir o que é exportado quando o pacote é importado.

### 2. `Livros/main.py`
Este é o ponto de entrada da aplicação. Ele contém a lógica principal para gerenciar os livros, incluindo funções para cadastrar, buscar, atualizar e remover livros. Essas funções serão refatoradas para uma classe para aplicar os princípios de encapsulamento e design orientado a objetos.

### 3. `Livros/models/__init__.py`
Este arquivo marca o diretório `models` como um pacote Python. Pode ser usado para inicializar o pacote ou definir o que é exportado quando o pacote é importado.

### 4. `Livros/models/livro.py`
Este arquivo define a classe `Livro`, que representa um livro com atributos como nome, autor, ISBN, preço e quantidade em estoque. Inclui métodos para exibir informações do livro e gerenciar o estoque.

### 5. `Livros/services/__init__.py`
Este arquivo marca o diretório `services` como um pacote Python. Pode ser usado para inicializar o pacote ou definir o que é exportado quando o pacote é importado.

### 6. `Livros/services/livraria.py`
Este arquivo conterá uma nova classe (ex: `Livraria`) que encapsula as funções de gerenciamento de livros do `main.py`. Fornecerá métodos para adicionar, buscar, atualizar e remover livros, promovendo uma melhor organização e encapsulamento.

## Uso
Para executar a aplicação, execute o arquivo `main.py`. Siga o menu na tela para gerenciar a coleção de livros. Certifique-se de que as dependências necessárias estão instaladas e que a estrutura do projeto é mantida.

## Melhorias Futuras
- Implementar um banco de dados para armazenamento persistente das informações dos livros.
- Adicionar autenticação de usuário para gerenciar o acesso à coleção de livros.
- Aprimorar a interface do usuário