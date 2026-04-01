"""
6 - Verificando Palíndromos 🔄

Descrição: Vamos testar se uma palavra é um palíndromo?!

Uma dica é: Utilize conceitos de manipulação de strings para inverter a 
palavra e comparar com a original.

O que aprenderemos?

Manipulação de strings em Python, especialmente invertendo uma string.
Compreensão de como comparar a string original com sua versão invertida 
para determinar se é um palíndromo.
Introdução ao conceito de palíndromos e sua aplicação em problemas de programação.
"""
def is_palindrome(word):
    # Remove espaços e converte para minúsculas
    cleaned_word = word.replace(" ", "").lower()
    
    # Inverte a palavra
    reversed_word = cleaned_word[::-1]
    
    # Compara a palavra original com a invertida
    return cleaned_word == reversed_word

# Testando a função
test_words = ["radar", "python", "Ana", "level", "palindrome"]
for word in test_words:
    if is_palindrome(word):
        print(f"'{word}' é um palíndromo.")
    else:
        print(f"'{word}' não é um palíndromo.")

# Saída esperada:
# 'radar' é um palíndromo.
# 'python' não é um palíndromo.
# 'Ana' é um palíndromo. 
# 'level' é um palíndromo.
# 'palindrome' não é um palíndromo.
  