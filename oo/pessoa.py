class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return 'Ola'


if __name__ == '__main__':
    p = Pessoa()
    print(p.cumprimentar())
    print(p.nome)

