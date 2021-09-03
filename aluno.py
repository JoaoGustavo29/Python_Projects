class Aluno(object):
    # def __init__(self, nome, mensalidade, idade):
    def __init__(self, nome, mensalidade=1000.0, idade=18):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_mensalidade(self):
        return self.mensalidade

    def set_mensalidade(self, valor):
        self.mensalidade = valor

    def get_idade(self):
        return self.idade

    def set_idade(self, nova_idade):
        self.idade = nova_idade

    def mostra_dados(self): # solução 1
        print(f'\nNome: {self.nome}')
        print(f'Mensalidade: {self.mensalidade}')
        print(f'Idade: {self.idade}')

    def mostra_dados2(self):    # solução 2
        print(f'\nNome: {self.get_nome()}')
        print(f'Mensalidade: {self.get_mensalidade()}')
        print(f'Idade: {self.get_idade()}')

    def retorna_dados(self):
        dados = f'{self.nome}, {self.mensalidade}, {self.idade}'  # uma das possíveis soluções
        return dados

    def aumento_mensalidade_valor_1(self, valor):   # solução 1
        self.mensalidade += valor

    def aumento_mensalidade_porcentagem(self, pct):
        self.mensalidade += self.mensalidade * pct / 100

    def pode_cnh(self):
        if self.idade <= 18:
            print('Não pode')
        else:
            print('Pode')


if __name__ == '__main__':
    aluno1 = Aluno('Paulo', 1000.00, 21)
    aluno2 = Aluno('Carla', 900.00, 20)

    print(f'Aluno 1\nNome: {aluno1.get_nome()}\nMensalidade: {aluno1.get_mensalidade()}\nIdade: {aluno1.get_idade()}')
    print(f'\nAluno 2\nNome: {aluno2.get_nome()}\nMensalidade: {aluno2.get_mensalidade()}\nIdade: {aluno2.get_idade()}')

    novo_nome = input('\nNovo nome: ')
    aluno1.set_nome(novo_nome)

    print(f'\nNome: ', aluno1.get_nome())    # solução 1
    aluno2.set_nome('Alice')    # solução 2

    print(f'\nNome: ', aluno2.get_nome())
    print(aluno2)

    aluno1.mostra_dados()
    aluno1.mostra_dados2()  # Solução 1
    Aluno.mostra_dados2(aluno2)  # solução 2

    print(f'\nDados concatenados: {aluno1.retorna_dados()}')
    print(f'\nDados concatenados: {aluno2.retorna_dados()}')

    aluno1.aumento_mensalidade_valor_1(110)
    print(f'\nNova mensalidade: {aluno1.get_mensalidade()}')

    aluno2.aumento_mensalidade_valor_1(110)
    print(f'\nNova Mensalidade: {aluno2.get_mensalidade()}')

    aluno1.aumento_mensalidade_porcentagem(10)
    print(f'\nNova mensalidade: {aluno1.get_mensalidade()}')

    aluno3 = Aluno('Ailton')
    aluno3.mostra_dados()

    aluno4 = Aluno('Marcelo', 1200)
    aluno4.mostra_dados()

    aluno5 = Aluno('Jagunço', idade=19)
    aluno5.mostra_dados()

    aluno6 = Aluno(idade=29, nome='Jessica')
    aluno6.mostra_dados()

    aluno1.pode_cnh()
