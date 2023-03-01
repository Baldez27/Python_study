salario = float(input('Qual é o salário do funcionário? R$ '))
aumento = salario + (salario * 0.15)
print('Um fincionário que ganhava R${:.2f}, com 15% de acréscimo, passa a receber R${:.2f}'.format(salario, aumento))
