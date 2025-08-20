import random

def jogo_tabuada():
    print("🎯 Bem-vindo ao jogo da tabuada!")
    print("Responda corretamente às operações. Digite 'sair' para encerrar.\n")

    acertos = 0
    erros = 0
    total_perguntas = 0

    while True:
        # Gera multiplicação aleatória
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        resposta_correta = a * b

        # Pergunta ao usuário
        resposta = input(f"Quanto é {a} x {b}? ")

        # Opção de saída
        if resposta.lower() == "sair":
            break

        # Verifica se o usuário digitou número válido
        if not resposta.isdigit():
            print("⚠️ Por favor, digite um número ou 'sair'.\n")
            continue

        resposta = int(resposta)
        total_perguntas += 1

        # Avaliação
        if resposta == resposta_correta:
            print("✅ Correto!\n")
            acertos += 1
        else:
            print(f"❌ Errado! A resposta certa é {resposta_correta}.\n")
            erros += 1

    # Resultado final
    print("\n📊 Resultado final:")
    print(f"Total de perguntas respondidas: {total_perguntas}")
    print(f"Acertos: {acertos}")
    print(f"Erros: {erros}")
    if total_perguntas > 0:
        print(f"Desempenho: {acertos / total_perguntas * 100:.2f}% de acertos!")

# Executa o jogo
jogo_tabuada()
