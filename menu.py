import time
import os

# Funções de Menu
def exibir_menu():
    print("Bem-vindo ao Menu!")
    print("[1] Iniciar Jogo")
    print("[2] Sobre o Jogo")
    print("[3] Sair")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def subir_nivel(personagem):
    """Função para aumentar as estatísticas do personagem ao subir de nível"""
    personagem['vida'] += 20
    personagem['ataque'] += 30
    personagem['mana'] += 15
    personagem['nivel'] += 1
    print(f"\n{personagem['nome']} subiu para o nível {personagem['nivel']}!")

def exibir_ficha(personagem):
    print('\n--- Ficha do Personagem ---')
    for chave, valor in personagem.items():
        print(f"{chave.capitalize()}: {valor}")

def main():
    limpar_tela()
    print('=' * 60)
    print('==' * 6, 'Seja Bem-vindo ao RPG do Submundo', '==' * 6)
    print('=' * 60)
    print('\nEssas são as classes disponíveis:\n')
    time.sleep(2)

    classes_rpg = {
        1: {"nome": "Guardião Arcano", "papel": "Tank / Suporte Mágico", "descricao": "Guerreiro com armadura rúnica que protege aliados e absorve danos.",
            "habilidades": ["Barreira Arcana", "Provocação Rúnica", "Cura por Runas"]},
        2: {"nome": "Lâmina Sombria", "papel": "Assassino / Dano físico", "descricao": "Especialista em furtividade e ataques rápidos com lâminas envenenadas.",
            "habilidades": ["Golpe Silencioso", "Sombra Veloz", "Veneno Paralizante"]},
        3: {"nome": "Teurgo da Tempestade", "papel": "Mago Elemental / Dano em área", "descricao": "Conjurador que manipula raios e ventos destrutivos.",
            "habilidades": ["Raio em Cadeia", "Turbilhão", "Olho da Tempestade"]},
        4: {"nome": "Arauto da Vida", "papel": "Suporte / Curandeiro", "descricao": "Sacerdote místico que cura e remove maldições dos aliados.",
            "habilidades": ["Toque da Vida", "Benção da Pureza", "Ressurreição Rápida"]},
        5: {"nome": "Forjador de Bestas", "papel": "Invocador / Dano variável", "descricao": "Domador que invoca criaturas míticas com diferentes funções.",
            "habilidades": ["Invocar Lobo Ígneo", "Vínculo Animal", "Chamar Quimera"]},
    }

    for id, classe in classes_rpg.items():
        print(f"{id}. {classe['nome']}\n   Papel: {classe['papel']}\n   Descrição: {classe['descricao']}\n   Habilidades:")
        for habilidade in classe['habilidades']:
            print(f"     - {habilidade}")
        print()

    nome = input('\nDigite o nome de seu avatar: ')
    print(f'\nSeja bem-vindo, jovem mestre {nome}!')

    try:
        escolha = int(input("\nDigite o número correspondente à sua classe: "))
        classe_escolhida = classes_rpg.get(escolha, {
            "nome": "Aventureiro Inexperiente",
            "papel": "Nenhum",
            "descricao": "Ainda não escolheu um caminho.",
            "habilidades": []
        })
    except ValueError:
        print("\nEntrada inválida! Você será um Aventureiro Inexperiente.")
        classe_escolhida = {
            "nome": "Aventureiro Inexperiente",
            "papel": "Nenhum",
            "descricao": "Ainda não escolheu um caminho.",
            "habilidades": []
        }

    personagem = {
        'nome': nome,
        'classe': classe_escolhida['nome'],
        'vida': 100,
        'ataque': 200,
        'mana': 10,
        'nivel': 1
    }

    exibir_ficha(personagem)

    while True:
        print(f"\nCerto jovem {personagem['nome']}, agora vamos prosseguir. O que deseja fazer agora!?\n")
        print("""
        [1] Iniciar primeira missão
        [2] Ver ficha do personagem
        [3] Descansar
        [4] Sair do jogo
        """)

        escolha_acao = input('Digite o número da ação desejada: ')

        if escolha_acao == '1':
            print('\nVocê se prepara para sua primeira missão no Submundo...')
            break

        elif escolha_acao == '2':
            exibir_ficha(personagem)

        elif escolha_acao == '3':
            print('\nVocê decide descansar para recuperar suas energias...')
            personagem['vida'] = 100

            print('Sua vida foi restaurada para 100.')
        elif escolha_acao == '4':
            
            print('\nSaindo do jogo... Até a próxima aventura!')
            break
        else:
            print('\nOpção inválida. Por favor, escolha uma das opções listadas.')

if __name__ == "__main__":
    main()
