"""
4 - Verificando Números Pares e Ímpares 🧮

Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 
Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça 
uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.

O que aprenderemos?

Utilização de condicionais em Python (if, else) para realizar verificações.
Introdução ao conceito de operador de módulo (%) para verificar se um número 
é par ou ímpar.
Exploração do uso de uma ferramenta de IA, como o Github Copilot, para otimizar 
a estrutura do código.
"""
# Solução utilizando condicionais e operador de módulo
def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "O número é par."
    else:
        return "O número é ímpar."

# Solução otimizada utilizando o Github Copilot
def verificar_par_ou_impar_otimizado(numero):
    return "O número é par." if numero % 2 == 0 else "O número é ímpar."

def main():
    numero = int(input("Digite um número inteiro: "))
    resultado = verificar_par_ou_impar(numero)
    print(resultado)

    resultado_otimizado = verificar_par_ou_impar_otimizado(numero)
    print(resultado_otimizado)
# Exemplo de uso
if __name__ == "__main__":
    main()
    