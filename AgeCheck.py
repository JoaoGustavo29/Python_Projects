idade = int(input("Informe a idade: "))

if idade <= 3:
    print(f"{idade} anos. É um bebê.")
elif idade <= 10:
    print(f"{idade} anos. É uma criança.")
elif idade <= 17:
    print(f"{idade} anos. É um adolescente.")
elif idade <= 40:
    print(f"{idade} anos. É um adulto.")

elif idade <= 60:
    print(f"{idade} anos. É um adulto 2.")
else:
    print(f"{idade} anos. É um idoso.")
