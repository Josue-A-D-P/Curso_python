# Lambda function
    # È uma função pequena (sem nome)
    # Pode ter varios argumentos mas só uma expreção
    # Muito utilizada dentro de outras funções
    # Código mais 'clean'


def somar(x):
    função2 = lambda x: x + 10
    return função2(x) * 4


print(somar(2))