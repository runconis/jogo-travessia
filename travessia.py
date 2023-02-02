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
