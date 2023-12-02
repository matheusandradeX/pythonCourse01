'''
Crie um função que aceita um número como entrada e retorna o quadrado desse número.
'''

numero = int(input("Digite um numero: "))

def funcaoQuadrado(x):
    quadrado  = x**2
    return quadrado


resultado = funcaoQuadrado(numero)


print(f'O quadrado de {numero} é {resultado}')

