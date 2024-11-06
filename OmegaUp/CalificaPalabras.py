
# %%
def calificador(ascii_value):
    ascii_value = ord(ascii_value)

    if ascii_value >= 48 and ascii_value <= 57: 
        suma = int(chr(ascii_value))

    elif ascii_value >= 97 and ascii_value <= 122:
        suma = ascii_value - 87

    elif ascii_value >= 65 and ascii_value <= 90:
        suma = (ascii_value - 55)*2
    else:
        suma = 0

    return suma

Ana = input()
Caro = input()

suma_A = 0
for caracter in Ana:
    suma_A = suma_A + calificador(caracter)

suma_C = 0
for caracter in Caro:
    suma_C = suma_C + calificador(caracter)

if suma_A > suma_C:
    print('Ana ', suma_A)
else:
    print('Carolina ', suma_C)


