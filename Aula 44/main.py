#Python Object-Oriented Programming

#Classes
    # Utilizadas para criar Objetos (instances)
    # Objetos são partes dentro de uma Class (instancias)
    # Classes são utilizadas para agrupar dados funções, podemos ser reutulizadas
    # Exemplos
    # Class: Frutas
    # Objects: Abacate, Banana...
from datetime import datetime

class Funcionarios:
    def __init__(self,nome,sobrenome,ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int( ano_atual - self.ano_nascimento)
        return self.ano_nascimento

#Criar o objeto
usuario1 = Funcionarios('Elena','Cabral',2009)
usuario2 = Funcionarios('Carol','Silva',2005)
usuario3 = Funcionarios('Andre','Iacono',2003)


print(Funcionarios.idade_funcionario(usuario1))