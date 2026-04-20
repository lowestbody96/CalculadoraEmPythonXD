def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero."
    return a / b

print("=== Calculadora Simples ===")

try:
    num1 = float(input("Digite o primeiro número: "))
    operador = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if operador == "+":
        resultado = somar(num1, num2)
    elif operador == "-":
        resultado = subtrair(num1, num2)
    elif operador == "*":
        resultado = multiplicar(num1, num2)
    elif operador == "/":
        resultado = dividir(num1, num2)
    else:
        resultado = "Erro: operador inválido."

    print("Resultado:", resultado)

except ValueError:
    print("Erro: digite apenas números válidos.")
