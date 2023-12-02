'''
Para este desafio, crie uma lista de frutas que inclui "maça" três vezes e outras frutas de sua escolha.
Use um loop for para contar quantas vezes "maça" aparece na lista e imprima o resultado.
'''


frutas = ['maça','laranja','limão','maça','pera','maça']

count = 0 
for x  in frutas:
    if x == 'maça':
        count = count +1


print("A fruta maça apareceu "+str(count)+" vezes")