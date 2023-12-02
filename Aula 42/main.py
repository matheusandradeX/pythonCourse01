#Python Object-Oriented Programming

#Classes
    # Utilizadas para criar Objetos (instances)
    # Objetos são partes dentro de uma Class (instancias)
    # Classes são utilizadas para agrupar dados funções, podemos ser reutulizadas
    # Exemplos
    # Class: Frutas
    # Objects: Abacate, Banana...

class Funcionarios:
    def __init__(self,nome,sobrenome,data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento


#Criar o objeto
usuario1 = Funcionarios('Elena','Cabral','12/01/2009')
usuario2 = Funcionarios('Carol','Silva','15/10/2005')
usuario3 = Funcionarios('Andre','Iacono','11/03/2003')



print(usuario1.nome)
print(usuario2.data_nascimento)
print(usuario3.data_nascimento)
