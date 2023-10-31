#questao 3
#ANTONIO ALDENI ALVES VASCONCELOS FILHO

def segundo_maior(lista):
  if len(lista) < 2:
      return "A lista deve ter pelo menos dois elementos."

  primeiro_max = segundo_max = float('-inf')

  for numero in lista:
      if numero > primeiro_max:
          segundo_max = primeiro_max
          primeiro_max = numero
      elif primeiro_max > numero > segundo_max:
          segundo_max = numero

  if segundo_max == float('-inf'):
      return "Não há segundo maior valor."

  return segundo_max

# Exemplo de uso:
lista_numeros = [10, 5, 8, 20, 15]
resultado = segundo_maior(lista_numeros)
print(f"O segundo maior valor na lista é: {resultado}")
