'''
Para este desafio, crie dois conjuntos, cada um contendo 5 nomes de seus amigos.
Alguns nomes devem estar presentes em ambos os conjuntos. 
Use um método para encontrar quais nomes aparecem em ambos os conjuntos e imprima o resultado
'''


conjuntoA = {'João','Maria','Ana','Bianca','Marcos'}

conjuntoB = {'Marcos','Paulo','Maria','Bianca','Paula'}



resultado = conjuntoA.intersection(conjuntoB)

print(resultado)