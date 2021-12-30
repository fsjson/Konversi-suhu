# Konversi Suhu
print(30*'=')
print('\nKONVERSI SUHU\n')
print(30*'=')
print('\n')
# input
print(30*'=')
Fahrenheit = float(input("Masukan Suhu Dalam Fahrenheit: "))
print(30*'=')
print(f'Suhu Adalah: { Fahrenheit } Fahrenheit')
# Fahrenheit ==>> Kelvin
print(30*'=')
Kelvin = (Fahrenheit - 32) * 5/9 + 273
print(f'Suhu Dalam Fahrenheit Adalah: { Kelvin } Kelvin')
# Kelvin ==>> Fahrenheit
print(30*'=')
Kelvin= float(input("Masukan Suhu Dalam Kelvin: "))
print(30*'=')
print(f'Suhu Adalah: { Kelvin } Kelvin')
print(30*'=')
Fahrenheit = (Kelvin - 273) * 9/5 + 32
print(f'Suhu Dalam Kelvin Adalah: { Fahrenheit } Fahrenheit')
print(30*'=')