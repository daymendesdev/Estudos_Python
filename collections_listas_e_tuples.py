#Lista com strings
familia = ["Wellyngton","Dayanne","ingrid","Jeniffer","Joel","Yasmim","Junior"]

#para vermos a lista
print(familia)
#Para acessar um determinado elemento da lista, utilizamos o índice
print(familia[1])
#Lista com números

#para pegar a lista de trás para frente
print(familia[-1])

#para pegar mais de um registro(o ": " vai ser pego o registro do índice 2 para a frente)
print(familia[2:]) 

#para pegar apenas alguns, excluíndo o 3, ou seja, pega até o índice 2
print(familia[0:3])

#para mudarmos um valor
familia[1] = "linda da Day"
print(familia)

#para adicionar uma outra lista(complemento) à sua lista
familia.extend(["José","Ivete"])
print(familia)

#para adicionar apenas um valor a lista
familia.append("Ana Carolina")
print(familia)

#para escolher em qual índice você vai adicionar o valor a lista
familia.insert(1,"Dadadayyy")
print(familia)

#Remove o último elemento da lista por padrão.
familia.pop() 

#escolher qual vai remover
familia.remove("Dadadayyy")
print(familia)

#apagar todos os registro da lista
#familia.clear()
#print(familia)

#retornar o indice com base no valor
print(familia.index("Yasmim"))

#Para saber quantos valores iguais eu tenho dentro de uma lista
print(familia.count("Yasmim"))

idades = [28,26,24,22,20,18,11,59,49]
#para ordenar uma lista de inteiros na ordem ascendente(se eu fizer isso com a lista de strings, ele vai retornar em ordem alfabética)
idades.sort()
print(idades)

#para inverter uma lista
familia.reverse()
print(familia)

#O .sort seguido do .reverse retorna o inverso em ordem

#para creferenciar uma lista para outra variável
familia2 = familia
print(familia)

#para fazer uma copia da lista( diferente do modelo acima, no modelo a seguir, se você alterar algo na variável de origem, essa continua a mesma)
familia2 = familia.copy()



##############################

                ###TUPLES###

#A diferença entre a lista e o tuple, é que o tuple é inalterável, ou seja, não pode ser alterado.

#exemplos
#nesse exemplo é uma list, vamos remover um índice da mesma
coordenadas = [-54.1022, 129.0681]
coordenadas.pop()
print(coordenadas)

#agora veremos um tuple
#nesse, se eu usar algum metodo de remover ou adicionar, ele dará erro
#todas as outras funções que não alteram, removem ou adicionam são válidas
#coordenadas2 = (-54.1022, 129.0681)
#coordenadas2.pop()
#print(coordenadas2)

