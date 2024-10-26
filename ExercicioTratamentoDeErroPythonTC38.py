print("Digite seu nome")
nome = input()

executar = True

while (executar == True):
    try:
        print("Digite seu ano de nascimento")
        ano = int(input())
        if(ano < 1922) or (ano > 2021):
            print("O ano precisa ser entre 1922 e 2024")
        else:
            idade = 2025 - ano
            print(nome, " voce completara", idade, "anos em 2025.")
        executar = False
    except:
        print("Precisa ser digitado apenas numeros")
