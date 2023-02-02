from time import sleep

# Introdução do jogo:
nome = input('Olá, qual seu nome? ').title()
sleep(0.5)
print(f'Vamos jogar um jogo, {nome}! \n')
sleep(1)
print('Oito pessoas estão na margem de um rio.')
print('Um pai, uma mãe, dois filhos, duas filhas, um policial e uma prisioneira... \n')
sleep(1)
print('Todas precisam atravessar o rio e há apenas uma jangada.')
print('As regras são claras:')
sleep(1)
print('1. A jangada só pode carregar duas pessoas por vez.')
print('2. Somente o pai, a mãe e o policial sabem manobrar a jangada.')
print('3. Filhos não podem ficar com a mãe na ausência do pai em nenhuma das margens do rio.')
print('4. Filhos não podem ser transportados pela mãe.')
print('5. Filhas não podem ficar com o pai na ausência da mãe em nenhuma das margens do rio.')
print('6. Filhas não podem ser transportadas pelo pai.')
print('7. E, por último: a prisioneira não pode ficar com os membros da família na ausência do policial. \n')
sleep(1)

# Listas para registrar a passagem das pessoas:
margemA = ['pai', 'mae', 'filho1', 'filho2', 'filha1', 'filha2', 'policial', 'prisioneira']
margemB = []

# Início do jogo:
print('Daqui em diante as pessoas ficarão conhecidas como:')
print('Pai, mae, filho1, filho2, filha1, filha2, policial e prisioneira!\n')
print('Pessoas na margem A: ', margemA)

# Funções para determinar de qual margem sairá a jangada:
def sair_da_margem_a():
    pessoa1 = input('Quem vai manobrar a jangada? Favor não usar acentos: ').lower().strip()
    acao(pessoa1, margemA, margemB)
    print('Pessoas na margem B: ', margemB)

def sair_da_margem_b():
    pessoa1 = input('Quem vai manobrar a jangada? Favor não usar acentos: ').lower().strip()
    acao(pessoa1, margemB, margemA)
    print('Pessoas na margem A: ', margemA)

# Função da travessia:
def acao(pessoa, margem1, margem2):
    while pessoa != 'pai' and pessoa != 'mae' and pessoa != 'policial':
        print('Esta pessoa não sabe manobrar a jangada!')
        pessoa = input('Quem vai manobrar jangada? Favor não usar acentos: ').lower().strip()

    if pessoa == 'pai' or pessoa == 'mae' or pessoa == 'policial':
        while pessoa not in margem1:
            print('Esta pessoa não está nesta margem!')
            pessoa = input('Quem vai manobrar a jangada? ').lower().strip()
            if pessoa in margem1:
                break

    escolha = input('A pessoa vai sozinha? Sim ou nao: ').lower().strip()

    while escolha != 'sim' and escolha != 'nao':
        print('Escolha inválida!')
        escolha = input('Esta pessoa vai sozinha? Sim ou nao: ').lower().strip()

    if escolha == 'sim' and pessoa == 'policial':
        if 'prisioneira' in margem1 and len(margem1) == 2:
            margem1.remove(pessoa)
            margem2.append(pessoa)
        elif 'prisioneira' in margem1 and len(margem1) > 2:
            print('A prisioneira não pode ficar sozinha com nenhum membro da família!')
            escolha = 'nao'
        else:
            margem1.remove(pessoa)
            margem2.append(pessoa)

    if escolha == 'sim' and pessoa == 'pai':
        if 'mae' in margem1 and ('filho1' in margem1 or 'filho2' in margem1):
            print('Os filhos não podem ficar sozinhos com a mãe!')
            escolha = 'nao'
        elif 'prisioneira' in margem1 and len(margem1) > 2 and 'policial' not in margem1:
            print('A prisioneira não pode ficar sozinha com nenhum membro da família!')
            escolha = 'nao'
        else:
            margem1.remove(pessoa)
            margem2.append(pessoa)
        
    if escolha == 'sim' and pessoa == 'mae':
        if 'pai' in margem1 and ('filha1' in margem1 or 'filha2' in margem1):
            print('As filhas não podem ficar sozinhas com o pai!')
            escolha = 'nao'
        elif 'prisioneira' in margem1 and len(margem1) > 2 and 'policial' not in margem1:
            print('A prisioneira não pode ficar sozinha com nenhum membro da família!')
            escolha = 'nao'
        else:
            margem1.remove(pessoa)
            margem2.append(pessoa)

    if escolha == 'nao':
        if pessoa == 'pai':
            pessoa2 = input('Quem vai junto? ').lower().strip()
            while True:
                if pessoa2 == 'filha1' or pessoa2 == 'filha2' or pessoa2 == 'prisioneira':
                    print('O pai não pode ir com esta pessoa!')
                    pessoa2 = input('Quem vai com o pai? ').lower().strip()
                elif pessoa2 == 'policial':
                    if 'prisioneira' in margem1 and len(margem1) > 3:
                        print('A prisioneira não pode ficar sozinha com nenhum membro da família!')
                        pessoa2 = input('Quem vai com o pai? ').lower().strip()
                    elif 'mae' in margem1 and ('filho1' in margem1 or 'filho2' in margem1):
                        print('A mãe não pode ficar sozinha com nenhum dos filhos.')
                        pessoa2 = input('Quem vai com o pai? ').lower().strip()
                    else:
                        margem1.remove(pessoa)
                        margem1.remove(pessoa2)
                        margem2.append(pessoa)
                        margem2.append(pessoa2)
                        break
                elif pessoa2 == 'filho1' and 'filho2' in margem1 and 'mae' in margem1:
                    print('Nenhum dos filhos pode ficar sozinho com a mãe!')
                    pessoa2 = input('Quem vai com o pai? ').lower().strip()
                elif pessoa2 == 'filho2' and 'filho1' in margem1 and 'mae' in margem1:
                    print('Nenhum dos filhos pode ficar sozinho com a mãe!')
                    pessoa2 = input('Quem vai com o pai? ').lower().strip()
                elif pessoa2 not in margem1 and pessoa2 not in margem2:
                    print('Esta pessoa não existe!')
                    pessoa2 = input('Quem vai com o pai? ').lower().strip()
                elif pessoa2 not in margem1 and pessoa2 in margem2:
                    print('Esta pessoa está na outra margem!')
                    pessoa2 = input('Quem vai com o pai? ').lower().strip()
                else:
                    margem1.remove(pessoa)
                    margem1.remove(pessoa2)
                    margem2.append(pessoa)
                    margem2.append(pessoa2)
                    break
        elif pessoa == 'mae':
            pessoa2 = input('Quem vai junto? ').lower().strip()
            while True:
                if pessoa2 == 'filho1' or pessoa2 == 'filho2' or pessoa2 == 'prisioneira':
                    print('A mãe não pode ir com esta pessoa!')
                    pessoa2 = input('Quem vai com a mãe? ').lower().strip()
                elif pessoa2 == 'policial':
                    if 'prisioneira' in margem1 and len(margem1) > 3:
                        print('A prisioneira não pode ficar sozinha com nenhum membro da família!')
                        pessoa2 = input('Quem vai com a mãe? ').lower().strip()
                    elif 'pai' in margem1 and ('filha1' in margem1 or 'filha2' in margem1):
                        print('O pai não pode ficar sozinho com nenhuma das filhas.')
                        pessoa2 = input('Quem vai com a mãe? ').lower().strip()
                    else:
                        margem1.remove(pessoa)
                        margem1.remove(pessoa2)
                        margem2.append(pessoa)
                        margem2.append(pessoa2)
                        break
                elif pessoa2 == 'filha1' and 'filha2' in margem1 and 'pai' in margem1:
                    print('Nenhuma das filhas pode ficar sozinha com o pai!')
                    pessoa2 = input('Quem vai com a mãe? ').lower().strip()
                elif pessoa2 == 'filha2' and 'filha1' in margem1 and 'pai' in margem1:
                    print('Nenhuma das filhas pode ficar sozinha com o pai!')
                    pessoa2 = input('Quem vai com a mãe? ').lower().strip()
                elif pessoa2 not in margem1 and pessoa2 not in margem2:
                    print('Esta pessoa não existe!')
                    pessoa2 = input('Quem vai com a mãe? ').lower().strip()
                elif pessoa2 not in margem1 and pessoa2 in margem2:
                    print('Esta pessoa está na outra margem!')
                    pessoa2 = input('Quem vai com a mãe? ').lower().strip()
                else:
                    margem1.remove(pessoa)
                    margem1.remove(pessoa2)
                    margem2.append(pessoa)
                    margem2.append(pessoa2)
                    break
