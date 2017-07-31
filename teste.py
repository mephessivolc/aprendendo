# mudar letras

import io

filename = 'leituradedados.txt'
readname = 'leituramodificado.txt'
with io.open(filename, mode='r') as fd:
    with io.open(readname, mode='w') as rd:
        for line in fd:
            rd.write(line.replace('\n', ''))
