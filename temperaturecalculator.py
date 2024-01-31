print("Welche Umrechnung möchten Sie durchführen:")
print("""
1: Celsius zu Fahrenheit
2: Fahrenheit zu Celsius
3: Celsius zu Kelvin
4: Kelvin zu Celsius
5: Fahrenheit zu Kelvin
6: Kelvin zu Fahrenheit""")

eingabe_auswahl = int(input("Bitte wählen Sie eine Option: (1-6)"))
eingabe_temperature = float(input("Geben Sie die Temperature an: "))

# Celsius zu Fahrenheit

if eingabe_auswahl == 1:
    fahrenheit = eingabe_temperature * 9 / 5 + 32
    print(f"{eingabe_temperature}°C entspricht {fahrenheit}°F.")
    
    
# Fahrenheit zu Celsius

if eingabe_auswahl == 2:
    celsius = (eingabe_temperature - 32) * 5 / 9
    print(f"{eingabe_temperature}°F entspricht {celsius}°C.")
    
# Celsius zu Kelvin

if eingabe_auswahl == 3:
    kelvin = eingabe_temperature + 273.15
    print(f"{eingabe_temperature}°C entspricht {kelvin}K.")
    
# Kelvin zu Celsius


