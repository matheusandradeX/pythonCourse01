'''
Para este desafio, crie uma lista com 5 nomes de países e as capitais desses países.
Peça ao usuário para digitar o nome de um país. Se o país estiver na lista, imprima
"A capital de [país] é [capital]". Se o país não estiver na lista, imprima "Desculpe não temos informações sobre a capital desse país".
'''

paises = {'Brasil':'Brasilia','Argentina':'Buenos Aries','Venezuela':'Caracas'}

país = input("Digite o nome do país: ")


if país in paises:
    print(f"A capital de {país} é {paises[país]}")
else:
    print('Desculpe não temos informações sobre a capital desse país')

