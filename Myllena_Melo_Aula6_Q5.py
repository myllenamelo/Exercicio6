#verifica palavra
def verificacao(stringlimpa):
    stringinvertida = str()
    palindromo = (stringlimpa).upper().split()
    palindromo = ''.join(palindromo)
    for i in range(len(palindromo)-1,-1,-1):
        stringinvertida += palindromo[i]

    if stringinvertida in palindromo:
        return (f'A palavra {stringlimpa} é um palíndromo.')

#exibe lista de palíndromos
def listapalíndromos(*lista):
    for string in lista[0]:
        if verificacao(string):
            print (verificacao(string))

#Código Principal        
palindromo = []
lista = []
quant = int(input('Quantas palavras você quer verificar? '))

for i in range(quant):
    lista.append(input('Digite a palavra: '))
    
listapalíndromos(sorted(lista))