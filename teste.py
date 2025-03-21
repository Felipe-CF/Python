import random, string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation

    senha = []

    for _ in range(tamanho):
        senha.append(random.choice(caracteres))

    return ''.join(senha)

print(gerar_senha(10))





print(sorted(input().split()))
