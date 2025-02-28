#lugar para guardar funções, comportamentos e funcionalidades relacionadas em um único lugar que pode ser replicado
#e modificado quantas vezes necessário

class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero
    
    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.genero}."
    
    def envelhecer(self, anos=1):
        self.idade += anos
        return f"{self.nome} agora tem {self.idade} anos."

# Exemplo de uso 
pessoa1 = Pessoa("Dayanne", 25, "Feminino")
print(pessoa1.apresentar())
pessoa1.envelhecer(2)
print(pessoa1.apresentar())


class Carro:
    def __init__(self, cor, modelo, preco):
        self.cor = cor
        self.modelo = modelo
        self.preco = preco
    def LigarCarro(self):
        print(f'Ligando o carro {self.modelo}')

mustang=Carro('Laranja', 'Mustang GT','350000')
mustang.LigarCarro()