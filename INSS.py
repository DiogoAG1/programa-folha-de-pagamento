# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import math

salarioB = float(input("Digite o salário: "))
vale =  input("Descontar o Vale Transporte? ")

if salarioB <1302.00:
    inss = salarioB*0.075
    print (f"Calculo do INSS R${inss}")
    print ("Seu salário liquído sem INSS é de: R$", (salarioB-inss))
elif salarioB <2571.29:
    inss = salarioB*0.09
    print (f"Calculo do INSS R${inss}")
    print ("Seu salário liquído é de: R$", (salarioB-inss))
elif salarioB <3856.94:
    inss = salarioB*0.12
    print (f"Calculo do INSS R${inss}")
    print ("Seu salário liquído é de: R$", (salarioB-inss))
elif salarioB <7507.50:
    inss = salarioB*0.14
    print (f"Calculo do INSS R${inss}")
    print ("Seu salário liquído é de: R$", (salarioB-inss))
elif salarioB >3856.95:
    inss = salarioB-876.95
    print (f"Calculo do INSS R${inss}")
    print ("Seu salário liquído é de: R$", (salarioB-inss))
if vale == "s" or vale == "S":  
    valVale = salarioB*0.06
    salarioB = salarioB - valVale
    print ("Seu salário liquído é de: R$", (salarioB-inss-valVale))
    