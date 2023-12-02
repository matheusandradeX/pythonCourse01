'''
Para este desafio, crie uma lista de número de 1 a 10. Use um 'for loop' para iterar sobre a lista.
Se o número atual da iteração for par, imprima "O número [número] é par".
Se o número for ímpar, imprima "O número [número] é impar".
'''


numeros = [1,2,3,4,5,6,7,8,9,10]

i = 0

while i <10:
    if numeros[i]%2:
        print(f'O numero {numeros[i]} é impar')
    else:
         print(f'O numero {numeros[i]} é par')
    i =i+1
