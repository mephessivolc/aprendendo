# mudar letras

import io

filename = 'leituradedados.txt'
readname = 'leituramodificado.txt'
with io.open(filename, mode='r') as fd:
    with io.open(readname, mode='w') as rd:
        for line in fd:
            rd.write(line.replace('\n', ''))


import csv

readcsv = 'report.csv'

with open(readcsv, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        print(row)
