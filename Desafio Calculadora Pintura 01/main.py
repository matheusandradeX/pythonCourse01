'''
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede. O usuário deverá fornecer as seguintes informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tintas
'''

rendimento = int(input("Digite o rendimento: "))

altura = int(input("Digite a altura em metros: "))

largura = int(input("Digite a largura em metros: "))


def calculo(x,y,z):
    area = (y*z)/x
    return area

resultado = calculo(rendimento,altura,largura) 
print(f'O rendimento da tinta é de {resultado} latas de tintas')