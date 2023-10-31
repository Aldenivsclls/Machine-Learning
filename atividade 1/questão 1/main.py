#questao 1
#ANTONIO ALDENI ALVES VASCONCELOS FILHO


def is_prime(n):
  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True


def prime_numbers_in_list(numbers):
  prime_list = []
  for num in numbers:
    if is_prime(num):
      prime_list.append(num)
  return prime_list


# Exemplo de uso:
numbers = [2, 3, 4, 5, 6, 7, 8, 9]
prime_numbers = prime_numbers_in_list(numbers)
print(prime_numbers)
