#Dicionario dos preços
precos = {
    'sauiches':{
        'Big Mac' : 20.00,
        'Duplo Quarteirão' : 25.00,
        'Big Tasty' : 22.00
    },
    'Bebidas':{
        'Coca-Cola' : 5.00,
        'Fanta' : 5.00,
        'Del Valle Laranja': 6.00
    },
    'Batatas':{
        'Pequena' : 7.00,
        'Média' : 9.00,
        'Grande' : 11.00
    }
}

# Função que recebe o nome do cliente e inicia o pedido

def pegar_nome_cliente(nome):
    print(f'Vamos iniciar o pedido - Cliente: {nome}')

# Função que exibe o sanduiche escolhido
def pegar_sanduiche(tipo_sanduiche):
    print(f'Voce escolheu o sanduiche: {tipo_sanduiche}')

# Função que exibe a bebida escolhida
def pegar_bebida(tipo_bebida):
    print(f'Voce escolheu a bebida: {tipo_bebida}')

# Função que exibe a batata escolhida
def pegar_batata(tipo_batata):
    print(f'Voce escolheu a batata do tamanho: {tipo_batata}')


# Função que monta o combo e chama as funções necessárias para exibir as escolhar


# Função para escolher o tipo de sanduiche
def escolher_opcao_sanduiche():
    while True:
        sanduiche = input('Digite o código do sanduiche: \n1 - Big Mac (R$ 25,00) \n2 - Duplo Quarteirao (R$ 22,00) \n3 - Big Tasty (R$ 22,00)\nV - Voltar \nS - Sair \n**************************\n')

        if sanduiche == 'V':
            return "voltar"
        elif sanduiche == 'S':
            exit()

        opcoes = {'1': 'Big Mac', '2' : 'Duplo Quarteirao', '3' : 'Big Tasty'}
        
        if sanduiche in opcoes:
            return opcoes[sanduiche]
        
        print('Opção invalida, tente novamente')


def montar_combo(nome, tipo_sanduiche, tipo_bebida, tamanho_batata):
    pegar_nome_cliente(nome)
    pegar_sanduiche(tipo_sanduiche)
    pegar_bebida(tipo_bebida)
    pegar_batata(tamanho_batata)


while True:
    nome_cliente = input('Digite o nome do cliente (ou [s] para sair: )')

    if nome_cliente.upper() == 'S':
        exit()

    while True:
        pedido = input('Digite o código do tipo e pedido: \n1- Somente sanduiche \n2- Somente bebida \n3 - Somente batata \n4 - Combo \nF - Fechar caixa \nV - Voltar \nS - Sair \n**************************\n')
        
        if pedido.upper()  == 'S':
            exit()
        elif pedido.upper() == 'V':
            break

        # Dicionario para armazenar os itens do pedido

        if pedido == '1':
            tipo_sanduiche = escolher_opcao_sanduiche() # Escolher o sanduiche


