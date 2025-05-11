import os
import time
from menu import exibir_menu  # Importa a função do menu.py

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def star_wars_efeito(texto, velocidade=0.3):
    linhas = texto.strip().split('\n')
    largura = os.get_terminal_size().columns
    altura = os.get_terminal_size().lines

    buffer = [''] * altura
    for linha in linhas:
        buffer.append(linha.center(largura))
        buffer.pop(0)
        clear()
        print('\n'.join(buffer))
        time.sleep(velocidade)

    time.sleep(3)

def iniciar_vilarejo():
    texto = """
    Eldoria das Brumas Eternas...

    Há muito tempo, um vilarejo surgiu nas fronteiras da grande floresta de Skelgar...
    """
    clear()
    star_wars_efeito(texto, velocidade=0.4)
    print("\nVocê chegou ao vilarejo. O que deseja fazer?")
    escolhas()

def escolhas():
    print('\nO que deseja fazer agora? ')
    print('[1] Falar com a velha')
    print('[2] Olhar ao redor')
    print('[3] Tentar entender o que aconteceu')

    escolha = input('\nEscolha uma ação: ')

    if escolha == '1':
        falar_com_a_velha()
    elif escolha == '2':
        olhar_ao_redor()
    elif escolha == '3':
        tentar_entender_o_que_aconteceu()
    else:
        print('\nOpção inválida! Tente novamente')
        escolhas()

def falar_com_a_velha():
    print('\nVocê se aproxima da velha e pergunta o que está acontecendo.')
    time.sleep(2)
    print("\nEla olha para você com um olhar que mistura receio e compaixão.")
    time.sleep(2)
    print("\nEste lugar... é um refúgio para aqueles que não pertencem mais ao seu mundo.")
    time.sleep(2)
    print("\nEla faz uma pausa. 'Se você chegou aqui, então há algo que os Guardiões precisam saber.'")
    escolhas()

def olhar_ao_redor():
    print("\nVocê observa a paisagem ao redor. O campo é coberto por uma névoa espessa, e ao longe, há uma torre que parece em ruínas.")
    time.sleep(2)
    print("\nA brisa traz um cheiro de terra e um som distante de algo movimentando-se na escuridão.")
    time.sleep(2)
    print("\nVocê percebe que a velha está lhe observando, mas não parece incomodada com seu comportamento.")
    time.sleep(2)
    print("\nAs palavras da velha ecoam em sua mente enquanto você começa a perceber que esta jornada está longe de ser comum.")
    escolhas()

def tentar_entender_o_que_aconteceu():
    print("\nVocê tenta entender o que aconteceu. A luz, o teletransporte... por que você está aqui?")
    time.sleep(2)
    print("\nDe repente, uma sensação de inquietação toma conta de você. Algo muito maior está acontecendo.")
    time.sleep(2)
    print("\n'Você não está sozinho aqui. Muitos vieram antes de você e não retornaram.'")
    time.sleep(2)
    print("\nAs palavras da velha ecoam em sua mente enquanto você começa a perceber que esta jornada está longe de ser comum.")
    escolhas()

def iniciar_jogo():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_menu()  # Chama o menu
    opcao = input("\nEscolha uma opção: ")
    if opcao == '1':
        iniciar_vilarejo()  # Chama o vilarejo se o jogador escolher a opção 1
    elif opcao == '2':
        print("Criado por você! 🌟")
    elif opcao == '3':
        print("Saindo...")
    else:
        print("Opção inválida.")

# Ponto de entrada para o programa
if __name__ == "__main__":
    iniciar_jogo()
