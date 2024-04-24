
# Em Java Script:

#   for (int i = 0, i < 0, i++){
#       console.log (i)   
#   }


#___________________________________________________________________________________________________________________________

# Em Python

#    for i in range (10):
#       print (i)
# 
#   Este codigo acima é a mesma coisa que o codigo escrito em JS 



#     for i in range (5,10):
#       print (i)
#
#   neste caso estamos dizendo que o i inicia-se em 5 e deverá rodar até chegar em 10

#     for i in range (10, 0, -1):
#       print (i)
#
#   neste caso estamos dizendo que o i inicia-se em 10 e deverá rodar até chegar em 0, sendo que ele sofre o decremento de -1

#___________________________________________________________________________________________________________________________

#   nomes = ["Aline", "Rita", "Sergio", "Ricardo", "Ariane", "Bernardo"]

#    for n in nomes:
#        print(n)





#___________________________________________________________________________________________________________________________

#                                 FEITO COM FOR

# Numero = int(input("Escolha um numero e descubra a taboada do mesmo: "))



# for n in range (11):
#     tabuada = Numero * n
#     print(f'{Numero} x {n} é: {tabuada}')
    
#___________________________________________________________________________________________________________________________



# NumeroDeNotas = int(input("Quantas notas você pretende Lançar?: "))
# Resultado = 0

# for i in range (NumeroDeNotas):
#     Notas = int(input(f"Lance a Nota {i}: "))
#     Resultado = Notas + Resultado 

# Resultado = Resultado/NumeroDeNotas
# print(f'A media geral é: {Resultado}')


#__________________________   NA FALTA DE 1 TEM DOIX   __________________________


# NumeroDeNotas = int(input("Quantas notas você pretende Lançar?: "))
# QtdNotas = []
# Resultado = 0
# for i in range (NumeroDeNotas):
#     Notas = int(input(f"Lance a Nota {i+1}: "))
#     QtdNotas.append(Notas)
#     Resultado = QtdNotas[i] + Resultado

# print('\n ________________________________________________________________________________________________________ \n')

# for x in range (NumeroDeNotas):
#     print(f'As notas digitadas foram: {QtdNotas[x]}')
    
# print(f'E a Media Correspondente a eles é de: {Resultado/NumeroDeNotas}')



#___________________________________________________________________________________________________________________________



#                                 FEITO COM WHILE

# Numero = int(input("Escolha um numero e descubra a taboada do mesmo: "))
# i=0

# while i <= 10:
#     tabuada = Numero * i
#     print(f'{Numero} x {i} é: {tabuada}')
#     i+=1


#___________________________________________________________________________________________________________________________


# NumeroDeNotas = int(input("Quantas notas você pretende Lançar?: "))
# Resultado = 0
# i=0

# while i < NumeroDeNotas:
#     Notas = int(input(f"Lance a Nota {i}: "))
#     Resultado = Notas + Resultado 
#     i+=1

# Resultado = Resultado/NumeroDeNotas
# print(f'A media geral é: {Resultado}')