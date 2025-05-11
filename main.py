def iniciar_jogo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Menu sendo exibido!")  # Depuração
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
