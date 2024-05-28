import requests

response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
data = response.json()
taxa_dolar = float(data['USDBRL']['bid'])

print((response))
print(f" Taxa do dolar é R$: {taxa_dolar:.2f}")