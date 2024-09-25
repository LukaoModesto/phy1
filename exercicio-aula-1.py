# Exercício 1:
# Solicite ao usuário que insira seu nome e idade. Em seguida, exiba uma mensagem de boas-vindas.
# mensagem Olá, [nome]! Você tem [idade] anos.

# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))

# print(f'Olá, {nome}! Você tem {idade} anos.')


################################################################

# Exercício 2:
# Solicite ao usuário que insira um numero flutuante
# soma com o valor constante 25
# mensagem = A soma de [numero] mais [NUMERO_CONSTANTE] é [resultado].

# Lembrete: Temos que converter o numero para flutuante


# numero = float(input("Digite um numero"))
# NUMERO_CONSTANTE = 25
# soma = numero + NUMERO_CONSTANTE

# print(f'A soma de {numero} mais {NUMERO_CONSTANTE} é {soma}.')

#################################################################

# Exercício 3:
# Crie uma variável chamada nome_completo para armazenar o nome completo de uma pessoa.
# Crie outra variável chamada idade para armazenar a idade da pessoa.
# Crie uma variável salario_mensal para armazenar o salário mensal da pessoa.
# Por fim, exiba essas informações de forma concatenada no seguinte formato:
# "Meu nome é [nome_completo], tenho [idade] anos e ganho R$ [salario_mensal] por mês."

# nome_completo = input('Digite seu nome completo: ')
# idade = input('Digite sua idade: ')
# salario_mensal = float(input('Digite seu salario'))

# print(f'Meu nome é {nome_completo}, tenho {idade} anos e ganho R$ {salario_mensal} por mês.')

# print('Meu nome é ' + nome_completo + ', tenho ' + idade + 'anos e ganho R$ ' + salario_mensal + ' por mês.')

##* Extra Formatar o salario_mensal como moeda



# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
# nome_completo = input('Digite seu nome completo: ')
# idade = input('Digite sua idade: ')
# salario_mensal = float(input('Digite seu salario'))
# valor_formatado = locale.currency(salario_mensal, grouping = True)
# print(f'Meu nome é {nome_completo}, tenho {idade} anos e ganho {valor_formatado} por mês.')


#################################################################

# Exercício 4:
# Solicite ao usuário dois números inteiros e exiba a soma dos números.



# num1 = int(input("Digite um numero"))
# num2 = int(input("Digite um numero"))
# soma = num1 + num2
# print(soma)

#################################################################

#Exercício 5:
# Peça ao usuário que insira um número decimal (float) e exiba o dobro desse número.
# Saida = O dobro de ? é ?.
# exemplo = entrada 5 então a saida seria "O dobro de 5 é 10"



# num = float(input('Digite um numero flutuante'))
# dobro = num * 2
# print(f'O dobro de {num} é {dobro}.')



#################################################################

# Exercício 6:

# Peça ao usuário que insira seu nome e se está estudando atualmente (responda com "sim" ou "não"). Exiba uma mensagem confirmando sua resposta.
# entrada = Digite seu nome
# entrada = Está estudando atualmente, digite "sim" ou "não 
## temos que tratar o valor de entrada "sim" ou "não com .strip().lower()
# saida =[nome], você está estudando: [esta_estudando].")
# a variavel [esta_estudando] vai ser igual a true ou false

# nome = input('Digite seu nome: ')
# estudando = input('Está estudando atualmente, digite "sim" ou "não": ')

# esta_estudando = (estudando.strip().lower() == 'sim')

# print(f'{nome}, você está estudando: {esta_estudando}.')


######

## Extra implementar if else
## se a variavel [esta_estudando] = True 
## saida = [nome], ótimo continue assim!
## se não 
## saida = [nome], vamos estudar!


# nome = input('Digite seu nome: ')
# estudando = input("Está estudando atualmente, digite \"sim\" ou \"não\": ")
  
# esta_estudando = (estudando.strip().lower() == 'sim')
# nao_estudando = (estudando.strip().lower() == 'nao')
# nao1_estudando = (estudando.strip().lower() == 'não')

# if esta_estudando == True:
# # if esta_estudando:
#     print(f'{nome}, você esta estudando!')
# elif nao_estudando == True or nao1_estudando == True:
#     print(f'{nome}, bora estuda')
# else:
#     print(f'Digite sim ou não')





#################################################################

# Exercício 7:
# Peça ao usuário para inserir seu nome e um número, depois exiba o nome repetido esse número de vezes.


# nome = input('Digite seu nome: ')
# numero_repeticoes = int(input('Digite um numero: '))
# print((f'{nome} \n') * numero_repeticoes)


#################################################################

# Exercício 8:
# Solicite ao usuário que insira seu peso e altura, calcule seu IMC (Índice de Massa Corporal) e exiba o resultado.
# Fórmula do IMC: IMC = peso / altura²

# peso = float(input('Digite seu peso: '))
# altura = float(input('Digite sua altura: '))

# IMC = peso / (altura ** 2)

# print(f'Seu IMC é {IMC:.2f}.')

#################################################################

# Exercício 9:
# Solicite ao usuário que insira a quantidade de horas trabalhadas e o valor da hora. Calcule e exiba o salário bruto.

# horas_trabalhadas = float(input('Digite o número de horas trabalhadas: '))
# valor_hora = float(input('Digite o valor por hora: '))
# salario = horas_trabalhadas * valor_hora

# print(f'Seu salário é R$ {salario}')

#################################################################

# Exercício 10:
# Solicite ao usuário um valor de produto e uma porcentagem de desconto. Calcule e exiba o valor final com o desconto aplicado.

# valor_produto = float(input('Digite o valor do produto: '))
# desconto = float(input('Digite a porcentagem de desconto: '))

# valor_final = valor_produto - (valor_produto * desconto / 100)

# print(f'O valor final com desconto é R$ {valor_final}')



#################################################################

#Exercício 11:
# Escreva um programa que solicite ao usuário um número e verifique se o número é positivo ou negativo. Se o número for zero, informe que é zero.

# numero > 0: "O número é positivo."
# numero < 0: "O número é negativo."
# numero == 0: "O número é zero."

# numero = float(input("Digite um número: "))

# if numero > 0:
#     print('O número é positivo.')
# elif numero < 0:
#     print('O número é negativo.')
# elif numero == 0:
#     print('O número é zero')
# else:
#     print('Digite um número valido!')





#################################################################

# Exercício 12:
# Peça ao usuário para inserir um número inteiro e verifique se é par ou ímpar. Exiba o resultado.

# numero = int(input('Digite um número inteiro: '))

# calculo = numero % 2

# if calculo == 0:
#     print(f'{numero} é par! ')
# else:
#     print(f'{numero} é ímpar! ')


#################################################################

# Exercício 13:
# O programa recebe o valor de compra e se o cliente for um cliente frequente (responda com "sim" ou "não")
# O cliente recebe desconto se suas compras forem maiores que 1000 'ou' se for cliente frequente
## temos que tratar o valor de entrada "sim" ou "não" com .strip().lower()
# utilize a conditional if e else

# compra = float(input('Digite o valor da compra: '))
# cliente_frequente = input('Digite se o cliente faz compras frequentes (responda com "sim" ou "não")').strip().lower() 

# if compra > 1000 or cliente_frequente == 'sim':
#     print('Você recebeu um desconto!')
# else:
#     print('Sem desconto!')

#################################################################


# Exercício 14:
# Crie um programa que solicite ao usuário 3 notas de um aluno (entre 0 e 10), calcule a média e exiba a classificação da nota com base na média final:

# Média menor que 5: "Reprovado"
# Média entre 5 e 6: "Recuperação"
# Média maior ou igual a 7: "Aprovado"

# nota1 = int(input('Digite a primeira nota (0 a 10)'))
# nota2 = int(input('Digite a segunda nota (0 a 10)'))
# nota3 = int(input('Digite a terceira nota (0 a 10)'))

# media = (nota1 + nota2 + nota3) / 3

# print(f"Média: {media:.2f}")

# if media < 5: 
#     print("Reprovado")
# # elif media >= 5 and media < 7:
# elif 5 <= media < 7: 
#     print("Recuperação")
# else:
#     print("Aprovado")





#################################################################

# Exercício 15:
# Escreva um programa que solicita a temperatura em graus Celsius e exibe se o clima está frio, agradável ou quente.

# Menor que 15: "O clima está frio"
# Entre 15 e 25: "O clima está agradável"
# 26 ou mais: "O clima está quente."

# temperatura = float(input("Digite a temperatura em graus Celsius"))

# if temperatura < 15:
#     print("O clima está frio")
# elif 15 <= temperatura <= 25: ####################
#     print("O clima está agradável")
# else:
#     print("O clima está quente.")





#################################################################

# Exercício 16:
# Crie um programa que solicite ao usuário que insira sua idade e exiba uma mensagem com base na faixa etária da pessoa:

# Menor de 12 anos: "Você é uma criança."
# Entre 12 e 17 anos: "Você é um adolescente."
# Entre 18 e 59 anos: "Você é um adulto."
# 60 anos ou mais: "Você é idoso."


# idade = int(input('Digite sua idade: '))

# if idade < 12:
#     print("Você é uma criança.")
# elif 12 <= idade < 18:
#     print("Você é um adolescente.")
# elif 18 <= idade < 60:
#     print("Você é um adulto.")
# else:
#     print("Você é idoso.")



