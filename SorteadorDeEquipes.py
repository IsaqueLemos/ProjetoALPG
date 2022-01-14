import random
ficheiro = open('SorteiosSalvos.txt', 'a')
ficheiro.close()

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

# Função para transformar informções de um arquivo de testo em uma lista dados
def obterDados(arquivo):
    lista = arquivo.read().split('-')
    del lista[0]
    dados = []

    for dado in lista:
        sorteio = dado.split('|')
        del sorteio[-1]
        dados.append(sorteio)

    return dados

condicao_de_parada = False
while condicao_de_parada == False:

    # Menu sorteio.
    print('\n\033[1;97m******* MENU *******\033[m')
    print('\033[1;32m1 - Novo Sorteio')
    print('2 - Verificar Sorteios Salvos')
    print('3 - Deletar Sorteio Salvo')
    print('4 - Sair\033[m')
    opcao = input('\033[1;33mSelecione a opção:  \033[m')

    # Criando um Novo Sorteio
    if opcao == '1':
        print('\n\033[1;36m******* Inserindo Dados do Novo Sorteio *******\033[m')

        # Definindo as configurações do Sorteio.
        passo1 = True
        while passo1:
            nome_do_sorteio = input('\033[1;33mInforme um nome para seu sorteio:  \033[m')
            condicao = len(nome_do_sorteio) > 0

            if condicao:
                passo1 = False
            else:
                print('\033[1;31m******* INFORME NO MÍNIMO 1 (UM) CARACTERE\033[m')

        passo2 = True
        while passo2:
            quantidade_de_equipes = input('\033[1;33mInsira a quantidade de equipes:  \033[m')
            condicao = quantidade_de_equipes.isdigit()
            if condicao:
                quantidade_de_equipes = int(quantidade_de_equipes)
                passo2 = False
            else:
                print('\033[1;31m******* INFORME APENAS NÚMEROS\033[m')

        passo3 = True
        while passo3:
            jogadores_por_equipe = input('\033[1;33mInsira a quantidade de jogadores por equipe:  \033[m')
            condicao = jogadores_por_equipe.isdigit()
            if condicao:
                jogadores_por_equipe = int(jogadores_por_equipe)
                passo3 = False
            else:
                print('\033[1;31m******* INFORME APENAS NÚMEROS\033[m')

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

            # Salvando os Sorteio
            salvar = input('\n\033[1;36m******* Você deseja salvar este sorteio (S/N)? \033[m').upper()

            if salvar == 'S':
                arquivo = open('SorteiosSalvos.txt', 'a')
                arquivo.write('-')
                arquivo.write(f'{nome_do_sorteio}|')
                for equipes in range(len(resultado)):
                    equipe = []

                    for jogador in resultado[equipes]:
                        equipe.append(jogador)
                
                    equipe = ' '.join(equipe)
                    arquivo.write(f'Equipe {equipes + 1}: {equipe}|')
                print('\033[1;32m******* Sorteio Salvo\033[m')
                arquivo.close()
            elif salvar == 'N':
                print('\033[1;31m******* Sorteio Descartado\033[m')
            else:
                print('\033[1;31m******* OPÇÃO INVÁLIDA\033[m')
                print('\033[1;31m******* Sorteio Descartado\033[m')

    # Verificando Sorteios Salvos
    elif opcao == '2':

        condicao_de_parada2 = False
        while condicao_de_parada2 == False:
            # Recolhendo Informações do Arquivo
            arquivo = open('SorteiosSalvos.txt', 'r')
            dados = obterDados(arquivo)
            arquivo.close()

            if len(dados) == 0:
                print('\n\033[1;34mAVISO: Não existem sorteios salvos, crie um novo sorteio e tente novamente.\033[m')
                condicao_de_parada2 = True
            else:
                # Imprimindo os Sorteios Salvos
                print('\n\033[1;36m******* Sorteios Salvos *******\033[m')
                for index in range(len(dados)):
                    sorteio = dados[index]
                    print(f'\033[1;32m{index + 1} - {sorteio[0]}\033[m')

                # Selecionando o Sorteio
                passo = True
                while passo:
                    opcao = input('\033[1;36mSelecione o sorteio e verifique seus dados:  \033[m')
                    condicao = opcao.isdigit()
                    if condicao:
                        opcao = int(opcao)
                        passo = False
                    else:
                        print('\033[1;31m******* INFORME APENAS NÚMEROS\033[m')


                if opcao <= len(dados):
                    sorteio_escolhido = dados[opcao - 1]
                    print(f'\n\033[1;97m{sorteio_escolhido[0]}:\033[m')
                    for index in range(len(sorteio_escolhido)):
                        if index != 0:
                            print(f'\033[97m{sorteio_escolhido[index]}\033[m')
                else:
                    print('\033[1;31m******* OPÇÃO INVÁLIDA\033[m')

                # Interrompendo o Loop
                opcao = input('\n\033[1;36m******* Deseja voltar ao menu (S/N)? \033[m').upper()
                if opcao == 'S':
                    condicao_de_parada2 = True
            
    # Excluindo Sorteios Salvos
    elif opcao == '3':

        condicao_de_parada2 = False
        while condicao_de_parada2 == False:
            # Recolhendo Informações do Arquivo
            arquivo = open('SorteiosSalvos.txt', 'r')
            dados = obterDados(arquivo)
            arquivo.close()

            if len(dados) == 0:
                print('\n\033[1;34mAVISO: Não existem sorteios salvos, crie um novo sorteio e tente novamente.\033[m')
                condicao_de_parada2 = True
            else:
                # Imprimindo os Sorteios Salvos
                print('\n\033[1;31m******* Deletar Sorteio *******\033[m')
                for index in range(len(dados)):
                    sorteio = dados[index]
                    print(f'\033[1;32m{index + 1} - {sorteio[0]}\033[m')

                # Selecionando o Sorteio
                passo = True
                while passo:
                    opcao = input('\033[1;31mInforme o sorteio para DELETAR:  \033[m')
                    condicao = opcao.isdigit()

                    if condicao:
                        opcao = int(opcao)
                        passo = False
                    else:
                        print('\033[1;34m******* INFORME APENAS NÚMEROS\033[m')

                if opcao <= len(dados):
                    sorteio_escolhido = dados[opcao - 1]

                    # Deletando o sorteio
                    print(f'\n\033[1;31m******* O sorteio ({sorteio_escolhido[0]}) foi excluido!\033[m')
                    del dados[opcao - 1]

                    # Reescrevendo as informações no arquivo.txt
                    if len(dados) > 0:
                        novos_dados = []
                        for dado in dados:
                            novo_dado = '|'.join(dado) + '|'
                            novos_dados.append(novo_dado)

                        dados = '-'.join(novos_dados)

                        arquivo = open('SorteiosSalvos.txt', 'w')
                        arquivo.write(f'-{dados}')
                        arquivo.close()

                    else:
                        arquivo = open('SorteiosSalvos.txt', 'w')
                        arquivo.close()


                else:
                    print('\033[1;31m******* OPÇÃO INVÁLIDA\033[m')

                # Interrompendo o Loop
                opcao = input('\n\033[1;36m******* Deseja voltar ao menu (S/N)? \033[m').upper()
                if opcao == 'S':
                    condicao_de_parada2 = True

    # Finalizando a Aplicação
    elif opcao == '4':
        print('\n\033[1;31m************** Programa Finalizado **************\033[m\n\n\n')
        condicao_de_parada = True

    # Mensagem para Opções Inválidas do Menu
    else:
        print('\033[1;31m******* OPÇÃO INVÁLIDA\033[m')