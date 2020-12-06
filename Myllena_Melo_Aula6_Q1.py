import random

#pede entrada e computador joga
def rodada():
    jogador = int(input('''Escolha sua opção: 
        (0) - Pedra
        (1) - Papel
        (2) - Tesoura 
        >_'''))
    computador = random.randint(0, 2)
    return jogador, computador

#verifica jogada
def jokenpo():
    jogador, computador = rodada()
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    if(jogador == computador):
        return 'EMPATE! Jogador: ' + opcoes[jogador] + ' - Computador: ' + opcoes[computador]
    if((jogador == 0 and computador == 1) or
       (computador == 0 and jogador == 1)):
        return 'O papel Venceu!' + 'Jogador: ' + opcoes[jogador] + ' - Computador: ' + opcoes[computador]
    elif((jogador == 0 and computador == 2) or
         (computador == 0 and jogador == 2)):
        return 'A Pedra Venceu!' + 'Jogador: ' + opcoes[jogador] + ' - Computador: ' + opcoes[computador]
    elif((jogador == 2 and computador == 1) or
         (computador == 2 and jogador == 1)):
        return 'A Tesoura Venceu!' + 'Jogador: ' + opcoes[jogador] + ' - Computador: ' + opcoes[computador]

#Código principal
print(jokenpo())
print('Fim de jogo.')