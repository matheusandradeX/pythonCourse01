'''
Para este desafio, crie duas funções. A primeira função deve aceitar um número e retornar o dobro desse número.
A segunda função deve aceitar um número e retornar o quadrado desse npumero.
Em seguida, chame a primeira função dentro da segunda para retornar o quadrado do dobro de um número.
'''
n = 2

def dobro(n):
    return n*2

def quadrado(n):
    return dobro(n)**2

print (f"O quadrado do dobro é {quadrado(n)}")


