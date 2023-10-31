#questao 4
#ANTONIO ALDENI ALVES VASCONCELOS FILHO

def ordenar_pessoas_por_nome(lista_de_pessoas):
  # Usando a função sorted para ordenar a lista de pessoas com base no primeiro elemento de cada tupla (o nome).
  lista_ordenada = sorted(lista_de_pessoas, key=lambda pessoa: pessoa[0])
  return lista_ordenada

# Exemplo de uso:
lista_de_pessoas = [("Alice", 25), ("Carlos", 30), ("Bianca", 22)]
lista_ordenada = ordenar_pessoas_por_nome(lista_de_pessoas)
print(lista_ordenada)
