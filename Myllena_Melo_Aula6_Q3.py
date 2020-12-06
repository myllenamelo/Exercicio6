#verifica mínimo e máximo
def minemax (n):
    menor = min(n) 
    maior = max(n) 
    print (f'O menor número é {menor} e o maior é {maior} .')
    return menor,maior

#codigo principal
i=0
resultado=0
numeros = list()
quant=int(input('Quantos números deseja inserir? '))
for i in range (0,quant):
    numeros.append(int(input('Insira o nº: ')))
minemax(numeros)
