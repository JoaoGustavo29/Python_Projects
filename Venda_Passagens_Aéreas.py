"""
João Gustavo Borges e Souza
UC20201728
Bacharel em Ciência da Computação
"""

# importando os pacotes
import random as rnd

# Declarando variáveis
passageiros = 0
adultos = 0
criancas = 0
pessoas = 0

# Dicionário para o avião
aviao_base = {"D": list(range(1, 201)), "C": [], "R": [], "valor": 0}

# Dicionário para alocar informações dos vôos
aviao = {}

# Dicionário para alocar informações das compras
informacoes_id = {}

# Menu
while True:
    print('\n' * 5)
    print('+-------------------------------------------------------------+')
    print('|      SEJA BEM-VINDO(A) AO SISTEMA SALUMAR LINHAS AÉREAS     |')
    print('+-------------------------------------------------------------+')
    print('')
    print('+-------------------------------------------------------------+')
    print('|                           MENU                              |')
    print('+-------------------------------------------------------------+')
    print('| OPÇÃO                      ||            CÓDIGO             |')
    print('+-------------------------------------------------------------+')
    print('| CADASTRAR CLIENTE          ||               1               |')
    print('+-------------------------------------------------------------+')
    print('| COMPRAS/RESERVAS/DEVOLUÇÃO ||               2               |')
    print('+-------------------------------------------------------------+')
    print('| INFORMAÇÕES DA PASSAGEM    ||               3               |')
    print('+-------------------------------------------------------------+')
    print('| SAIR DO PROGRAMA           ||               4               |')
    print('+-------------------------------------------------------------+')

    opcoesCodigo = ['1', '2', '3', '4']  # Lista de códigos

    codigo = input('\nDigite o código correspondente a opção desejada: ')
    print('\n')

    while codigo not in opcoesCodigo:
        codigo = input('Código Inválido! Por favor, digite novamente: ')
        continue

    else:
        if codigo == '1':

            # Cadastramento do cliente

            print('+----------------------------------------------------+')
            print('|   SEJA BEM-VINDO! VAMOS REALIZAR O SEU CADASTRO!   |')
            print('+----------------------------------------------------+')
            nomeCliente = input('Digite seu nome: ')  # Variável para o nome do Cliente

            while len(nomeCliente) < 4:  # Verificação do tamanho do nome do cliente
                nomeCliente = input('Nome inválido. Por favor, digite novamente: ')
                continue

            else:
                print(f'{nomeCliente.title()} é um prazer te receber como cliente!')

        elif codigo == '2':

            # Compra/Reserva/Devolução de passagens

            print('+-----------------------------------------------+')
            print('|    Seja Bem-Vindo a Salumar Linhas aéreas!    |')
            print('+-----------------------------------------------+')

            destino = input('\nQual o seu destino? ')

            while len(destino) < 4:  # Checagem de caracteres
                destino = input('\nPor favor, insira um destino: ')
                continue

            else:
                print('\nOK! Seu destino é {}. Vamos checar as melhores oportunidades para você!'
                      .format(destino.title()))

            if destino.lower() in list(aviao.keys()):  # Verificação de Destino no dicionário do avião
                local = destino.lower()

            else:
                valor_Voo = rnd.randint(500, 2000)  # Gerando valor do vôo aleatóriamente entre os valores 500 - 2000
                aviao[destino.lower()] = aviao_base
                aviao[destino.lower()]['valor'] = valor_Voo
                local = destino.lower()

            print(f'\nO voo possui {len(aviao[local]["D"])} assentos, {len(aviao[local]["D"]):.0f} disponíveis, '
                  f'{len(aviao[local]["C"]):.0f} comprados e {len(aviao[local]["R"])} reservados. '
                  f'\nO valor do vôo é ' f'{aviao[local]["valor"]} reais.')

            escolha = input('\nE aí, você deseja continuar? ')

            opcoesEscolha = ['Sim', 'Não', 'sim', 'não']

            while escolha not in opcoesEscolha:
                escolha = input('\nEscolha inválida! Por favor, digite novamente:')
                continue

            else:
                if escolha == 'sim' or escolha == 'Sim':

                    passagens = int(input(f'\nQue ótimo!\n\nQuantas passagens você deseja comprar/devolver/reservar? '))

                    print('\nAgora preciso que você me informe, qual das seguintes opções você deseja realizar.')

                    opcao = input("\nC = comprar/Confirmar Reserva\nR = reservar\nD = Devolver(cancelar compra)\nSua "
                                  "opcao: ")

                    # Listas para auxiliar na contagem de passagens

                    comprar = []
                    reservar = []
                    devolver = []

                    if opcao == "C" or opcao == "c":
                        while True:

                            assento = input('Caso, tenha assento reservado digite o número que faremos o resto.'
                                            '\nDigite o número do assento desejado: ')

                            if not assento.isdigit():  # Verificando se a informação digitada é um dígito
                                print('Apenas números.')

                            else:
                                assento = int(assento)
                                if assento in aviao[local]["D"]:  # Verificando se o assento está disponível
                                    print('Assento comprado.')

                                    aviao[local]["D"].remove(assento)  # Removendo o assento da Lista de disponíveis

                                    aviao[local]["C"].append(assento)  # Adicionando o assento na Lista de comprados
                                    comprar.append(assento)

                                    if len(comprar) == passagens:  # Verificando se o número de assentos
                                        break                      # é igual ao número de passagens desejado

                                elif assento in aviao[local]['R']:  # Verificando se o assento está reservado
                                    print('Assento Comprado.')

                                    aviao[local]['R'].remove(assento)  # Removendo o assento da Lista de reservados

                                    aviao[local]['C'].append(assento)  # Adicionando o assento na Lista de comprados
                                    comprar.append(assento)

                                    if len(comprar) == passagens:  # Verificando se o número de assentos
                                        break                      # é igual ao número de passagens desejado

                                else:
                                    print("Assento indisponível\nTente novamente.")

                    elif opcao == "R" or opcao == "r":
                        while True:
                            assento = input('\nDigite o número do assento que deseja reservar: ')

                            if not assento.isdigit():  # Verificando se a informação digitada é um dígito
                                print('Apenas números.')

                            else:
                                assento = int(assento)
                                if assento in aviao[local]["D"]:  # Verificando se o assento está disponível
                                    print('Assento Reservado.')

                                    aviao[local]["D"].remove(assento)  # Removendo o assento da Lista de Disponíveis

                                    aviao[local]["R"].append(assento)  # Adicionando o assento na Lista de Reservados
                                    reservar.append(assento)

                                    if len(reservar) == passagens:  # Verificando se o número de assentos
                                        break                       # é igual ao número de passagens desejado

                                else:
                                    print('Assento indisponível\nTente novamente.')

                    elif opcao == "D" or opcao == "d":
                        while True:
                            compras = input('Digite o código da compra ou N = Não tenho código: ').upper()
                            if compras != '' and compras[0] == 'N':
                                print('Voltando ao menu iniciar.')
                                break

                            elif compras in list(informacoes_id.keys()):
                                while True:
                                    assento = input('\nDigite o número do assento : ')

                                    if not assento.isdigit():
                                        print('Apenas números')

                                    else:
                                        assento = int(assento)
                                        if assento in aviao[local]["C"]:
                                            print('Compra cancelada.')
                                            aviao[local]["C"].remove(assento)
                                            aviao[local]["D"].append(assento)
                                            informacoes_id[compras]['comprados'].remove(assento)
                                            devolver.append(assento)

                                        elif assento in aviao[local]["R"]:
                                            print('Reserva Cancelada.')
                                            aviao[local]["R"].remove(assento)
                                            aviao[local]["D"].append(assento)
                                            informacoes_id[compras]['reservados'].remove(assento)
                                            devolver.append(assento)
                                            if len(devolver) == passagens:
                                                break
                                        else:
                                            print('Assento indisponível\nTente novamente.')

                                if informacoes_id[compras]['comprados'] == [] and informacoes_id[compras][
                                    'reservados'] == []:
                                    del informacoes_id[compras]

                            else:
                                print('Código de compra indisponível\nTente novamente.')

                    if opcao in ["R", "r", "C", "c"]:
                        passageiros += passagens

                        idade = int(input('\nDigite a idade dos passageiros: '))

                        if idade > 5:
                            adultos += 1
                        else:
                            criancas += 1

                        pessoas += 1

                        while pessoas < passageiros:
                            idade = int(input('\nDigite a idade dos passageiros: '))

                            if idade > 5:
                                adultos += 1
                            else:
                                criancas += 1

                            pessoas += 1

                        if idade < 5:
                            valor_final = (aviao[local]['valor'] * pessoas)
                        else:
                            valor_final = (aviao[local]['valor'] * 0.5 * criancas) + (aviao[local]['valor'] * adultos)

                        compra_id = f'{destino[:2].upper()}-{rnd.randint(10000, 99999)}'
                        base_inf = {"comprados": comprar, "reservados": reservar, "valor_f": valor_final}
                        informacoes_id[compra_id] = base_inf
                        print(f'\nSeu código de compra: {compra_id}')

                elif escolha == 'não' or escolha == 'Não':
                    print('\nFoi um prazer te ter conosco! Volte sempre!')
                    break

        elif codigo == '3':
            print('Vamos conferir as informações da sua compra!')
            codigo = input('Digite o código da compra ou S para sair: ').upper()
            if codigo != '' and codigo[0] == 'S':
                print('Voltando ao iniciar.')

            elif codigo in list(informacoes_id.keys()):
                print(f"\nCódigo de compra: {codigo}")
                print(f"Assentos comprados: {informacoes_id[codigo]['comprados']}")
                print(f"Assentos reservados: {informacoes_id[codigo]['reservados']}")
                print(f"Valor final: {informacoes_id[codigo]['valor_f']}")

            else:
                print('Código inválido ou comando errado.')

        elif codigo == '4':
            break
