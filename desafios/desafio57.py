r = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while r not in 'MmFf':
    r = str(input('Dados invalidos. Por favor, infome seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(r))