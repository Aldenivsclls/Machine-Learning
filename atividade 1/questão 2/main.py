#questao 2
#ANTONIO ALDENI ALVES VASCONCELOS FILHO

def elementos_unicos(lista1, lista2):
  # Crie um conjunto com os elementos das duas listas para eliminar duplicatas
  conjunto1 = set(lista1)
  conjunto2 = set(lista2)

  # Calcule a diferença simétrica para obter elementos únicos em cada lista
  elementos_unicos_lista1 = conjunto1.symmetric_difference(conjunto2)

  # Converta o resultado de volta em uma lista
  lista_resultante = list(elementos_unicos_lista1)

  return lista_resultante

# Exemplo de uso:
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
resultado = elementos_unicos(lista1, lista2)
print(resultado)  # Isso imprimirá [1, 2, 6, 7]
