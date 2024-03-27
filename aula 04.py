# 1 ____________________________________________________

# Palavra =input("Digite uma palavra: ")

# print('Essa palavra possui', len(Palavra), 'caracteres')

# 2 ____________________________________________________

# letra =input("Digite a letra que você deseja contar: ")
# Palavra =input("Digite uma palavra: ")

# print('Essa palavra possui', Palavra.count(letra), 'caracteres a em sua composição')


# 3 ____________________________________________________


# numeroPalavras =int(input("quantas palavras você deseja listar?: "))
# palavras = []

# for n in range (numeroPalavras):
#     palavra =input("Digite uma palavra: ")
#     palavras.append(palavra)

# print(" ".join(palavras))



# 4 ____________________________________________________


# palavra = input("escreva uma palavra: ")

# print('essa palavra ficaria', palavra[::-1], 'invertida')


# 5 ____________________________________________________

palavra = input("escreva uma palavra: ")
palavra = palavra.lower()
verificação = palavra.split(" ")
junção = len(verificação)
teste = " "

for n in range (junção):
    teste = teste + verificação[n]

teste = teste.strip()

if teste == teste[::-1]:
   print('essa palavra é um palindromo')
    
else:
  print('essa palavra NÃO é um palindromo')