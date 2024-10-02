# numero = 0

# while numero != 9999:
#     numero = int(input('Digite um numero ou digite 9999 para sair'))
#     exit()

# print('fim')

# numero = 0
# soma = 0

# while True:
#     numero = int(input('Digite um numero ou digite 9999 para sair: '))
#     if numero == 9999:
#         break
#     else:
#         soma += numero
#         print(soma)

# print(soma)
# print('fim')

# break(quebrar)
# break interrompe completamente o loop
# break interrompe apenas um loop, permitindo que o programa continue
# executando apos o loop

for i in range(5):
    if i == 3:
        break 
    print (i)
print (f'Valor{i}')