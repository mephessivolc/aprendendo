class Teste():
    def __init__(self, nome, teste):
        self.name = nome
        self.teste = teste

    def imp(self):
        return self.name

n=[]

n.append(Teste('clovis', 'teste'))
n.append(Teste('gisele', 'teste1'))
print(len(n))
for i in range(len(n)):
    print("%s - %s"%(i,n[i].imp()))

# print(n[0].imp())
# try:
#     del n[0]
#     print('Deletando clovis')
# except:
#     print('Error')
#
# print(n[1].imp())
# print(n[0].imp())
