'''
	Teste de Fermat para numero primo
'''
def teste(obj):
	i = 2
	while (obj % i != 0):
		i += 1
		if (i == primo):
			break

	if (i == obj):
		return (True,i)
	else:
		return (False,i)

logico = True
n = 0
maximo = 0

while (logico):
	primo = 2**(2**n)+1
	logico,num = teste(primo)
	if logico:
		print("numero de Fermat: %s é primo"%primo)

	else:
		logico = True
		maximo += 1
		print('Teste nº: %s\nNumero de Fermat: %s não é primo\n\nPois %s/%s = %s '\
			%(maximo,primo,primo,num,primo/num))
		if maximo>5:
			logico = False
	n += 1


# print('numero de Fermat: %s não é primo\n\npois %s/%s = %s '%(primo,primo,num,primo/num))
