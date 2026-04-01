"""
5 - Calculando Média de Notas 📚

Descrição: Agora vamos calcular a média de três notas fornecidas na entrada 
do usuário. Uma dica é: Utilize operadores aritméticos para realizar o 
cálculo da média.

O que aprenderemos?

Uso de variáveis para armazenar dados fornecidos pelo usuário.
Aplicação de operadores aritméticos (+, /) para calcular a média de um 
conjunto de valores.
Prática na solicitação e manipulação de entrada do usuário.
"""
# Solução:
# Solicitar as notas do usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcular a média
media = (nota1 + nota2 + nota3) / 3

# Exibir a média para o usuário
print(f"A média das notas é: {media:.2f}")
