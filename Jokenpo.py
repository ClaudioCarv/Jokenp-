import random
import platform
import os
import time
from colors import cores
from colors import tipos
import emoji

#função de limpar o CMD
def limpar():
    if platform.system() == 'Windows':
        os.system('cls')

#variáveis emoji
choros = emoji.emojize(':loudly_crying_face:')
risos = emoji.emojize(':rolling_on_the_floor_laughing:')
eba = emoji.emojize(':partying_face:')

#score dos vencedores
jogador = 0
computador = 0

#lista random
list = ['pedra', 'papel', 'tesoura']

#repetição do game
while True:
    limpar()

    #escolha aleatória do computador
    c = random.choice(list)

    print('{}{}Jokenpô{}'.format(cores['ciano'], tipos['negrito'], cores['limpa']).center(40))

    print('{}1- Pedra\n2- Papel\n3- Tesoura{}'.format(cores['ciano'], cores['limpa']))

    vr = int(input('{}\nDigite aqui a sua escolha: {}'.format(cores['verde'], cores['limpa'])))
    print('{}Vamo lá hein...{}'.format(cores['vermelho'], cores['limpa']))
    time.sleep(1)
    print('{}TU VAI PERDER {}{}'.format(cores['vermelho'], cores['limpa'], risos))
    time.sleep(1)
    print('{}3{}'.format(cores['amarelo'], cores['limpa']))
    time.sleep(1)
    print('{}2{}'.format(cores['amarelo'], cores['limpa']))
    time.sleep(1)
    print('{}1{}'.format(cores['amarelo'], cores['limpa']))
    time.sleep(1)
    print('{}VAII{}\n'.format(cores['amarelo'], cores['limpa']))
    time.sleep(0.5)

    #caso o jogador escolha pedra
    if(vr == 1 and c == 'pedra'):
        print('Pedra VS Pedra')
        print('{}EMPATE{}'.format(cores['amarelo'], cores['limpa']))
    elif(vr == 1 and c == 'papel'):
        print('Pedra VS Papel')
        print('{}COMPUTADOR VENCEU!{}'.format(cores['vermelho'], cores['limpa']))
        print('{}EU DISSEEE{}{}'.format(cores['vermelho'], risos, cores['limpa']))
        print('{}{}\nVocê perdeu...{}{}'.format(tipos['sublinhado'], cores['vermelho'], choros, cores['limpa']))
        
        computador += 1
    elif(vr == 1 and c == 'tesoura'):
        print('Pedra VS Tesoura')
        print('{}JOGADOR VENCEU!{}'.format(cores['verde'], cores['limpa']))
        print('{}{}\nVocê ganhou!{}{}'.format(tipos['sublinhado'], cores['verde'], eba, cores['limpa']))
        jogador += 1

    #caso o jogador escolha papel
    elif(vr == 2 and c == 'papel'):
        print('Papel VS papel')
        print('{}EMPATE{}'.format(cores['amarelo'], cores['limpa']))
    elif(vr == 2 and c == 'pedra'):
        print('Papel VS Pedra')
        print('{}JOGADOR VENCEU!{}'.format(cores['verde'], cores['limpa']))
        print('{}{}\nVocê ganhou!{}{}'.format(tipos['sublinhado'], cores['verde'], eba, cores['limpa']))
        jogador += 1
    elif(vr == 2 and c == 'tesoura'):
        print('Papel VS Tesoura')
        print('{}COMPUTADOR VENCEU!{}'.format(cores['vermelho'], cores['limpa']))
        print('{}EU DISSEEE{}{}'.format(cores['vermelho'], risos, cores['limpa']))
        print('{}{}\nVocê perdeu...{}{}'.format(tipos['sublinhado'], cores['vermelho'], choros, cores['limpa']))
        
        computador += 1

    #caso o jogador escolha tesouraw
    elif(vr == 3 and c == 'tesoura'):
        print('Tesoura VS Tesoura uii')
        print('{}EMPATE{}'.format(cores['amarelo'], cores['limpa']))
    elif(vr == 3 and c == 'Papel'):
        print('Tesoura VS Papel')
        print('{}JOGADOR VENCEU!{}'.format(cores['verde'], cores['limpa']))
        print('{}{}\nVocê ganhou!{}{}'.format(tipos['sublinhado'], cores['verde'], eba, cores['limpa']))
        jogador += 1
    elif(vr == 3 and c == 'pedra'):
        print('Tesoura VS Pedra')
        print('{}COMPUTADOR VENCEU!{}'.format(cores['vermelho'], cores['limpa']))
        print('{}EU DISSEEE{}{}'.format(cores['vermelho'], risos, cores['limpa']))
        print('{}{}\nVocê perdeu...{}{}'.format(tipos['sublinhado'], cores['vermelho'], choros, cores['limpa']))
        
        computador += 1

    #print do score dos vencedores
    print('{}\nJogador: {}{}'.format(cores['verde'], jogador, cores['limpa']))
    print('{}Computador: {}{}'.format(cores['vermelho'], computador, cores['limpa']))
    
    #escolha para jogar novamente ou encerrar o game
    esc = str(input('{}\nDeseja jogar novamente ? S/N: {}'.format(cores['verde'], cores['limpa']))).lower()
    
    if(esc == 's'):
        print('{}Reiniciando{}'.format(cores['amarelo'], cores['limpa']))
        time.sleep(0.5)
        limpar()
    elif(esc == 'n'):
        print('Encerrado')
        break