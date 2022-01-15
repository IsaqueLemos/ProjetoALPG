import random

print('\n\033[1;36m************************************************')
print('************** Sorteio de Equipes **************')
print('************************************************\033[m')

# Função para sortear as equipes
def sortear(lista, quantidade_de_equipes, jogadores):
    equipes = []

    for i in range(quantidade_de_equipes):
        equipe = []
    
        for e in range(jogadores):
            jogador = random.choice(lista)
            equipe.append(jogador)
            lista.remove(jogador)

        equipes.append(equipe)
    
    return equipes

condicao_de_parada = False
while condicao_de_parada == False:

    # Menu sorteio.
    print('\n\033[1;97m******* MENU *******\033[m')
    print('\033[1;32m1 - Novo Sorteio')
    print('2 - Sair\033[m')
    opcao = input('\033[1;33mSelecione a opção:  \033[m')

    # Criando um Novo Sorteio
    if opcao == '1':
        print('\n\033[1;36m******* Inserindo Dados do Novo Sorteio *******\033[m')

        # Definindo as configurações do Sorteio.

        # Capturando o nome do sorteio, executando até o usuário informar uma string com no mínimo um caractere
        passo1 = True
        while passo1:
            nome_do_sorteio = input('\033[1;33mInforme um nome para seu sorteio:  \033[m')
            condicao = len(nome_do_sorteio) > 0

            if condicao:
                passo1 = False
            else:
                print('\033[1;31m******* INFORME NO MÍNIMO 1 (UM) CARACTERE\033[m')

        # Capturando a quantidade de equipes, executando até o usuário informar um número
        passo2 = True
        while passo2:
            quantidade_de_equipes = input('\033[1;33mInsira a quantidade de equipes:  \033[m')
            condicao = quantidade_de_equipes.isdigit()
            if condicao:
                quantidade_de_equipes = int(quantidade_de_equipes)
                passo2 = False
            else:
                print('\033[1;31m******* INFORME APENAS NÚMEROS\033[m')

        # Capturando a quantidade de jogadores por equipes, executando até o usuário informar um número
        passo3 = True
        while passo3:
            jogadores_por_equipe = input('\033[1;33mInsira a quantidade de jogadores por equipe:  \033[m')
            condicao = jogadores_por_equipe.isdigit()
            if condicao:
                jogadores_por_equipe = int(jogadores_por_equipe)
                passo3 = False
            else:
                print('\033[1;31m******* INFORME APENAS NÚMEROS\033[m')

        # Capturando os nomes dos jogadores e adicionando-os em uma lista
        jogadores = list(map(str, input(f'\033[1;33mInforme o nome dos jogadores separados por espaço:  \033[m').split()))

        jogadores_necessarios = quantidade_de_equipes * jogadores_por_equipe

        # Verificando se há a quantidade necessária de jogadores para preencher as equipes.
        if len(jogadores) < jogadores_necessarios:
            print(f'\n\033[1;31m******* Você informou {len(jogadores)} jogador(es).')
            print(f'******* O Programa espera no mínimo {jogadores_necessarios} jogador(es) para completar as equipes!\033[m')
        else:

            # Gerando as equipes e printando o resultado do sorteio.
            resultado = sortear(jogadores, quantidade_de_equipes ,jogadores_por_equipe)

            for equipes in range(len(resultado)):
                
                print(f'\n\033[1;97m******* Equipe {equipes + 1}\033[m')
                
                for jogador in resultado[equipes]:
                    print(f'\033[97m{jogador}\033[m')

            print('\n\033[1;97m******* Restantes\033[m')
            for restante in jogadores:
                print(f'\033[97m{restante}\033[m')
    
    # Finalizando a Aplicação
    elif opcao == '2':
        print('\n\033[1;35m******* CRÉDITOS: GABRIEL, ISAQUE e WEDSON *******\033[m')
        print('\033[1;31m************** Programa Finalizado **************\033[m\n\n\n')
        condicao_de_parada = True

    # Mensagem para Opções Inválidas do Menu
    else:
        print('\033[1;31m******* OPÇÃO INVÁLIDA\033[m')