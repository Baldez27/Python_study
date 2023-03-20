name = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}'.format(name.upper()))
print('Seu nome em minúsculo é {}'.format(name.lower()))
print('Seu nome tem ao todo {} letras'.format(len(name) - name.count(' '))) 
#print('Seu primeiro nome tem {} letras'.format(name.find(' ')))
separa = name.split()
print('Seu primeiro nome é {}, ele tem {} letras'.format(separa[0], len(separa[0])))
