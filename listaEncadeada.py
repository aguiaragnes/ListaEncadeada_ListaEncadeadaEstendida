class No:

    def __init__(self, carga):
        self.carga = carga
        self.prox = None

    def __str__(self):
        return str(self.carga)


class ListaEncadeada:

    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def inserir_no_inicio(self, valor):
        novo_no = No(valor)
        if self.cabeca is None:
            self.cabeca = novo_no
            self.cauda = novo_no
        else:
            novo_no.prox = self.cabeca
            self.cabeca = novo_no

    def inserir_no_final(self, valor):
        novo_no = No(valor)
        if self.cauda is None:
            self.cabeca = novo_no
            self.cauda = novo_no
        else:
            self.cauda.prox = novo_no
            self.cauda = novo_no

    def remover_do_inicio(self):
        if self.cabeca is None:
            return
        if self.cabeca == self.cauda:
            self.cabeca = None
            self.cauda = None
        else:
            self.cabeca = self.cabeca.prox

    def remover_do_final(self):
        if self.cauda is None:
            return
        if self.cabeca == self.cauda:
            self.cabeca = None
            self.cauda = None
        else:
            atual = self.cabeca
            while atual.prox != self.cauda:
                atual = atual.prox
            self.cauda = atual
            self.cauda.prox = None

    def __str__(self):
        if self.cabeca is None:
            return 'Lista vazia'
        resultado = []
        atual = self.cabeca
        while atual is not None:
            resultado.append(str(atual))
            atual = atual.prox
        return ' -> '.join(resultado)


'''
lista = ListaEncadeada()

lista.inserir_no_final(5)
lista.inserir_no_final(1)
lista.inserir_no_final(7)
lista.inserir_no_final(4)
lista.inserir_no_final(8)

print(lista)
'''
