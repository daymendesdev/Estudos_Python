num1 = 5
num2 = 3.5

#Não sabe qual é o tipo de dado que está utilizando? basta usar a seguinte função:

#print (type(num1))

#Em seguida, será mostrado o tipo de variável na tela da seguinte maneira
# <class 'tipo'>

#para convertermos um dado
print("aqui está convertendo passando o número")
a = float(5)
print(a)

#também podemos fazer utilizando o nome da variável
print("aqui está convertendo passando a")
a = float(num1)
print(a)

#AGORA VAMOS CONVERTER DE FLOAT PAR AINTEIRO

print("convertendo de float para int")
b = int(num2)
print(b)

#Agora vamos converter de string para float e int

num3 = "10"
num4 = "15.5"
print(type(num3))
print(type(num4))

convert_num3 = int(num3)
print(convert_num3)
print(type(convert_num3))
convert_num4 = float(num4)
print(convert_num4)
print(type(convert_num4))


#para converter uma string com casa terminal para inteiro, devemos fazer assim:
convert_num5 = int(float("5.3"))
print(type(convert_num5))