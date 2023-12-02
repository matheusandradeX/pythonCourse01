'''
Para este desafio, crie uma função que calcule a potência de um número. 
A função deve aceitar dois argumentos: a base e o expoente. No entanto, 
se o expoente não for fornecido ao chamar a função, ele deve assumir o valor padrão de 2;
'''

def calculo (x,y=2):
    return x ** int(y) 

base = int(input("Digite a base: "))
expoente = input("Digite o expoente: ")


if expoente:
    print(f'O resultado é {calculo(base,expoente)}')
else:
    print(f'O resultado é> {calculo(base)}')