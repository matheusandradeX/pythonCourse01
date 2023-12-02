'''
Para este desafio, crie um loop que peça ao usuário para digitar o nome de uma fruta.
Se a fruta digitada não foir 'abacate', o loop deve continuar pedindo ao usuário para digitar o nome de uma fruta.
Se a fruta for 'abacate', o loop deve terminar e o programa deve imprimir "Parabens você acertou a fruta!"
'''

fruta = input("Digite o nome de uma fruta: ")

while fruta != 'abacate':
    input("Digite novamente!")
    fruta = input("Digite o nome de uma fruta: ")
    if fruta.lower() == 'abacate':
        print("Parabens você acertou a fruta!")
