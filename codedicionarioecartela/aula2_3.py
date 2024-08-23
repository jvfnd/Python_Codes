def coletar_dados():

    dados = []
    while True:
        nome = input("Digite o nome (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        idade = input("Digite a idade: ")
        try:
            idade = int(idade)
        except ValueError:
            print("Idade deve ser um número inteiro. Tente novamente.")
            continue


        dados.append({'nome': nome, 'idade': idade})
    return dados

def salvar_em_arquivo(dados, nome_do_arquivo):

    with open(nome_do_arquivo, 'w') as arquivo:
        for item in dados:
            linha = f"Nome: {item['nome']}, Idade: {item['idade']}\n"
            arquivo.write(linha)

def main():

    dados = coletar_dados()
    if dados:
        salvar_em_arquivo(dados, 'dados_pessoas.txt')
        print("Dados Salvos em arquivo txt")
    else:
        print("Nenhum dado salvo")
    dadosjson = salvar_em_arquivo(dados, 'dados_pessoas.json')

    dadoscsn = salvar_em_arquivo(dados, 'dados_pessoas.csn')

if __name__ == '__main__':
    main()
