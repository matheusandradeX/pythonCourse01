# Filter Function 
    #Muito utilizado com listas
    #Aplicar uma função a um interable, filtrando os items. (List, tuple,dic,etc)

valores = [10,12,34,44,57]

def remover20(x):
    return x > 20

print(list(filter(remover20, valores)))

