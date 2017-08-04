from random import choice

def gera_senha(tamanho):
        caracters = '0123456789abcdefghijlmnopqrstuwvxzABCDEFGHIJKLMNOPQRSTUVXWYZ'
        senha = ''
        for char in range(tamanho):
                senha += choice(caracters)
        return  senha

print (gera_senha(8))
