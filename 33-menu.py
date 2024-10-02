def menu_principal():
    print('menu principal')
    print('Digite o codigo do menu')
    print('1: opcao 1')
    print('2: opcao 2')
    print('3: opcao 3')
    print('4: Finalizar')
    print('5: Cancelar')
def mostrar_sub_menu(opcao):
    print(f'Você esta na {opcao}')
    print('1: Fazer algo na opção')
    print('2: Voltar ao menu anterior')
    print('3: Sair')

while True:
    menu_principal()

    opcao = input('Escolha uma opção: ')
    
    if opcao == '1':
        mostrar_sub_menu('voce esta na opçao 1')
        sub_opcao = input('Escolha uma ação: ')

        if sub_opcao == '1':
            print('Voce fez algo na opção 1.')
        elif sub_opcao == '2':
            continue
        elif sub_opcao == '3':
            exit()
        else:
            print('Opção invalída! Tente novamente!')
        

    elif opcao == '2':
        mostrar_sub_menu('Opção 2')
        sub_opcao = input('Escolha uma ação: ')
        if sub_opcao == '1':
            print('Voce fez algo na opção 1.')
        elif sub_opcao == '2':
            continue
        elif sub_opcao == '3':
            exit()
        else:
            print('Opção invalída! Tente novamente!')



    elif opcao == '3':
        mostrar_sub_menu('Opção 3')
        sub_opcao = input('Escolha uma ação: ')
        if sub_opcao == '1':
            print('Voce fez algo na opção 1.')
        elif sub_opcao == '2':
            continue
        elif sub_opcao == '3':
            exit()
        else:
            print('Opção invalída! Tente novamente!')
        
    elif opcao == '4':
        print('Finalizar')
        break
    elif opcao == '5':
        print('sair')
        exit()
    else:
        print('Opcao invalida')/n
