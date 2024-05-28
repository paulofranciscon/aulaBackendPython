taxa_euro = 5.56
valor_real = float(input('Digite o valor em real: R$ '))
valor_iene = 30.32
valor_peso_argentino = 172.72

print(f'EURO:            {valor_real / taxa_euro:.2f}')
print(f'IENE JAPONES:    {valor_iene * valor_real:.2f}')
print(f'PESO ARGENTINO:  {valor_peso_argentino * valor_real:.2f}')