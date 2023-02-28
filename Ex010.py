real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.20
euro = real / 5.65
print('Com R${:.2f} você pode comprar US${:.2f} e também Є{:.2f}'.format(real, dolar, euro))
