'''
Criar um programa que dependendo da temperatura (em Celsius) do steak
ele retorna o ponto de cozimento em portugues. O usuário deverá fornecer a temperatura

Temperaturas - Cozimento
120°F ou 48°C - Rare (Selada)
130°F ou 54°C - Medium rare (Ao ponto para mal)
140°F ou 60°C - Medium (Ao ponto)
150°F ou 65°C - Medium well (Ao ponto para o bem)
160°F ou 71°C - Well done (Bem passada)
'''

ponto_carne = int(input("Digite a temperatura da carne : "))


if ponto_carne <48:
    print("You must heat more")
elif ponto_carne in range(48,53):
    print(" Medium rare")
elif ponto_carne in range(54,59):
    print("Medium")
elif ponto_carne in range(60,64):
    print("Medium well")
elif ponto_carne in range(65,70):
    print("Well done ")
else:
    print("Digite um valor valido")

