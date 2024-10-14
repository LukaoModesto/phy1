def menu_principal():
    print('Menu principal')
    print('Digite o código do menu')
    print('1: Opção 1')
    print('2: Opção 2')
    print('3: Opção 3')
    print('4: Finalizar')
    print('5: Sair')

def mostra_sub_menu(opcao):
    print(f'Você está na {opcao}')
    print('1: Fazer algo na opção')
    print('2: Voltar ao menu anterior')
    print('3: Sair')

def main():
    while True:
        menu_principal()

        opcao = input('Escolha uma opção:')

        if opcao == '1':
            mostra_sub_menu('Opção 1')
            sub_opcao = input('Escolha uma ação: ')

            if sub_opcao == '1':
                print('Você fez algo na opção 1.')
            elif sub_opcao == '2':
                continue
            elif sub_opcao == '3':
                exit()
            else:
                print('Opção invalida!') 

        elif opcao == '2':
            mostra_sub_menu('Opção 2')
            sub_opcao = input('Escolha uma ação: ')

            if sub_opcao == '1':
                print('Você fez algo na opção 2.')
            elif sub_opcao == '2':
                continue
            elif sub_opcao == '3':
                exit()
            else:
                print('Opção invalida!')    

        elif opcao == '3':
            mostra_sub_menu('Opção 3')
            sub_opcao = input('Escolha uma ação: ')

            if sub_opcao == '1':
                print('Você fez algo na opção 2.')
            elif sub_opcao == '2':
                continue
            elif sub_opcao == '3':
                exit()
            else:
                print('Opção invalida!')


        elif opcao == '4':
            print('Finalizar!')
            break
    
        elif opcao == '5':
            print('Sair!')
            exit()
        else:
            print('Opção invalida! Tente novamente!')
        

main()