#cálculo da conta+gorjeta
def valorconta(conta,gorj=10):
    return conta + gorj
    
#codigo principal

c=float(input('Qual é o valor da conta? R$'))
condicao=str(input('Você deseja pagar a gorjeta? S/N'))
if condicao.upper() == 'N':
    print('O valor da conta foi de R$ ',c)
    print('Obrigado =) volte sempre')
else:
    valortotal = valorconta(c)
    print('O valor da conta com a gorjeta totalizou R$',valortotal)
    print('Obrigado =) volte sempre')