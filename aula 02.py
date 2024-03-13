#                         VERIFICAR SE É MENOR OU MAIOR QUE 10 

# resposta = int(input("digite um numero: "))


# if resposta>10:
#     print("o numero digitado é maior que 10, ", resposta, " foi o numero digitado")
    

# elif resposta == 10:
#     print("o numero digitado é igual a 10, ", resposta, " foi o numero digitado")

# else:
#     print("o numero digitado é menor que 10, ", resposta, " foi o numero digitado")

#_______________________________________________________________________________________



#                         HORAS TRABALHADAS

# import os
# import time

# os.system('cls')

# def teste(): 
#     NHT = int(input("Digite a Quantidade de Horas Trabalhadas: "))
#     VPH = int(input("Digite o Valor Pago Por Hora: "))

#     SB = NHT * VPH

#     if SB < 1000:   
#         Desconto = SB * (5/100)
#         SL = SB - Desconto
#         print("O Salario Bruto Corresponde a: ", SB)
#         print("O Valor a Ser Descontado a: ", Desconto)
#         print("O Salario Liquido Corresponde a: ", SL)
#         time.sleep(3)
#         os.system('cls')
#         teste()
        
#     elif SB > 1000 and SB <=2000:
#         Desconto = SB * (10/100)
#         SL = SB - Desconto
#         print("O Salario Bruto Corresponde a: ", SB)
#         print("O Valor a Ser Descontado a: ", Desconto)
#         print("O Salario Liquido Corresponde a: ", SL)
#         time.sleep(3)
#         os.system('cls')
#         teste()
        
#     else:
#         Desconto = SB * (15/100)
#         SL = SB - Desconto
#         print("O Salario Bruto Corresponde a: ", SB)
#         print("O Valor a Ser Descontado a: ", Desconto)
#         print("O Salario Liquido Corresponde a: ", SL)
#         time.sleep(3)
#         os.system('cls')
#         teste()
    
# teste()

#____________________________________________________________________________________

#                          Calculo IMC


import os
import time

os.system('cls')

def CalculoIMC(): 
    Nome = input("Digite o seu Nome: ")
    Altura = float(input("Digite a sua Altura: "))
    Peso = float(input("Digite o Seu Peso: "))
    
    IMC = Peso / (Altura**2)
    
    if IMC < 18.5:
        print("Olá %s, \nAtualmente você possui %f de Percentual de Gordura  \nSe Classifica como Abaixo do Peso" % (Nome, IMC))
        
    elif IMC >= 18.5 and IMC <= 24.9:
        print("Olá %s, \nAtualmente você possui %f de Percentual de Gordura  \nSe Classifica como Peso Normal" % (Nome, IMC))
    
    elif IMC >= 25 and IMC <= 29.9:
        print("Olá %s, \nAtualmente você possui %f de Percentual de Gordura  \nSe Classifica como Levemente Acima do Peso" % (Nome, IMC))
    
    elif IMC >= 30 and IMC <= 34.9:
        print("Olá %s, \nAtualmente você possui %f de Percentual de Gordura  \nSe Classifica como Obesidade 1" % (Nome, IMC))
        
    elif IMC >= 35 and IMC <= 39.9:
        print("Olá %s, \nAtualmente você possui %f de Percentual de Gordura  \nSe Classifica como Obesidade 2 (Severa)" % (Nome, IMC))
    
    else:
        print("Olá %s, \nAtualmente você possui %f de Percentual de Gordura  \nSe Classifica como Obesidade Mórbida" % (Nome, IMC))

CalculoIMC()


