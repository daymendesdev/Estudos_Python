minha_string = "qualquer Texto"

print(f"concatenar {minha_string} em string")

#deixando minha string toda em maiúscula utilizando função
print(minha_string.upper())

#deixando tudo em minúsculo
print(minha_string.lower())

#deixando a primeira letra do paragrafo maiúscula
print(minha_string.capitalize())

#para retornar um bool se é maiúsculo
print(minha_string.isupper())

#para tetornar um bool se é minusculo
print(minha_string.islower())

#remover os espaços antes e depois
print(minha_string.strip())

#substituir algo da string
print(minha_string.replace("qualquer","Meu",1)) #esse um significa que só quero subsituir o primeiro, se tiver mais partes no texto com o parametro que passei, ele não subistituirá

#contar quantas letras tem na string
print(len(minha_string))

#para pegarmos letras a parte
print(minha_string[5:8])
#de trás para a frente
print(minha_string[-4:-1])

#pegar o primeiro index de um texto
#ex: o texto é "qualquer texto"
#indice         01234567891111

print(minha_string.index("quer"))

#verificar se uma palavra existe na string

x = "texto" in minha_string
print(x)

#string com multiplas linhas
#utilizamos 3 "'", veja o exemplo a seguir

string_teste = """
linha1
linha2
linha3
"""

print(string_teste)

#Ou podemos fazer de um jeito mais simples

string_teste2 = "linha1\nlinha2\nlinha3\n"
print(string_teste2)