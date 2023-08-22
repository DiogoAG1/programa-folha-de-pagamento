import math

salarioB = float(input("Digite o salário: "))
vale = input("Descontar o Vale Transporte? ")

if salarioB < 1320.01:
    inss = salarioB * 0.075
    print(f"Calculo do INSS R${inss}")
    salarioL = (salarioB - inss)
    print("Seu salário liquído é de: R$", salarioL)
elif salarioB > 1320.00 and salarioB < 2571.30:
    inss = (salarioB - 1320) * 0.09 + 99
    print(f"Calculo do INSS R${inss}")
    salarioL = (salarioB - inss)
    print("Seu salário liquído é de: R$", salarioL)
elif salarioB > 2571.29 and salarioB < 3856.95:
    inss = (salarioB - 2571.29) * 0.12 + 99 + 112.62
    print(f"Calculo do INSS R${inss}")
    salarioL = (salarioB - inss)
    print("Seu salário liquído é de: R$", salarioL)
elif salarioB > 3856.94 and salarioB < 7507.50:
    inss = (salarioB - 3856.95) * 0.14 + 99 + 112.62 + 154.28
    print(f"Calculo do INSS R${inss}")
    salarioL = (salarioB - inss)
    print("Seu salário liquído é de: R$", salarioL)
elif salarioB > 7507.49:
    inss = (salarioB - 3856.95) * 0.14 + 99 + 112.62 + 154.28
    print(f"Calculo do INSS R${inss}")
    salarioL = (salarioB - inss)
    print("Seu salário liquído é de: R$", salarioL)
else:
    print("Ops! Algo deu errado contacte seu programador!")

if vale == "s" or vale == "S":
    valVale = (salarioB - inss) * 0.06
    print(f"Desconto do vale transporte é de R${valVale}")
    salarioL = (salarioB - inss) - valVale
    print("Seu salário liquído é de: R$", salarioL)

if salarioL <=1903.98:
   irrf=0
   deducao=0
elif salarioL >=1903.99 and salarioL <=2826.65:
   irrf=7.5/100
   deducao=142.80
elif salarioL >=2826.66 and salarioL <=3751.05:
   irrf=15/100
   deducao=354.80
elif salarioL >=3751.06 and salarioL <=4664.68:
   irrf=22.5/100
   deducao=636.13
else:
   irrf=27.5/100
   deducao=869.36

irrf=(salarioL*irrf)-deducao

print(f"Desconto do IRRF é de R${irrf}")

salario_final=salarioL-irrf

print(f"Seu salário final é de: R${salario_final}")
