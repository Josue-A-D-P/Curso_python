# Python object-oriented programming

# Classes
    # utilizadas para criar objetos (instances)
    # objetos são partes dentro de uma classe (intancias)
    # classes são utilizadas para sgrupar dados e funçoes, podendo reutilizar


#criar a classe
class Funcionarios:
    def __init__ (self, nome, sobrenome, data_de_nacimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_de_nacimento = data_de_nacimento

#criar o objeto
usuario1 = Funcionarios('Elena', 'cabral', '12/03/1999')
usuario2 = Funcionarios('Mario', 'Texeira', '12/03/1997')


#criar os parametros usuario1
'''
usuario1.nome = 'Elena'
usuario1.sobrenome = 'cabral'
usuario1.data_de_nacimento = '12/03/1999'


#criar os parametros usuario2
usuario2.nome = 'Mario'
usuario2.sobrenome = 'Texeira'
usuario2.data_de_nacimento = '12/03/1997'''


#print()
print(usuario1.nome)
print(usuario2.nome)