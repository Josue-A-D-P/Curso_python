# Dicionarios 
    # Utiliza index no formato de keys e value
    # Aceita integer float string boolean...


aluno = {
    'Nome': 'Ana',
    'Idade': 16,
    'Nota_final': 'A', 
    'Aprovação': True
    }


print(aluno)
print()


# Atualizar
aluno.update({'Nome': 'Jose', 'Nota_final': 'B',})
print(aluno)
print()


# Inserir
aluno.update({'Cep': 98030942, 'cpf': 64681520358,})
print(aluno)
print()


#Remover iten
del aluno['Nota_final']
print(aluno)
print()


# Voce pode adicionar uma menssagem de retorno caso não exista não retorna erro
print(aluno.get('endereço', 'Não existe'))
print()


print(aluno.get('Idade', 'Não existe'))