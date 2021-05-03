nome = input('Qual seu Nome? ')
idade = int(input('Qual sua idade? '))
altura = float(input('Qual sua altura? '))
peso = float(input('Qual seu peso? '))
imc = peso / (altura ** 2)

# Parâmetros IMC
magreza = imc <= 18.4
normal = 18.5 <= imc <= 24.9
sobrepeso = 25.0 <= imc <= 29.9
obesidade = 30.0 <= imc <= 39.9

if magreza:
    print(f'{nome} tem {idade} anos e {altura} de altura, atualmente pesa {peso}kg. Seu IMC é igual a: {imc:.2f},'
          f'você se encontra com magreza.')
elif normal:
    print(f'{nome}, Você se encontra com um IMC igual a: {imc:.2f}, onde é classificado como normal.')
elif sobrepeso:
    print(f'{nome}, seu IMC é igual a: {imc:.2f}, classificado como sobrepeso.')
elif obesidade:
    print(f'{nome}, seu IMC é igual a: {imc:.2f}, classificado como obesidade.')
else:
    print(f'{nome}, seu IMC é igual a: {imc:.2f}, classificado como obesidade grave.')
