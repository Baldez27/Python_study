dias = int(input('Quantos dias alugados? '))
distancia = float(input('Quantos KM rodados? '))
total_pagar = (dias * 60) + (distancia * 0.15)
print('O total a pagar é de R$ {:.2f}'.format(total_pagar))
