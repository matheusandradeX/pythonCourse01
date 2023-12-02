'''
Neste desafio, quero que você crie um script que 
solicite ao usuário dois números. Em seguida, 
seu script deve imprimir a soma, a subtração, a multiplicação
a divisão (resultado decimal) e a exponenciação 
(primeiro número elevado ao segundo número) desses dois números
'''

numero1 = int(input("Digite o numero 1: "))
numero2 = int(input("Digite o numero 2: "))

soma = numero1 + numero2
multiplicacao = numero1 * numero2
divisao = numero1 /numero2
exponeciacao = numero1 ** numero2

print(f"Soma e {soma}")
print(f"multiplicacao e {multiplicacao}")
print(f"divisao e {int(divisao)}")
print(f"exponeciacao e {exponeciacao}")