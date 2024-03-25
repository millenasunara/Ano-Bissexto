def bissexto(ano): 
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    return False


d_ano = {}

while True:
    indice = input("Insira um índice (ou 'sair' para sair): ")

    if indice.lower() == 'sair':
        break

    ano = int(input("Insira o ano correspondente: "))
    d_ano[indice] = ano

for indice, ano in d_ano.items():
    verificar = input(f"Você deseja verificar se o ano {ano} do índice {indice} é bissexto? (s/n): ")

    if verificar.lower() == 's':
        if bissexto(ano):
            print(f"O ano {ano} do índice {indice} é bissexto.")
        else:
            print(f"O ano {ano} do índice {indice} não é bissexto.")
    else:
        print("---Verificação de ano bissexto ignorada.---")
print("Resultado final do dicionário: ",d_ano)