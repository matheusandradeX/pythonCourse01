'''
Para este desafio, imagine que você tem uma loja de carros. Crie uma lista com os carros 
que você tem em estoque: BMW X6, BMW i5, BMW i8. Peça ao usuário para que ele insira o nome do carro que deseja comprar.
Se o carro estiver em estoque, imprima "Este carro está disponível". Se o carro não estiver em estoque, imprima "Desculpe, este carro não está disponível"
'''

estoque = ["BMW X6","BMW i5","BMW i8"]

carro = input("Digite o modelo do carro que deseja: ")


if carro in estoque:
    print("Carro tem em estoque")
else:
    print("Carro não tem em estoque")
