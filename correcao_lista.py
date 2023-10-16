'''
@staticmethod
def inverter(lista):
	nova_lista = ListaEncadeada()
	atual = lista.cabeca
	while atual is not None:
		nova_lista.inserir_no_inicio(atual.carga)
		atual = atual.prox
	return nova_lista
'''


@staticmethod
def inverter(lista):
    atual = lista.cabeca
    anterior = None
    while atual is not None:
        prox = atual.prox
        atual.prox = anterior
        anterior = atual
        atual = prox
    lista.cabeca = anterior
    return lista
