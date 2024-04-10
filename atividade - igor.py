i = 0
qtdVotosUm = 0
qtdVotosDois = 0
qtdVotosTres = 0
empate = 0


candidatoUm = input('Digite o nome do primeiro Candidatos: ')
candidatoDois = input('Digite o nome do segundo Candidatos: ')
candidatoTres = input('Digite o nome do terceiro Candidatos: ')

qtdVotos = int(input('\nDigite a quantidade de Votos a serem realizados: '))

print(f'\n Candidatos \n 1 - {candidatoUm}\n 2 - {candidatoDois}\n 3 - {candidatoTres}')

while i < qtdVotos:
    voto = input('\nDigite o seu Voto: ')
    
    if voto.lower() == candidatoUm.lower():
        qtdVotosUm += 1
        i += 1
        
    elif voto.lower() == candidatoDois.lower():
        qtdVotosDois += 1
        i += 1
        
    elif voto.lower() == candidatoTres.lower():
        qtdVotosTres += 1
        i += 1
        
    else:
        print('Digite um candidato valido')
        i -= 1
        qtdVotos -= 1
        
if qtdVotosUm == qtdVotosDois and qtdVotosDois == qtdVotosTres:
    
    empate = 1

    print(f'\n\nTodos os Candidatos empataram, com {qtdVotosUm} votos')


elif qtdVotosUm == qtdVotosDois or qtdVotosUm == qtdVotosTres:
    
    empate = 1
    
    if qtdVotosUm == qtdVotosDois:
        print(f'\n\n{candidatoUm} empatou com {candidatoDois},  com {qtdVotosUm} votos')
        
    elif qtdVotosUm == qtdVotosTres:
        print(f'\n\n{candidatoUm} empatou com {candidatoTres}, com {qtdVotosUm} votos')
        
        
    
elif qtdVotosDois == qtdVotosUm or qtdVotosDois == qtdVotosTres:
    
    empate = 1
    
    if qtdVotosDois == qtdVotosUm:
        print(f'\n\n{candidatoDois} empatou com {candidatoUm},  com {qtdVotosDois} votos')
        
    elif qtdVotosDois == qtdVotosTres:
        print(f'\n\n{candidatoDois} empatou com {candidatoTres}, com {qtdVotosDois} votos')
    
    
    

elif empate == 0 and qtdVotosUm > qtdVotosDois and qtdVotosUm > qtdVotosTres:
    print(f'\n\nCandidato {candidatoUm} Foi o Vencedor com {qtdVotosUm} Votos')
    
elif empate == 0 and  qtdVotosDois > qtdVotosUm and qtdVotosDois > qtdVotosUm:
    print(f'\n\nCandidato {candidatoDois} Foi o Vencedor com {qtdVotosDois} Votos')
    
elif empate == 0 and  qtdVotosTres > qtdVotosUm and qtdVotosTres > qtdVotosDois:
    print(f'\n\nCandidato {candidatoTres} Foi o Vencedor com {qtdVotosTres} Votos')
    

print(f'\nA Votação terminou da seguinte forma\n 1 - {candidatoUm} - {qtdVotosUm} Votos\n 2 - {candidatoDois} - {qtdVotosDois} Votos\n 3 - {candidatoTres} - {qtdVotosTres} Votos\n')