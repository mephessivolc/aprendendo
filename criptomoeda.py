'''
    Programa feito por diversao e aprendizado sobre JSON
    Fará busca de quais criptomoedas estão sendo mineradas, buscará as
    cotações por JSON da internet, calculará o valor referente em Real
    e exibirá o valor de cada criptomoeda e no fim a soma do valor de todas.
'''

import json
import requests

# lista de codigos das criptomoedas que estao na carteira
matriz=['AEON', 'BCN', 'ETC', 'ETH', 'FCN', 'XMR']

valores=[] # armazenar quantidades de cada criptomoeda na carteira

# preencher o armazenamento
for i in range(len(matriz)):
    valores.append(input(matriz[i]+': '))

# buscar JSON de cotação de cada criptomoeda
data=[]
for i in range(len(matriz)):
    # recebendo JSON de valores de cotacoes: BRL, USD (final do link)
    string = ('https://min-api.cryptocompare.com/data/pricemulti?fsyms='+matriz[i]+'&tsyms=BRL,USD')
    load = requests.get(string)
    read = load.content.decode('utf-8') # decodificando para utf-8
    data.append(json.loads(read)) # acrescentar as informações

# montar o esquema pra calcular e apresentar em uma tabela
print('Resultados')
soma = 0
for i in range(len(matriz)):
    res = data[i][matriz[i]]['BRL']*float(valores[i]) # se quiser saber o valor em Dolares, troque 'BRL' por 'USD'
    soma = soma+res
    print('%s: %s'%(matriz[i], res))

print('Total: %s'%soma)
