# Exercício Python 18: Escreva um programa que leia dois números
# inteiros e compare-os. mostrando na tela uma mensagem:
#
# – O primeiro valor é maior
#
# – O segundo valor é maior
#
# – Não existe valor maior, os dois são iguais
print("números")
num1= int(input("Digite o número 1:"))
num2= int(input("Digite o número 2:"))

if num1==num2:
    print("Os dois são iguais.")
elif num1>num2:
    print("o número 1 é o maior.")
else:
    print("o número 2 é o maior.")