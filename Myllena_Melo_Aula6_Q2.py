from time import sleep

#Verifica inicio,fim e passo
def contador (i, f, p):
    print (f'contagem de {i} até {f} de {p} em {p}')

    if p < 0:
        p*= -1
    if p==0:
        p=1
    if  i < f:
        cont=i
        while cont <= f:
            print (f'{cont}', end=' ',flush=True)
            sleep(0.5)
            cont += p
        print('fim')
    else:
        cont=i
        while cont >= f:
            print (f'{cont}', end=' ',flush=True)
            sleep(0.5)
            cont -= p
        print('fim')

#Código principal
contador (1,10,1)
contador (10,0,2)
print ('Contagem personalizada:')
inicio=int(input('Início:'))
fim=int(input('Fim:'))
passo=int(input('Passo:'))
contador(inicio,fim,passo)