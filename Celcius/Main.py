# Program Konversi Suhu
print(''' 
=================================
+ + + Program Konversi Suhu + + +
=================================
''')
# Peng-inputan
Celcius = float(input("Masukan SUhu Dalam Celcius: "))
print('\n' + 30*'^' + '\n')
print("suhu adalah",Celcius, "Celcius\n")

# Reamur
Reamur = (4/5) * Celcius
print(f'Suhu Dalam Reamur Adalah: { Reamur } Celcius\n')

# Fahrenheit
Fahrenheit = ((9/5) * Celcius) + 32
print(f'Suhu Dalam Fahrenheit Adalah: { Fahrenheit } Celcius\n')

# Kelvin
Kelvin = Celcius + 273
print(f'Suhu Dalam Kelvin Adalah: { Kelvin } Celcius\n')
print(30*'^')