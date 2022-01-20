#Operações

# a = 6
# b = 8
# soma = a + b
# print('A soma é: ' +  str(soma))

# S = 10
# Se = 10
# multiplicacao = S * Se
# print('o resultado é obviamente: ' + str(multiplicacao))

# A = 500
# B = 3
# divisao = A % B
# print(divisao) retorna o resto da divisão

#curiosidades:
# A = 500
# B = 3
# divisao = A // B
# print(divisao) não me devolve o tal do resto do float

# A = 5 * 3 + 2
# print(A) nesse ele prioriza a multiplicação mesmo sem eu dizer, e me devolve 17
#
# A = 5 * (3 + 2)
# print(A) nesse a prioridade é a adição, então ele me dá 25

#aqui

# usar só:
# n
# me devolve:
# Traceback (most recent call last):
#   File "C:/Users/Sales/programming/cursos-sabrina/DIO/intro-phyton-dio/pythonProject/practice.py", line 13, in <module>
#     n
# NameError: name 'n' is not defined

#list
# arr = [0, 2, 4, 6, 8]
# print(arr[2])
#
# arr1 =  [0, 2, 4, 6, 8]
# print(arr[4])
#
# katze = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(katze[6]) fiz certin

#If

# batata = 'saborosa'
# if batata == 'horrível':
#     print('credo!')
# else:
#    print('Que delicia!')

# dia =  'bom'
# if dia == 'bom':
#     print('Incrível, fico feliz!')
# else:
#     print('O que houve?')

#  x = int(input("Please enter an integer: "))
# Please enter an integer: 42:
#  if x < 0:
#      x = 0
#      print('Negative changed to zero')
#  elif x == 0:
#      print('Zero')
#  elif x == 1:
#     print('Single')

# x = 12
# if x > 20:
#     print('nein')
# elif x == 12:
#     print('Zwolf')

# z = 'zebra'
# if z != 'zebra':
#     print('cavalo?')
# elif z == 'zebra':
#     print('fofinha hihi')

#prática depois da observação de hoje

# b = 5 * 4
# while b == 20:
#     print('Du bist klug')


# c = 4 * 9 + 2
# if c > 32:
#     print('cool')
# else:
#     print('shut up bitch')

#//////////////////////////////////////////////////////////só a prática (como sempre)

# a = 3
# b = 2
# soma = a + b
# print('A soma é:' + str(soma))

# a = 1
# b = 2
# c = 0
# conta = a + b * c
# print(conta) ele fez 2 * 0 + 1

# a = 1
# b = 2
# c = 0
# conta = (a + b) * c
#print(conta) deu 0

# car = 'legal'
# if car == 'legal' :
#     print('nice')
# else :
#     print('bão')

# car = 'chevette'
# if car == 'fusca' :
#     print('bonitin')
# else :
#     print('aaa é qual então? ')

# zimmer = 1
# while zimmer == 1 :
#     print('stonks')

#Mais conceitos, pois entendi os de cima bem

#for - measuring strings

# words = ['cat', 'window', 'likes']
# for w in words:
#      print (w)
#
# nomes = ['Pedro', 'João', 'Leticia']
# for n in nomes:
#      print(n)

# Repetindo tudo que há fiz para relembrar. dia 12/01/2022

#operações normais

#soma
# S = 2
# T = 3
# multiplicacao = 2 + 3
# print (multiplicacao)

#subração
# S = 6
# R = 6
# subtracao = S - R
# print(subtracao)

#multiplicação
# A = 15
# B = 3
# multiplicacao = A * B
# print(multiplicacao)

#Divisão
# A = 25
# B = 5
# divisao = A / B
# print(divisao)
# me dá 5.0

#Resto
# A = 25
# B = 5
# resto = A % B
# print(resto)

#Operações com strings

#Soma
# A = 13.90
# B = 2.40
# soma = A + B
# print( "Deu: " + str(soma))
# #Obs: se vc colocar 13,90 ele vai entender como um array, retornando: Deu: (13, 90, 2, 40). Se não for array
# #Mas sim número decimal, use o ponto para separar as casas decimais, bem.

#Subtração
# A = 13.90
# B = 2.40
# sub = A - B
# print( "Deu: " + str(sub))
# deu 11.5

#Multiplicacao
# A = 2.25
# B = 4
# multiplicacao = A * B
# print("Deu:" + str(multiplicacao))

#Divisao
# A = 2.25
# B = 4
# divisao = A / B
# print("Deu:" + str(divisao))

#Detalhes adicionais
# A = 500
# B = 3
# divisao = A // B
# print(divisao) não me devolve o tal do resto do float

# A = 5 * 3 + 2
# print(A) nesse ele prioriza a multiplicação mesmo sem eu dizer, e me devolve 17
#
# A = 5 * (3 + 2)
# print(A) nesse a prioridade é a adição, então ele me dá 25

#Se eu esqueci, não treinei o suficiente, bora!

# A = 300
# B = 2
# div = A // B
# print(div)
# deu 150 bem safe


# B = 150000
# C = 50
# div = B // C
# print(div)
# como o planejado

# caixas = 300
# pedidos = 25
# div = caixas //pedidos
# print(div)
# 12 yeee

#Sobre prioridade de operações

# N = 1 * 4 + 15
# print(N)
#multiplicação primeiro, deu 19

# N = 1 * (2 + 15)
# print(N)

#Tá ótimo fia! Próxima parte

#20/01 revendo

# a = 1200
# b = 300
# divisao = a // b
# print (divisao)

# a = 12.5
# b = 3
# divisao = a // b
# print (divisao)
# como o esperado

# Entendendo elif

# cor = 2
#
# if cor == 3:
#     print('Nice, another color set selected')
# elif cor == 1:
#     print('As default')
# else:
#     print('Uh...okay then')
# Clean as water


# nummer = 'NaN'
# nummer = 3
# nummer = 'ost'
# if nummer == 'NaN':
#     print('cool')
# elif nummer == 3:
#     print('alright')
# else:
#     print('anyways...')

# catNummer = 0
#
# if catNummer == 1:
#     print('OWWWW which is your cats name?')
# elif catNummer > 1:
#     print('Woooow! How much do you have, then?')
# elif catNummer == 0:
#     print('Aaaa..but why? Dont you like them?')

#laços de repetição: for

#Exemplo base
# nomes = ['Pedro', 'João', 'Leticia']
# for n in nomes:
#      print(n)
#Ok
#
# nomesGatos = ['Al', 'Bella', 'Knuckles', 'Botinhas']
# for n in nomesGatos:
#      print(n, len(n))
# else:
#      print('Os nomes dos meus gatos são esses')
#FUNCIONOU WEEEEE

# Zimmer = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in Zimmer:
#     print(i)

#Boa, finalmente eu entendi

# numero = [1, 2, 3, 4]
# for n in numero:
#     print(n)

#parei aqui. faça funcionar
# words = ['cat', 'window', 'defenestrate']
# for w in words[:]:
#   if len(w) > 6:
#   words.insert(0, w)
#  print(n)
#













