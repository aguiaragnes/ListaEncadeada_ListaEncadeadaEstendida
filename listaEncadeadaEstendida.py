from listaEncadeada import ListaEncadeada


class ListaEncadeadaEstendida(ListaEncadeada):

    def pares(self):
        valores_pares = []
        atual = self.cabeca
        while atual is not None:
            if atual.carga % 2 == 0:
                valores_pares.append(atual.carga)
            atual = atual.prox
        return valores_pares

    def impares(self):
        valores_impares = []
        atual = self.cabeca
        while atual is not None:
            if atual.carga % 2 != 0:
                valores_impares.append(atual.carga)
            atual = atual.prox
        return valores_impares

    def buscar_pos(self, valor):
        pos = 0
        atual = self.cabeca
        while atual is not None:
            if atual.carga == valor:
                return pos
            atual = atual.prox
            pos += 1
        return -1

    def inserir_pos(self, pos, valor):
        novo_no = No(valor)
        if pos == 0:
            novo_no.prox = self.cabeca
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            for i in range(pos - 1):
                if atual is None:
                    return
                atual = atual.prox
            if atual is not None:
                novo_no.prox = atual.prox
                atual.prox = novo_no

    def remover_de_posicao(self, pos):
        if pos == 0:
            self.remover_do_inicio()
        else:
            atual = self.cabeca
            for i in range(pos - 1):
                if atual is None:
                    return
                atual = atual.prox
            if atual is not None and atual.prox is not None:
                atual.prox = atual.prox.prox

    def remover_ocorrencias(self, valor):
        anterior = None
        atual = self.cabeca
        while atual is not None:
            if atual.carga == valor:
                if anterior is None:
                    self.cabeca = atual.prox
                else:
                    anterior.prox = atual.prox
            else:
                anterior = atual
            atual = atual.prox


'''
# Exemplo de uso da classe ListaEncadeadaEstendida
lista_estendida = ListaEncadeadaEstendida()
lista_estendida.inserir_no_final(1)
lista_estendida.inserir_no_final(2)
lista_estendida.inserir_no_final(3)
lista_estendida.inserir_no_final(4)
lista_estendida.inserir_no_final(2)
print(lista_estendida)  # Deve exibir: "1 -> 2 -> 3 -> 4 -> 2"

print("Valores pares:", lista_estendida.pares())  # Deve exibir: [2, 4, 2]
print("Valores ímpares:", lista_estendida.impares())  # Deve exibir: [1, 3]
print("Posição do valor 3:", lista_estendida.buscar_pos(3))  # Deve exibir: 2
lista_estendida.inserir_pos(1, 5)
print(lista_estendida)  # Deve exibir: "1 -> 5 -> 2 -> 3 -> 4 -> 2"
lista_estendida.remover_de_posicao(3)
print(lista_estendida)  # Deve exibir: "1 -> 5 -> 2 -> 4 -> 2"
lista_estendida.remover_ocorrencias(2)
print(lista_estendida)  # Deve exibir: "1 -> 5 -> 4"
'''
