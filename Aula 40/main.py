#Python Object-Oriented Programming

#Classes
    # Utilizadas para criar Objetos (instances)
    # Objetos são partes dentro de uma Class (instancias)
    # Classes são utilizadas para agrupar dados funções, podemos ser reutulizadas
    # Exemplos
    # Class: Frutas
    # Objects: Abacate, Banana...


class Funcionarios:
    nome = 'Elena'
    sobrenome = 'Cabral'
    data_nascimento = '12/01/2009'

usuario1 = Funcionarios()

print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nascimento)
