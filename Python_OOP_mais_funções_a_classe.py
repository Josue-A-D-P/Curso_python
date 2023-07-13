from datetime import datetime

# Python object-oriented programming

# Classes
    # utilizadas para criar objetos (instances)
    # objetos são partes dentro de uma classe (intancias)
    # classes são utilizadas para sgrupar dados e funçoes, podendo reutilizar


#criar a classe
class Funcionarios:
    def __init__ (self, nome, sobrenome, ano_de_nacimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_de_nacimento = ano_de_nacimento


    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome       


    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_de_nacimento = int (ano_atual - self.ano_de_nacimento)
        return self.ano_de_nacimento


#criar o objeto
usuario1 = Funcionarios('Elena', 'cabral', 1999)
usuario2 = Funcionarios('Mario', 'Texeira', 1997)

print(Funcionarios.nome_completo(usuario1))
print(Funcionarios.idade_funcionario(usuario1))
print()
print(Funcionarios.nome_completo(usuario2))
print(Funcionarios.idade_funcionario(usuario2))