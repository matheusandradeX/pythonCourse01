'''
Para este desafio, crie uma função que aceite dois números como entrada e retorne a soma desses números.
'''


def soma(x,y):
    resultado = x +y
    return resultado

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

print(f'A soma dos numeros {numero1} e {numero2} é {soma(numero1,numero2)}')