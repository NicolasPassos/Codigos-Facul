print("Informe de qual unidade de medida de temperatura deseja partir")
print("Digite 1 para Celsius, 2 para Farenheit e 3 para Kelvin")
a = int(input(""))
print("")
print("Informe para qual unidade de medida de temperatura deseja converter")

if a == 1:
    print("Digite 1 para converter em Farenheit e 2 para converter em Kelvin")
    b = int(input(""))

    if b == 1:
        print("Informe a temperatura em celsius que deseja converter")
        valor1 = float(input(""))
        calculo = (valor1 * 9/5) + 32
        print("")
        print("A temperatura ",valor1," ºC em Farenheit é: ",calculo," ºF.")
    if b == 2:
        print("Informe a temperatura em celsius que deseja converter")
        valor1 = float(input(""))
        calculo = valor1 + 273
        print("")
        print("A temperatura ",valor1," ºC em Kelvin é: ",calculo," K.")  
if a == 2:
    print("Digite 1 para converter em Celsius e 2 para converter em Kelvin")
    b = int(input(""))
    if b == 1:
        print("Informe a temperatura em Farenheit que deseja converter")
        valor1 = float(input(""))
        calculo = (valor1 - 32) * 5/9
        print("")
        print("A temperatura ",valor1," ºF em Celsius é: ",calculo," ºC.")
    if b == 2:
        print("Informe a temperatura em Farenheit que deseja converter")
        valor1 = float(input(""))
        calculo = 5 * (valor1-32)/9 + 273.15
        print("")
        print("A temperatura ",valor1," ºF em Kelvin é: ",calculo," K.")
if a == 3:
    print("Digite 1 para converter em Farenheit e 2 para converter em Celsius")
    b = int(input(""))
    if b == 1:
        print("Informe a temperatura em Kelvin que deseja converter")
        valor1 = float(input(""))
        calculo = valor1 * 1.8 - 459.67
        print("")
        print("A temperatura ",valor1," K em Farenheit é: ",calculo," ºF.")
    if b == 2:
        print("Informe a temperatura em Kelvin que deseja converter")
        valor1 = float(input(""))
        calculo = valor1 - 273
        print("")
        print("A temperatura ",valor1," K em Celsius é: ",calculo," ºC.")