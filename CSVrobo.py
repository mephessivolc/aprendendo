    # transformar linha em coluna e os caracteres de numeros em numeros decimais
    import csv # pacote para trabalhar com csv

    readcsv = 'report.page.csv' # nome do arquivo

    # abrir o arquivo, ler as informações de 2 linhas e muitas colunas
    # e passar para a variavel linha do tipo lista
    with open(readcsv, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        linha = []
        for row in spamreader:
            linha.append(row) # setando informações

    writecsv = 'resp.csv' # arquivo de resposta

    # abrir o arquivo, escrever as informações em linas com duas colunas
    with open(writecsv, 'w') as csvfile:
        # instanciar a classe de escrever csv
        spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(linha[0])):
            arg = linha[1][i].replace('.','') # retirar os pontos da string
            arg = arg.replace(',','.') # trocar as virgulas por pontos da string
            arg = arg.replace('"','') # retirar aspas duplas da string
            arg = float(arg) # converter string para float
            msg=[linha[0][i], arg] # colocar em linhas cada informação nas suas respectivas colunas
            spamwriter.writerow(msg) # escrever no arquivo final as informações
