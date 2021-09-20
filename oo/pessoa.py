class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Ola'


if __name__ == '__main__':
    olivia = Pessoa(nome='Olivia', idade=1)
    pedro = Pessoa(olivia, nome='Pedro', idade=28)

    print(pedro.filhos)
    for filho in pedro.filhos:
        print(filho.nome)

    pedro.sobrenome = 'Lisboa'
    print(pedro.sobrenome)

    print(Pessoa.olhos)
    print(pedro.olhos)
