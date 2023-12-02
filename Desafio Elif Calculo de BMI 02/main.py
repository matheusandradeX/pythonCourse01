# Calculo de IMC - Indice de Massa Corporal

'''
Qual é sua Altura em cm:
Qual é o seu peso em kg:

Menor que 18,5 Magro
Entre 18,5 e 24,9 Normal
Entre 25,0 e 29,9 Sobrepeso 
Entre 30,0 e 39,9 Obesidade
Maior que 40,0 Obesidade Grave
'''
def imc(altura,peso):
    result = peso/(altura **2)
    return result

altura = float(input("Qual é sua altura em metros: "))
peso = float(input("Qual é o seu peso em Kg: "))

resultado = imc(altura,peso)

print(resultado)

if resultado <18.5:
    print("Seu IMC é "+str(resultado)+" Magro")
elif  resultado >= 18.5 and resultado <24.9:
    print("Seu IMC é "+str(resultado)+" Normal")
elif resultado >= 25.0 and resultado <29.9:
    print("Seu IMC é "+str(resultado)+" Sobrepeso")
elif resultado >= 30.0 and resultado <39.9:
    print("Seu IMC é "+str(resultado)+" Obesidade")
elif resultado > 40:
    print("Seu IMC é "+str(resultado)+" Obesidade Grave")



