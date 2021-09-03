"""   CEUB   -   Bacharelado em Ciência da Computação (BCC)   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.

- CRUD
- CRUD (acrônimo do inglês Create, Read, Update and Delete) são as quatro
operações básicas (inclui, consulta, atualiza e apaga os dados) utilizadas
em bases de dados relacionais (RDBMS) fornecidas aos usuários do sistema.

- Desenvolva o programa usando lista com as funções main com repetição, menu,
create, read, update e delete para simular um CRUD. Neste exercício, use nomes.

- A função main gerencia o programa usando uma estrutura de repetição,
ou seja, todas as funções serão chamadas da função main.

- A função menu não recebe nada, apresenta as quatro operações do CRUD,
lê a opção do usuário e retorna a opção digitada pra função main:
    [c] - Create (inserir um item)
    [r] - Read (mostrar toda a lista)
    [u] - Update (substituir um item)
    [d] - Delete  (remover um item)
    [e] - Exit (sair)
    Opção:
lista = []                      # Lista vazia
def menu():                     # Original
    print('[c] - Create')
    print('[r] - Read')
    print('[u] - Update')
    print('[d] - Delete')
    print('[e] - Exit')
    opcao = input('Opção: ')
    return opcao

- Na função menu, inclua a msg : 'Opção inválida, tente novamente."
e só sai da função menu se o usuário digitar uma das opções válidas.
ela deve aceitar letra maiuscula ou minúscula
"""
# Dicas def menu(): use while e um if dentro do while com msg erro
lista = []                      # Lista vazia


def menu():
    l_opcoes = ['c', 'r', 'u', 'd', 'e']
    print('[c] - Create')
    print('[r] - Read')
    print('[u] - Update')
    print('[d] - Delete')
    print('[e] - Exit')
    while True:
        opcao = input('Opção: ').lower()
        if opcao in l_opcoes:
            break
        else:
            print('Opção inválida, tente novamente.')
    return opcao

# - A função create não recebe nada e não retorna nada. Lê um nome e insere na lista.


def create():
    nome = input('Nome: ')
    lista.append(nome)

# NA função read, se a lista estiver vazia, mostre a msg: 'lista vazia.' e sai da função.
# Senão, mostre todos os itens da lista na vertical

# def read():                            # Original
#    print(lista)                        # Na horizontal


def read():
    # Verifica se a lista não está vazia
    if lista_nao_vazia():
        # print(lista)  # Na horizontal
        ct = 0
        for v in lista:     # Na vertical, com indice e ct
            print(ct, '-', v)
            ct += 1
        # for v in lista:       # Na vertical, sem índice
        #    print(v)
        # qtd = len(lista)
        # for i in range(qtd):      # Na vertical, com indice e com len e range
        #   print(i, '-', lista[i])
        # for indice, v in enumerate(lista):    # na vertical com indice, sem ct e sem range
        #   print(indice, ' - ', v)
    # else:
        # print('Lista vazia.')


''' Na função update, se lista vazia, mostre msg "Lista Vazia."
Senão mostre os itens da lista.
Se posição não existe, msg erro. Use try...Except...
Teste: uma posição válida e uma posição inválida.
def update():                               # Original
    p = int(input("Qual posição: "))
    novo_nome = input("Novo nome: ")
      Usando notação de vetor:               Sintaxe: nome_lista[indice] = novo_nome
    lista[p] = novo_nome                     Solução 1, notação vetor.
      lista.pop(p)                           Solução 2, funções de lista.
      lista.insert(p, novo_nome)             Solução 2 '''

# Dicas: algoritmo do update atualizado
# Dicas def update()
# def update():                             # Algoritmo do update atualizado
#   Verificat se lista não está vazia(if:)
#       mostre todos os itens
#       try:
#           lê os dados necessários pra atualizar
#           atualiza
#       except IndexError as e:
#           msg erro 1 ('posição nao existe)
#   Lista vazia (else):
#       msg erro 2 ('lista vazia)


def update():
    # Verifica se lista não está vazia
    if lista_nao_vazia():
        read()                                # Chama a função def read()
        try:                                   # Tentando
            p = int(input('Qual posição: '))
            novo_nome = input('Novo nome: ')
            lista[p] = novo_nome
        except IndexError as e:
            print('Error IndexError:\n', e)
        except Exception as e:
            print('Error Exception:\n', e)
    # else:
        # print('Lista Vazia.')


''' Na função delete, se lista vazia, mostra msg 'Lista vazia'
Senão mostre os itens da lista.
Verifique se valor (nome) está na lista, se valor não existe, msg erro'
Nesta solução, não use try...except
testes: um nome válido e um nome inválido'''
# def delete():
    # v = input("Qual nome: ")
    # lista.remove(v)


def delete():
    if lista_nao_vazia():
        read()
        nome = input('Qual nome: ')
        if nome in lista:
            lista.remove(nome)
        else:
            print(f'O {nome} não está na lista.')
    # else:
        # print('Lista vazia.')


""" Com o objetivo de eliminar o codigo repetido nas defs readm update e delete
crie esta função:
- crie a função lista_nao_vazia, ela não recebe nada e retorna o valor lógico True ou false.
se a lista estiver vazia, mostra a msg 'Lista Vazia' e retorna false. E se a lista não estiveer vazia
retorna True. Ela vai ser chamada pelas funções read, update, delete.
Atualize essas três funções para funcionar com a função lista_nao_vazia. """


def lista_nao_vazia():
    if lista != []:
        nao_vazia = True
    else:
        nao_vazia = False
        print('A lista está vazia')
    return nao_vazia


if __name__ == '__main__':          # Atalho: mai <tab>
    while True:
        op = menu()                 # A variável op recebe o valor que a função menu retorna
        if op == 'c':
            create()                # Chama a função create
        elif op == 'r':
            read()
        elif op == 'u':
            update()
        elif op == 'd':
            delete()
        else:
            break
