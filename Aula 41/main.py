#Python Object-Oriented Programming

#Classes
    # Utilizadas para criar Objetos (instances)
    # Objetos são partes dentro de uma Class (instancias)
    # Classes são utilizadas para agrupar dados funções, podemos ser reutulizadas
    # Exemplos
    # Class: Frutas
    # Objects: Abacate, Banana...

class Funcionarios:
    pass

#Criar o objeto
usuario1 = Funcionarios()
usuario2 = Funcionarios()

#Criar os parametros do usuario1
usuario1.nome = 'Elena'
usuario1.sobrenome = 'Cabral'
usuario1.data_nascimento = '12/01/2009'

#Criar os parametros do usuario2
usuario2.nome = 'Carol'
usuario2.sobrenome = 'Silva'
usuario2.data_nascimento = '15/10/2005'

#print

print(usuario1.nome)
print(usuario2.data_nascimento)
