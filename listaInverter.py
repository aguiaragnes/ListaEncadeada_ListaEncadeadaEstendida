# from listaEncadeada import ListaEncadeada


class ListaEncadeada:

    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def inserir_no_final(self, valor):
        novo_no = No(valor)
        if self.cauda is None:
            self.cabeca = novo_no
            self.cauda = novo_no
        else:
            self.cauda.prox = novo_no
            self.cauda = novo_no

    def __str__(self):
        if self.cabeca is None:
            return "Lista vazia"
        resultado = []
        atual = self.cabeca
        while atual is not None:
            resultado.append(str(atual))
            atual = atual.prox
        return " -> ".join(resultado)


class No:

    def __init__(self, carga):
        self.carga = carga
        self.prox = None


def inverterLista(lista):
    lista_invertida = ListaEncadeada()
    atual = lista.cabeca
    while atual is not None:
        lista_invertida.inserir_no_inicio(atual.carga)
        atual = atual.prox
    return lista_invertida


'''
# Exemplo de uso
lista_original = ListaEncadeada()
lista_original.inserir_no_final("A")
lista_original.inserir_no_final("B")
lista_original.inserir_no_final("C")

print("Lista Original:", lista_original)
lista_invertida = inverterLista(lista_original)
print("Lista Invertida:", lista_invertida)
'''
