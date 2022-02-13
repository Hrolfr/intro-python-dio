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

#primeiro treino do ano, dia 04/02/2022
#Refazendo os exemplos iee

#parte 0 - Operações

# a = 2
# b = 2
# soma = a + b
# print(soma)

# a = 2
# b = 2
# sub = a - b
# print(sub)

# a = 2
# b = 2
# mult = a * b
# print(mult)

# a = 2
# b = 2
# div1 = a / b
# print(div1)

# a = 2
# b = 2
# div2 = a // b
# print(div2)

# a = 2
# b = 2
# resto = a % b
# print(resto)

#0.1

# a = 2.5
# b = 2.5
# soma = a + b
# print(soma)
# devolve 5.0

# a = 2,5
# b = 2,5
# soma = a + b
# print(soma)
# devolve o array (2, 5, 2, 5)

# a = 144
# b = 2.5
# div = a / b
# print(div)
# devolveu 57.6

# a = 144
# b = 2.5
# div = a // b
# print(div)
# devolveu 57.0

# a = 144
# b = 2.5
# mult = a * b
# print(mult)
#devolveu 360.0

# a = 144
# b = 2.5
# sub = a - b
# print(sub)
# devolveu 141.5

# a = 144
# b = 2.5
# soma = a + b
# print(soma)
# devolveu 146.5

# a = 144
# b = 2.5
# resto = a % b
# print(resto)
# devolveu 1.5

#0.2 - prioridade de operações

# a = 500
# b = 150
# c = 25
# d = 0
# oper = a + b / c + d
# print(oper)
# #deu 506.0

# a = 500
# b = 150
# c = 25
# d = 0
# oper = a + b // c + d
# print(oper)
#deu 506

# a = 500
# b = 150
# c = 25
# d = 0
# oper = (a + b) / c + d
# print(oper)
# deu 26.0

# a = 500
# b = 150
# c = 25
# d = 0
# oper = (a + b) // c + d
# print(oper)
# deu 26

# a = 500
# b = 150
# c = 25
# d = 0
# oper = a + b / (c + d)
# print(oper)
# deu 506.0

#parte 1 - array

#list exemplos
# arr = [0, 2, 4, 6, 8]
# print(arr[2])
#1
# arr1 =  [0, 2, 4, 6, 8]
# print(arr[4])
#2
# katze = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(katze[6]) fiz certin

# heroi = ['batman','superman', 'lanterna-verde', 'arqueiro-verde', 'flash']
# print(heroi[4])
#me devolveu o flash
#
# heroi = ['batman','superman', 'lanterna-verde', 'arqueiro-verde', 'flash']
# print(heroi[2])
#lanterna verde
#
# heroi = ['batman','superman', 'lanterna-verde', 'arqueiro-verde', 'flash']
# print(heroi[1])
#superman

# arr = [1, 3, 6, 10, 15, 21, 27, 35]
# print(arr[5])

# gatos =  ['branco', 'amarelo', 'cinza', 'siames', 'preto', 'tres cores']
# print(gatos[3])

#parte 2 - if, else e elif

#exemplo meu
# nummer = 'NaN'
# nummer = 3
# nummer = 'ost'
# if nummer == 'NaN':
#     print('cool')
# elif nummer == 3:
#     print('alright')
# else:
#     print('anyways...')

# cat = 'grey'
# if cat == 'grey':
#     print('Love them')
# elif cat != 'grey' :
#     print('Which colour he has?')
# else:
#     print('Do not like cats?')

# carro = 'opalao'
# if carro == 'opalao':
#     print('chique')
# elif carro != 'opalao':
#     print('qual entao?')

# carro = 'grrr'
# if carro == 'opalao':
#      print('chique')
# elif carro == 'fusquinha':
#      print('qual entao?')
# else:
#      print('esse é bom também')
# Obs: se eu usar o != (no elif) e depois o else, ele sempre vai preferir a opção do elif

#parte 3 - for

#Exemplo base
# nomes = ['Pedro', 'João', 'Leticia']
# for n in nomes:
#       print(n)

# numero = [1, 2, 3, 4, 5, 6]
# for n in numero:
#      print(n)

# nomesGatos = ['Al', 'Bella', 'Knuckles', 'Botinhas']
# for n in nomesGatos:
#        print(n, len(n))
# else:
#        print('Os nomes dos meus gatos são esses')

# Zimmer = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in Zimmer:
#     print(i)

# numero = [1, 2, 3, 4]
# for n in numero:
#     print(n)

# words = ['cat', 'window', 'defenestrate']
# for w in words:
#   print(w)

# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))
#wtf, funcionou

# numbers = [12, 5, 7]
# for n in numbers:
#     print(n)

#itens novos

#range()

#exemplo 1
# for i in range(5):
#     print(i)

# for i in range(10):
#    print(i)
# do 0 até o 9

# for i in range(5, 10):
#     print(i)
# vai do 5 até o 9

# for i in range(5, 11):
#     print(i)
# vai do 5 até o 10

# for i in range(0, 10, 3):
#  print(i)
#trás 0, 3, 6, 9

# for i in range(-10, -100, -30):
#  print(i)
#-10, -40, -70

# for i in range(-10, -100, -50):
#      print(i)
#deu -10, -60, -

# for i in range(-10, -200, -50):
#     print(i)
#deu -10, -60, -110, -160

#agora entendi certinho, era relativo a números aleatórios, assim como dizia na documentação.

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])
#     0 Mary
#     1 had
#     2 a
#     3 little
#     4 lamb

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(range(10))
# wtf??????

#dia 13/02/2022

#revisando o for

# words = ['cat', 'window', 'defenestrate']
# for w in words:
#   print(w)

# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))
#wtf, funcionou

# words = ['viking', 'axe', 'sword', 'shield']
# for i in words:
#      print(i)

# words = ['viking', 'axe', 'sword', 'shield']
# for i in words:
#      print(i, len(i))

# words = ['kid', 'candy', 'toys', 'colours']
# for w in words:
#     print(w)

# words = ['kid', 'candy', 'toys', 'colours']
# for w in words:
#     print(w, len(w))

# oc = ['bob esponja', 'patrick', 'lula molusco', 'seu cirigueijo']
# for o in oc:
#     print(o)

# oc = ['bob esponja', 'patrick', 'lula molusco', 'seu cirigueijo']
# for o in oc:
#     print(o, len(o))

# oc2 = ['bob esponja', 'patrick', 'lula molusco', 'seu cirigueijo'], ['gary', 'sardinhas', 'mae do bob']
# for o in oc2:
#     print(o)

# oc2 = ['bob esponja', 'patrick', 'lula molusco', 'seu cirigueijo'], ['gary', 'sardinhas', 'mae do bob']
# for o in oc2:
#     print(o, len(o))
#o curioso é que ele não conta as letras do array, mas sim as palavras de ambos

# oc2 = ['bob esponja', 'patrick', 'lula molusco', 'seu cirigueijo'], ['gary', 'sardinhas', 'mae do bob']
# for o in oc2:
#     print(o, len(o))

#voltando range()

#exemplos base

# for i in range(5):
#     print(i)

# for i in range(5, 11):
#     print(i)

# for i in range(0, 10, 3):
#  print(i)

# for i in range(-10, -100, -30):
#  print(i)
#-10, -40, -70

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])
#     0 Mary
#     1 had
#     2 a
#     3 little
#     4 lamb

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(range(10))

#experimentos

# for i in range(9):
#     print(i)
#do 0 até o 8

# for i in range(4):
#     print(i)

# for i in range(1, 200):
#     print(i)
# do 1 até 199

# for i in range(2, 14):
#     print(i)
# do 2 até o 13

# for i in range(0, 50, 5):
#     print(i)
# faz a tabuada do 5 do 0 ao 45

# for i in range(0, 55, 5):
#     print(i)
# vai do 0 até o 50

# for i in range(0, 22, 2):
#     print(i)

# for i in range(0, 33, 3):
#      print(i)

# for i in range(0, 110, 10):
#     print(i)

# for i in range(-10, -100, -30):
#   print(i)
#-10, -40, -70

# for i in range(-20, -100, -50):
#     print(i)
#-20, -70

# for i in range(-20, -200, -50):
#     print(i)
#gerou -20 -70 -120 -170

# for i in range (-30, -300, -80):
#     print(i)
#gerou -30, -110, -190, -270
