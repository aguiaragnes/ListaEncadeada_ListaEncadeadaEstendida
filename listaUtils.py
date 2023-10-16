from listaEncadeada import ListaEncadeada


class ListaUtils:

    @staticmethod
    def clonar(lista):
        nova_lista = ListaEncadeada()
        atual = lista.cabeca
        while atual is not None:
            nova_lista.inserir_no_final(atual.carga)
            atual = atual.prox
        return nova_lista

    @staticmethod
    def inverter(lista):
        nova_lista = ListaEncadeada()
        atual = lista.cabeca
        while atual is not None:
            nova_lista.inserir_no_inicio(atual.carga)
            atual = atual.prox
        return nova_lista

    @staticmethod
    def join(lista, separador):
        elementos = []
        atual = lista.cabeca
        while atual is not None:
            elementos.append(str(atual))
            atual = atual.prox
        return separador.join(elementos)

    @staticmethod
    def split(string, separador):
        elementos = string.split(separador)
        nova_lista = ListaEncadeada()
        for elemento in elementos:
            nova_lista.inserir_no_final(elemento)
        return nova_lista

    @staticmethod
    def intercalar(lista1, lista2):
        nova_lista = ListaEncadeada()
        atual1 = lista1.cabeca
        atual2 = lista2.cabeca
        while atual1 is not None or atual2 is not None:
            if atual1 is not None:
                nova_lista.inserir_no_final(atual1.carga)
                atual1 = atual1.prox
            if atual2 is not None:
                nova_lista.inserir_no_final(atual2.carga)
                atual2 = atual2.prox
        return nova_lista


'''
# Exemplo de uso da classe ListaUtils
lista = ListaEncadeada()
lista.inserir_no_final("a")
lista.inserir_no_final("b")
lista.inserir_no_final("c")
lista.inserir_no_final("d")

# Clonar a lista
copia = ListaUtils.clonar(lista)
print(copia)  # Deve exibir: "a -> b -> c -> d"

# Inverter a lista
invertida = ListaUtils.inverter(lista)
print(invertida)  # Deve exibir: "d -> c -> b -> a"

# Juntar os elementos com vírgula
texto = ListaUtils.join(lista, ",")
print(texto)  # Deve exibir: "a,b,c,d"

# Dividir a string em uma lista encadeada
nova_lista = ListaUtils.split("a,b,c,d", ",")
print(nova_lista)  # Deve exibir: "a -> b -> c -> d"

# Intercalar duas listas
lista1 = ListaEncadeada()
lista1.inserir_no_final("1")
lista1.inserir_no_final("3")
lista2 = ListaEncadeada()
lista2.inserir_no_final("2")
lista2.inserir_no_final("4")
intercalada = ListaUtils.intercalar(lista1, lista2)
print(intercalada)  # Deve exibir: "1 -> 2 -> 3 -> 4"
'''
