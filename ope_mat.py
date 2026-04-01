"""
3 - Operações Matemáticas Simples 📐

Descrição: Vamos solicitar como entrada dois números e depois vamos 
realizar uma operação simples entre eles.

O que aprenderemos?

Operações Matemáticas Básicas
Entrada de dados
Utilização eficiente do Github Copilot
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

opracao = input("Digite a operação desejada (+, -, *, /): ")

if opracao == "+":
    resultado = num1 + num2
elif opracao == "-":
    resultado = num1 - num2
elif opracao == "*":
    resultado = num1 * num2
elif opracao == "/":
    resultado = num1 / num2
else:
    print("Operação inválida!")
    resultado = None

print("O resultado da operação é:", resultado)
