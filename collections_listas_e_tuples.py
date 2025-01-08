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

#para adicionar outro valor a lista
familia.extend(["José","Ivete"])
print(familia)