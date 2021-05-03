nome = input('Digite seu nome: ')
tamanho_nome = len(nome)
idade = input('Digite sua idade: ')
horario = input('Digite a hora atual: ')

if tamanho_nome <= 4:
    print(f'Bem vindo(a), gostei do seu nome {nome}, pequeno e fácil.')
elif tamanho_nome <= 6:
    print(f'Bem vindo(a), gostei do seu nome{nome}.')
else:
    print(f'Bem vindo(a), gostei do seu nome {nome}, achei grande.')

if idade.isdigit():
    idade = int(idade)

    if 18 <= idade:
        print(f'{nome} você é maior de idade. Acesso Autorizado.')
    else:
        print(f'{nome} você é menor de idade. Acesso Negado.')
else:
    print('Idade inválida.')

if horario.isdigit():
    horario = int(horario)

    if 0 > horario > 23:
        print('Horário inválido.')
    else:
        if horario <= 11:
            print(f'Login efetuado às {horario} horas. Bom dia {nome}.')
        elif horario <= 17:
            print(f'Login efetuado às {horario} horas. Boa tarde {nome}.')
        else:
            print(f'Login efetuado às {horario} horas. Boa noite {nome}.')
else:
    print('Digite um horário válido (0-23).')
