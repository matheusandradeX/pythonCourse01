'''
Para este desafio, crie uma função lambda que eleve um número ao quadrado. 
'''

numeros = [1,2,3,4,5,6,7,8]

quadrado = lambda num: num ** 2 
resultados = []

for i in numeros:
    resultados.append(quadrado(i))


print(f'Os quadrados dos numeros {numeros} são {resultados}')