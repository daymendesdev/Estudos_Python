import math

#Operadores aritméticos

num1 = 2
num2 = 3

# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 % num2) #mostra o resto da divisao
# print(num1 ** num2)
# print(num1 // num2) #divide se as casas decimais



print(3 + 5 * 7 + 3)
#para fazer primeiro a soma e depois a multiplicação, fazemos da seguinte mandeira
print((3+5)*(7+3))

#para retornarmos um número ABSOLUTO, utilizamos a função
print(abs(-15))

#para fazer a exponenciação
print(pow(3,3))


#retorna o valor maximo, no caso, aqui é o 5
print(max(1,5,5,4,74,85,43))

#retorna o valor mínimo,no caso, aqui é o 1
print(min(1,4,74,58,5))

#retorna arredondamento por aproximação, ou seja, arredonda para o numero mais proximo
print(round(8.3))


#para utilizar a função de matematica fornecida pelo math, importate no início

#o floor arredonda para baixo
print(math.floor(8.8))

#o ceil arredonda para cima
print(math.ceil(8.8))
      
#funcção de raiz quadrada
print(math.sqrt(9))