print("Bem-vinda Professora Aline, ao Sistema de Contagem de Cédulas!")

candidatos = []
for i in range(3):
    nome = input(f"Digite o nome do candidato:")
    candidatos.append(nome)
    
votos = {candidato: 0 for candidato in candidatos}

total_votos = int(input("Digite o número total de votos a serem contados:"))

for voto in range(total_votos):
    while True:
        voto_candidato = input(f"Voto {voto+1} - Digite o nome do candidato:")
        if voto_candidato in votos:
            votos[voto_candidato] += 1
            break
        else:
            print("Candidato não encontrado. Insira um nome válido.")
            
        
print("\nResultado da Eleição:")
for candidato, num_votos in votos.items():
    print(f"{candidato} : {num_votos} votos")
    

max_votos = max(votos.values())
vencedores = [candidato for candidato, voto in votos.items() if voto == max_votos]

if len(vencedores) > 1:
    print(f"\nHouve um empate entre {', '.join(vencedores)}. Todos com {max_votos} votos!")
else:
    print(f"\nO Vencedor é {vencedores[0]} com {max_votos} votos!")
