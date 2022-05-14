salarioHora = float(input("Quanto voce ganha por hora ?"))
horas = int(input("Quantas horas trabalhadas no mês ? "))
salarioTotal = salarioHora * horas
IR = 0.11
INSS = 0.08
Sindicato = 0.05
impostos = IR + INSS + Sindicato
descontos = salarioTotal * impostos
salarioLiquido = salarioTotal - descontos
print("Seu salário líquido é {}".format(salarioLiquido))
