print("""***************************************

----- Bienvenido al conversor de unidades -----
""")

# Variables
salir = False

# Funciones de temperatura
def celsius_fahrenheit(valor_celsius_user):
    resultado_celsius = (valor_celsius_user * 9/5)+32
    return resultado_celsius
def fahrenheit_celsius(valor_fahrenheit_user):
    resultado_fahrenheit = (valor_fahrenheit_user -32)*(5/9)
    return resultado_fahrenheit
def kelvin_celsius(valor_kelvin_celsius_user):
    resultado_kelvin_celsius = (valor_kelvin_celsius_user - 273.15)
    return resultado_kelvin_celsius
def celsius_kelvin(valor_celsius_kelvin_user):
    resultado_celsius_kelvin = (valor_celsius_kelvin_user + 273.15)
    return resultado_celsius_kelvin
def kelvin_fahrenheit(valor_kelvin_fahrenheit_user):
    resultado_kelvin_fahrenheit = ((valor_kelvin_fahrenheit_user - 273.15)*(9/5))+32
    return resultado_kelvin_fahrenheit
def fahrenheit_kelvin(valor_fahrenheit_kelvin_user):
    resultado_fahrenheit_kelvin = ((valor_fahrenheit_kelvin_user - 32)*(5/9))+273.15
    return resultado_fahrenheit_kelvin

# Funciones de longitud
def cm_km(valor_cm_km_user):
    resultado = valor_cm_km_user / 100000
    return resultado
def km_cm(valor_km_cm_user):
    resultado = valor_km_cm_user * 100000
    return resultado
def m_cm(valor_m_cm_user):
    resultado = valor_m_cm_user * 100
    return resultado
def cm_m(valor_cm_m_user):
    resultado = valor_cm_m_user / 100
    return resultado
def m_km(valor_m_km_user):
    resultado = valor_m_km_user / 1000
    return resultado
def km_m(valor_km_m_user):
    resultado = valor_km_m_user * 1000
    return resultado


# Desarrollo del programa
while (salir == False):
    print("""\n***************************************

    1. Temperatura
    2. Longitud
    3. Salir del programa

***************************************""")
    option_user = int(input("\n¿Qué opción quieres elegir? -"))

    if option_user == 1:
        print("""***************************************
        
        Selecciona la opción que deseas:
        
        1. Celsius -> Fahrenheit
        2. Fahrenheit -> Celsius
        3. Kelvin -> Celsius
        4. Celsius -> Kelvin
        5. Kelvin -> Fahrenheit
        6. Fahrenheit -> Kelvin
        
***************************************""")
        option_user = int(input("\n¿Qué opción quieres elegir? -"))
        if option_user == 1:
            valor_celsius_user = float(input("\n¿Qué valor en Celsius quieres convertir? -"))
            print(f""" *****************************************
         {valor_celsius_user} °C es igual a {celsius_fahrenheit(valor_celsius_user):.2f} °F
 *****************************************""")
        elif option_user == 2:
            valor_fahrenheit_user = float(input("\n¿Qué valor en Fahrenheit quieres convertir? -"))
            print(f""" *****************************************
         {valor_fahrenheit_user} °F es igual a {fahrenheit_celsius(valor_fahrenheit_user):.2f} °C
 *****************************************""")
        elif option_user == 3:
            valor_kelvin_user = float(input("\n¿Qué valor en Kelvin quieres convertir? -"))
            print(f""" *****************************************
        {valor_kelvin_user} K es igual a {kelvin_celsius(valor_kelvin_user):.2f} °C 
 *****************************************""")
        elif option_user == 4:
            valor_celsius_kelvin_user = float(input("\n¿Qué valor en Celsius quieres convertir? -"))
            print(f""" *****************************************"
        {valor_celsius_kelvin_user} °C es igual a {celsius_kelvin(valor_celsius_kelvin_user):.2f} K "
 *****************************************""")
        elif option_user == 5:
            valor_kelvin_fahrenheit_user = float(input("\n¿Qué valor en Kelvin quieres convertir? -"))
            print(f""" *****************************************
        {valor_kelvin_fahrenheit_user} K es igual a {kelvin_fahrenheit(valor_kelvin_fahrenheit_user):.2f} °F 
 *****************************************""")
        elif option_user == 6:
            valor_fahrenheit_kelvin_user = float(input("\n¿Qué valor en Fahrenheit quieres convertir? -"))
            print(f""" *****************************************
        {valor_fahrenheit_kelvin_user} °F es igual a {fahrenheit_kelvin(valor_fahrenheit_kelvin_user):.3f} K
 *****************************************""")

    elif option_user == 2:
        print("""***************************************
        Selecciona la opción que deseas:
    
        1. Centímetro -> Kilómetro
        2. Kilómetro -> Centímetro
        3. Metro -> Centímetro
        4. Centímetro -> Metro
        5. Metro -> Kilómetro
        6. Kilómetro -> Metro
    
***************************************""")
        option_user = int(input("\n¿Qué opción quieres elegir? -"))
        if option_user == 1:
            valor_cm_km_user = float(input("\n¿Qué valor en centímetros quieres convertir? -"))
            print(f""" *****************************************
                {valor_cm_km_user} cm es igual a {cm_km(valor_cm_km_user):.2f} km
 *****************************************""")
        elif option_user == 2:
            valor_km_cm_user = float(input("\n¿Qué valor en kilómetros quieres convertir? -"))
            print(f""" *****************************************
                {valor_km_cm_user} km es igual a {km_cm(valor_km_cm_user):.2f} cm
 *****************************************""")
        elif option_user == 3:
            valor_m_cm_user = float(input("\n¿Qué valor en metros quieres convertir? -"))
            print(f""" *****************************************
                {valor_m_cm_user} m es igual a {m_cm(valor_m_cm_user):.2f} cm
 *****************************************""")
        elif option_user == 4:
            valor_cm_m_user = float(input("\n¿Qué valor en centímetros quieres convertir? -"))
            print(f""" *****************************************
                {valor_cm_m_user} cm es igual a {cm_m(valor_cm_m_user):.2f} m
 *****************************************""")
        elif option_user == 5:
            valor_m_km_user = float(input("\n¿Qué valor en metros quieres convertir? -"))
            print(f""" *****************************************
                {valor_m_km_user} m es igual a {m_km(valor_m_km_user):.2f} km
 *****************************************""")
        elif option_user == 6:
            valor_km_m_user = float(input("\n¿Qué valor en kilómetros quieres convertir? -"))
            print(f""" *****************************************
                {valor_km_m_user} km es igual a {km_m(valor_km_m_user):.2f} m
 *****************************************""")

    elif option_user == 3:
        print("\n**** Gracias por utilizar el sistema ****")
        salir = True