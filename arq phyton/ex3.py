sexo = str(input("Você é um Homem ou uma Mulher ?")).strip().lower()
if sexo=="homem":
    altura = float(input("Escreva sua altura"))
    pesoIdeal = (72.7*altura) - 58
    print("Seu peso ideal é {}".format(pesoIdeal))
elif sexo=="mulher":
    altura = float(input("Escreva sua altura"))
    pesoIdeal = (62.1*altura) - 44.7
    print("Seu peso ideal é {}".format(pesoIdeal))