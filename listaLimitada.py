from listaEncadeada import ListaEncadeada


class ListaLotadaException(Exception):

    def __init__(self):
        super().__init__("A lista está lotada.")


class ListaLimitada(ListaEncadeada):

    def __init__(self, capacidade):
        super().__init__()
        self.capacidade = capacidade
        self.quantidade_atual = 0

    def inserir_no_final(self, valor):
        if self.quantidade_atual >= self.capacidade:
            raise ListaLotadaException()
        super().inserir_no_final(valor)
        self.quantidade_atual += 1

    def remover_do_final(self):
        super().remover_do_final()
        self.quantidade_atual -= 1


'''
# Exemplo de uso da classe ListaLimitada
lista_limitada = ListaLimitada(3)  # Define a capacidade máxima como 3
lista_limitada.inserir_no_final("A")
lista_limitada.inserir_no_final("B")
print(lista_limitada)  # Deve exibir: "A -> B"
print("Quantidade atual:", lista_limitada.quantidade_atual)  # Deve exibir: 2

lista_limitada.inserir_no_final("C")
print(lista_limitada)  # Deve exibir: "A -> B -> C"
print("Quantidade atual:", lista_limitada.quantidade_atual)  # Deve exibir: 3

# Tentando inserir um quarto elemento (a lista está lotada)
try:
	lista_limitada.inserir_no_final("D")
except ListaLotadaException as e:
	print("Erro:", e)

# Removendo elementos
lista_limitada.remover_do_final()
print(lista_limitada)  # Deve exibir: "A -> B"
print("Quantidade atual:", lista_limitada.quantidade_atual)  # Deve exibir: 2
'''
