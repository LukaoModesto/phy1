# Dicionario com os preços dos produtos

precos = {
    'sanduiches':{
        'Big Mac' : 20.00,
        'Duplo Quarteirão' : 25.00,
        'Big Tasty' : 22.00
    },
    'bebidas':{
        'Coca-Cola' : 5.00,
        'Fanta' : 5.00,
        'Del Valle Laranja' : 6.00
    },
    'batatas':{
        'Pequena' : 7.00,
        'Média' : 9.00,
        'Grande' : 11.00
    }
}

# Função que recebe o nome do cliente e inicia o pedido

def pegar_nome_cliente(nome):
    print(f'Vamos iniciar o pedido - Cliente: {nome}')

# pegar_nome_cliente('Fulano')

# Função que exibe o sanduiche escolhido
def pegar_sanduiche(tipo_sanduiche):
    print(f'Você escolheu o sanduiche: {tipo_sanduiche}')

# pegar_sanduiche('Duplo Quarteirão')

# Função que exibe a bebida escolhida

def pegar_bebida(tipo_bebida):
    print(f'Você escolheu a bebida: {tipo_bebida}')

# pegar_bebida('Coca-Cola')


# Função que exibe a batata escolhida

def pegar_batata(tipo_batata):
    print(f'Você escolheu a batata do tamanho: {tipo_batata}')

# pegar_batata('Pequena')


# Função que monta o combo e chama as funções necessárias para exibir as escolhas
def montar_combo(nome, tipo_sanduiche, tipo_bebida, tamanho_batata):
    pegar_nome_cliente(nome)
    pegar_sanduiche(tipo_sanduiche)
    pegar_bebida(tipo_bebida)
    pegar_batata(tamanho_batata)

# montar_combo('Diego','Big Tasty','Coca-cola','Pequena')


# Função para escolher o tipo de sanduíche
def escolher_opcao_sanduiche():
    while True:
        sanduiche = input('Digite o código do sanduíche: \n1 - Big Mac (R$ 20,00) \n2 - Duplo Quarteirão (R$ 25,00) \n3 - Big Tasty (R$ 22,00) \nV - Voltar \nS - Sair')

        if sanduiche == "V":
            return "voltar"
        elif sanduiche == "S":
            exit()

        opcoes = {'1': 'Big Mac', '2' : 'Duplo Quarteirão', '3': 'Big Tasty' }

        if sanduiche in opcoes:
            return opcoes[sanduiche]
        
        print('Opção inválida, tente novamente') #### Terminamos aqui

        
           


while True:
    nome_cliente = input('Digite o nome do cliente (ou [s] para sair): ')

    if nome_cliente.upper() == 'S':
        exit()

    pegar_nome_cliente(nome_cliente)

    while True:
        pedido = input('Digite o código do tipo e pedido: \n1 - Somente sanduíche \n2 - Somente bebida \n3 - Somente batata \n4 - Combo \nF - Fechar caixa \nV - Voltar \nS - Sair \n********************* \n' )

        if pedido.upper() == "S":
            exit()
        elif pedido == "V":
            break

        # Dicionario para armazenar os itens do pedido

        if pedido == '1':
            tipo_sanduiche = escolher_opcao_sanduiche() # Escolhe o sanduíche



