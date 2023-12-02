# Listas 
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variavel

cor_cliente = input('Digite a cor desejada: ')
cores = ['amarelo','verde','azul','vermelho']

if cor_cliente.lower() in cores:
    print('Em estoque')
else:
    print('Não ')