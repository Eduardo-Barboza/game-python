from random import randint, choice
from time import sleep

cores = {"limpa":"\033[m",
          'verde':'\033[32m',
          'amarelo':'\033[33m',
          'vermelho':'\033[31m',
          'pretobranco':'\033[7;30m'
}

print('=='*30)
print('SEJA BEM VINDO A CETRAL DE JOGOS, QUAL JOGO DESEJA JOGAR? ')
print('=='*30)

v3 = 0
j3 = 0

while True:
    print(f'''{cores['verde']}
        [1] Jogo da adivinhação
        [2] Jogo do Predra, papel ou tesoura
        [3] Jogo do par ou ímpar
        [4] Sair do Jogo{cores['limpa']}''')
    print('=='*20)
    
    escolha = int(input('Qual jogo deseja jogar? '))
    print('---'*20)
    if escolha == 1:
        computador = randint(1,20)
        while True:
            jogador = int(input(f'Em qual número estou pensando? '))
            if jogador != computador:
                if jogador < computador:
                    print('O número que estou ensando é maior.')
                else:
                    print('O núero que estou pensando é menor.')
            elif jogador == computador:
                print(f'{cores['verde']}Parabéns, você acertou!!{cores['limpa']}')
                v3+=1
                break
        print('*'*50)
    elif escolha == 2:
        while True:
            itens = ['PEDRA', 'PAPEL', 'TESOURA']
            computador = choice(itens)
            jogador = str(input('Qual é a sua escolha? ')).upper().strip()
            if jogador != computador:
                print(f'{cores['vermelho']}Você errou, tente mais uma vez.{cores['limpa']}')
            else:
                print(f'{cores['verde']}Parabéns, você acertou!!{cores['limpa']}')
                v3+=1
                break
    elif escolha == 3:
        print('Bem vindo ao jogo do par ou ímpar, vamos ver se você consegue me vencer \nCarregando...')
        sleep(2)
        while True:
            computador = randint(0,10)
            jogador = int(input('Qual o número desejado? '))
            soma = computador + jogador
            tipo = ' '
            j3 += 1
            while tipo not in 'PI':
                tipo = str(input('Deseja ímpar ou par? [P/I] ')).upper().strip() [0]
            if tipo == 'P':
                if soma % 2 == 0:
                    print(f'{cores['verde']}Parabéns, você acertou!!{cores['limpa']}')
                    v3 += 1
                else:
                    print(f'{cores['vermelho']}Você perdeu.{cores['limpa']}')
                    break
            elif tipo == 'I':
                if soma % 2 == 1:
                    print(f'{cores['verde']}Parabéns, você acertou!!{cores['limpa']}')
                    v3 += 1
                else:
                    print(f'{cores['vermelho']}Você perdeu.{cores['limpa']}')
                    break
                print('Vamos jogar de novo....')
        print('*'*50)
    elif escolha == 4:
        break
print('Carregando.....')    
for c in range(0,10):
    print(c)
    sleep(0.2)

print('=='*20)
print(f'{cores['amarelo']}Ao total, você conseguiu {v3} vitórias.\nAté a próxima campeão!!!!{cores['limpa']}')
print('=='*20)