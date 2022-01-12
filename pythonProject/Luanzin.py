#A saga do Hello World

#Caso 1:
# print('Hello World')

#Operações:
# A = 1
# B = 2
# soma = A + B
# print(soma)

# A = 1
# B = 2
# subtracao = A - B
# print(subtracao)

# A = 1
# B = 2
# multiplicacao = A * B
# print(multiplicacao)

# A = 14
# B = 2
# divisao = A / B
# print(divisao)

# A = 14
# B = 2
# divisao = A // B
# print(divisao)

# A = 14
# B = 2
# resto = A % B
# print(resto)

#Operação + string

# o jeito certo:
# A = 14
# B = 2
# divisao = A // B
# print("O resultado é: " + str(divisao))

# A = 14
# B = 2
# divisao = A // B
# print("O resultado é: " + divisao)
# retornou: line 48, in <module>
#     print("O resultado é: " + divisao)
# TypeError: can only concatenate str (not "int") to str

#prioridade de operações

# A = 5 * 2 + 3
# print(A)
#
# A = 5 * (2 + 3)
# print(A)

#Fim da parte 1

# array list

# arr = [0, 2, 4, 6, 8]
# print(arr[2])

# arr1 =  [0, 2, 4, 6, 8]
# print(arr1[4])

# katze = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(katze[6]) fiz certin

#Problema
arr = [1,2,3,4,5,6]
print(arr[5.5])

#detalhe
# A = 13.90
# B = 2.40
# soma = A + B
# print( "Deu: " + str(soma))
# #Obs: se vc colocar 13,90 ele vai entender como um array, retornando: Deu: (13, 90, 2, 40). Se não for array
# #Mas sim número decimal, use o ponto para separar as casas decimais, bem.