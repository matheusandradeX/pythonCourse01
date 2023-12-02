'''
Para este desafio, crie uma lista com os nomes de três cidades. Peça ao usuário para digitar o nome de uma cidade.
Se a cidade estiver na lista, imprima "A cidade está na lista de cidades".
Se a cidade não estiver na tupla, imprima "A cidade não está na lista de cidades".
Obs. Você não pode utilizar list[]
'''


cidades  = {'São Paulo','Salvador','Minas Gerais'}



cidade = input("Digite o nome da cidade: ")


if cidade in cidades:
    print(f"A cidade {cidade} está na lista de cidades")        
else:
     print("Cidade não encontrada")
             