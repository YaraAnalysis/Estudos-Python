class Animal:
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho

    def respirar(self):
        print(f'O animal {self.nome} está respirando.')
        print(f'O tamanho dele é {self.tamanho}.')