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


for x in aluno.values():
    print(x)
print()


for x in aluno.items():
    print(x)
