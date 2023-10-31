#questao 5
#ANTONIO ALDENI ALVES VASCONCELOS FILHO
def encontrar_max_min(lista):
if not lista:
    return None, None  # Retorna None se a lista estiver vazia

maior = menor = lista[0]  # Inicializa o maior e o menor com o primeiro elemento

for numero in lista:
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

return maior, menor
