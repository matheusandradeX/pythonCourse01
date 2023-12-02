'''
Para este desafio, crie uma lista de frutas e outra de vegetais.
Use um "for loop" aninhado (nested for loop) para imprimir todas as 
combinações possíveis de frutas e vegetais, com a fruta primeiro e o
vegetal em segundo
'''


frutas  = ['maça','peira','uva','laranja']
vegetais = ['alface','beteraba','rucula','reponho']





for x  in frutas:
    for y in vegetais:
        print(x,y)
