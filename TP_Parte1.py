##### MARCO ####
# Programa para una agencia de venta de paquetes turisticos, el que lo usa es el empleado de la agencia

import time
import random

# Funcion de convertir numeros a palabras
def numero_a_palabras(numero):
    unidades = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    centenas = ["","ciento", "docientos", "trecientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
    especiales = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciseis", "diecisiete", "dieciocho", "diecinueve"]
    
    if 0 <= numero < 10:
        return unidades[numero]
    elif 10 <= numero < 20:
        return especiales[numero - 10]
    elif 20 <= numero < 100:
        if numero % 10 == 0:
            return decenas[numero // 10]
        else:
            return decenas[numero // 10] + " y " + unidades[numero % 10]
    else:
        return numero

# Funcion de verificar si un año es bisiesto
def es_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

# Funcion de validar la fecha
def validar_fecha(viaje_anio, viaje_mes, viaje_dia, anio_actual, mes_actual, dia_actual):
    if viaje_mes < 1 or viaje_mes > 12:
        print("Mes no valido. Por favor, intente nuevamente.")
        return True
    if viaje_dia < 1:
        print("Dia no valido. Por favor, intente nuevamente.")
        return True
    if viaje_mes in [4, 6, 9, 11] and viaje_dia > 30:
        print("Dia no valido para el mes dado. Por favor, intente nuevamente.")
        return True
    if viaje_mes == 2:
        if es_bisiesto(viaje_anio) and viaje_dia > 29:
            print("Dia no valido para febrero en un año bisiesto. Por favor, intente nuevamente.")
            return True
        elif not es_bisiesto(viaje_anio) and viaje_dia > 28:
            print("Dia no valido para febrero en un año no bisiesto. Por favor, intente nuevamente.")
            return True
    if viaje_dia > 31:
        print("Dia no valido. Por favor, intente nuevamente.")
        return True
    if (viaje_anio < anio_actual) or (viaje_anio == anio_actual and viaje_mes < mes_actual) or (viaje_anio == anio_actual and viaje_mes == mes_actual and viaje_dia < dia_actual):
        print("Fecha no valida. Por favor, intente nuevamente.")
        return True
    return False

### FACU ###

# Funcion para agregar paquetes a la matriz
def agregar_paquete(paquetes, destino, dias, transporte, hotel, precio, disponibilidad, identificador):
    paquete = [destino, dias, transporte, hotel, precio, disponibilidad,identificador+1]
    paquetes.append(paquete)

# Funcion para mostrar los paquetes (pueden ser todos o algunos dependiendo la busqueda)
def mostrar_paquetes(disponibles):
    if disponibles:
        print("")
        print("Paquetes disponibles: ")
        print("")
        print(f"{'Destino':^18} | {'Dias':^5} | {'Aerolinea':^25} | {'Hotel':^28} | {'Precio':^8} | {'Disponibilidad':^16} | {'ID':^2}") 
        print("-" * 120)
        for paquete in disponibles:
            print(f"{paquete[0]:18} {paquete[1]:^10} {paquete[2]:27} {paquete[3]:30} {paquete[4]:>5}$ {paquete[5]:^12} {paquete[6]:^20}")
    else:
        print("No se encontraron paquetes disponibles.")

# Funcion generar factura
def generar_factura(paquete, clientes, cantidad_personas, fecha_viaje, numero_reserva):
    print()
    print("-" * 90)
    print("Agencia de Viajes 'Destinos Splinter'".center(90))
    print()
    print("Numero de reserva: ", str(numero_reserva).zfill(8))
    print()
    
    print(f"Destino: {paquete[0]}".ljust(30, '.'), end="")
    print(f"Fecha del viaje: {fecha_viaje}".rjust(60, '.')) 
    
    print(f"Aerolinea: {paquete[2]}".ljust(50, '.'), end="")
    print(f"Dias: {paquete[1]}".rjust(40, '.'))
    
    print(f"Hotel: {paquete[3]}".ljust(50, '.'), end="")
    print(f"Precio por persona: {paquete[4]}$".rjust(40, '.'))
    
    print(f"Cantidad de personas: {cantidad_personas}".ljust(50, '.'), end="")
    print(f"Total: {paquete[4] * cantidad_personas}$".rjust(40, '.'))
    
    print()
    print("Pasajeros:")
    
    for i in range(len(clientes)):
        cliente = clientes[i]
        print(f"Pasajero {i+1}: {cliente['nombre']}, DNI: {cliente['dni']}")
    
    print("-" * 90)

### MARTIN ###

# Funcion generar numero de reserva
def generar_numero_reserva():
    nuevo_numero = len(numeros_reserva) + 1
    return nuevo_numero

# Funcion para agregar una reserva a la lista de reservas
def agregar_reserva(paquete, clientes, cantidad_personas, fecha_viaje, numero_reserva):
    reserva = {
        'numero_reserva': numero_reserva,
        'paquete': paquete,
        'clientes': clientes,
        'cantidad_personas': cantidad_personas,
        'fecha_viaje': fecha_viaje
    }
    reservas.append(reserva)


### FACU ###

# Funcion para mostrar las reservas
def mostrar_reservas(reservas):
    if reservas == []:
        print("No hay reservas realizadas.")
    else:
        print("Reservas realizadas:")
        print("")
        print("-" * 50)
        for reserva in reservas:
            print(f"Numero de reserva: {reserva['numero_reserva']}")
            print(f"Destino: {reserva['paquete'][0]}")
            print(f"Fecha del viaje: {reserva['fecha_viaje']}")
            print(f"Cantidad de pasajeros: {reserva['cantidad_personas']}")
            print("Clientes:")
            for cliente in reserva['clientes']:
                print(f"  Nombre: {cliente['nombre']}, DNI: {cliente['dni']}")
            print("-" * 50)

# Programa principal

# Matriz de paquetes hardcodeada
# [Destino, Dias, Aerolinea, Hotel, Precio, Disponibilidad, ID]
identificador = 22
paquetes = [
    ["Barcelona", 6, "Iberia", "Hotel NH Barcelona", 1450, 12, 1],
    ["Berlin", 6, "Lufthansa", "Berlin Plaza Hotel", 1500, 10, 2],
    ["Berlin", 8, "Delta Airlines", "Berlin Central Hotel", 1600, 8, 3],
    ["Ciudad de Mexico", 9, "Aeromexico", "Hotel CDMX", 1350, 4, 4],
    ["Londres", 4, "British Airways", "The London Inn", 1500, 5, 5],
    ["Londres", 5, "Aerolineas Argentinas", "The London Inn", 1550, 8, 6],
    ["Londres", 5, "British Airways", "The London Inn", 1450, 2, 7],
    ["Londres", 6, "Lufthansa", "The London Inn", 1600, 2, 8],
    ["Madrid", 7, "Iberia", "Hotel Madrid Centro", 1550, 9, 9],
    ["Madrid", 5, "Air Europa", "Hotel Madrid Centro", 1500, 3, 10],
    ["Nueva Delhi", 8, "British Airways", "Delhi Palace Hotel", 2100, 10, 11],
    ["Nueva York", 10, "Aerolineas Splinter", "NYC Plaza", 1800, 8, 12],
    ["Nueva York", 12, "Delta Airlines", "NYC Plaza", 1900, 12, 13],
    ["Nueva York", 8, "Delta Airlines", "The Central Park North", 1600, 2, 14],
    ["Rio de Janeiro", 7, "LATAM Airlines", "Hotel Atlantico Copacabana", 1050, 10, 15],
    ["Rio de Janeiro", 5, "Aerolinas Argentinas", "Hotel Atlantico Copacabana", 900, 5, 16],
    ["Rio de Janeiro", 10, "LATAM Airlines", "Hotel Atlantico Copacabana", 1250, 20, 17],
    ["Seul", 5, "Delta Airlines", "Seoul Central Hotel", 1450, 15, 18],
    ["Sidney", 8, "Delta Airlines", "Sydney Harbour Hotel", 2200, 4, 19],
    ["Tokyo", 7, "Delta Airlines", "Tokyo Grand Hotel", 2000, 5, 20],
    ["Paris", 7, "Air France", "Hotel Parisien", 1700, 8, 21],
    ["Paris", 5, "Air France", "Hotel Parisien", 1400, 9, 22]
]

#### MARCO ####

# Lista de los nombres de los meses
nombres_meses = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]

# Obtener fecha actual
fecha_actual = time.localtime()
anio_actual, mes_actual, dia_actual = fecha_actual.tm_year, fecha_actual.tm_mon, fecha_actual.tm_mday

### NACHO ###

# Tupla para almacenar los numeros de reserva
numeros_reserva = list()

# Lista para almacenar las reservas
reservas = []

# Diccionario de funciones de busqueda
criterios_busqueda = {
    "1": lambda paquetes, destino: [paquete for paquete in paquetes if paquete[0] == destino],
    "2": lambda paquetes, dias: [paquete for paquete in paquetes if paquete[1] == int(dias)],
    "3": lambda paquetes, precio: [paquete for paquete in paquetes if paquete[4] <= int(precio)],
    "4": lambda paquetes, hotel: [paquete for paquete in paquetes if paquete[3] == hotel],
    "5": lambda paquetes, aerolinea: [paquete for paquete in paquetes if paquete[2] == aerolinea],
    "6": lambda paquetes, ID: [paquete for paquete in paquetes if paquete[6] == int(ID)]
}

print("--- Sistema de busqueda y reserva de paquetes turisticos ---")

opcion = 0
while opcion != 5:
    print("\n1. Agregar paquete")
    print("2. Busqueda y reserva de paquete")
    print("3. Mostrar todos los paquetes disponibles")
    print("4. Mostrar reservas")
    print("5. Salir")
        
    opcion = int(input("\nSeleccione una opcion: "))
    print("")
    
    if opcion == 1:
        destino = input("Ingrese el destino: ")
        dias = int(input("Ingrese la cantidad de dias: "))
        transporte = input("Ingrese la aerolinea: ")
        hotel = input("Ingrese el nombre del hotel: ")
        precio = int(input("Ingrese el precio: "))
        disponibilidad = int(input("Ingrese cuanta disponibilidad hay para el paquete: "))
        agregar_paquete(paquetes, destino, dias, transporte, hotel, precio, disponibilidad, identificador)
        identificador = identificador + 1
        print("Paquete agregado con exito.")

    elif opcion == 2:
        
        cantidad_personas = int(input("¿Cuantas personas van a viajar? (Hasta 30 personas): "))
        
        # validamos el numero de personas
        while not (0 < cantidad_personas <= 30):
                print("Numero de personas no valido, ingrese de nuevo.")
                cantidad_personas = int(input("¿Cuantas personas van a viajar?: "))
        
        paquetes_buscados = [paquete for paquete in paquetes if paquete[5] >= cantidad_personas]

        if paquetes_buscados == []:
            print(f"No hay paquetes disponibles con una disponibilidad para {cantidad_personas} personas.")
        
        else:
            # empezamos con la busqueda
            print("Seleccione el criterio de busqueda: ")
            print("1. Por destino")
            print("2. Por dias")
            print("3. Por precio")
            print("4. Por hotel")
            print("5. Por aerolinea")
            print("6. Por ID")

            mensajes_busqueda = {
                "1": "Ingrese el destino que desea buscar: ",
                "2": "Ingrese la cantidad de dias que desea buscar: ",
                "3": "Ingrese el precio maximo que desea buscar: ",
                "4": "Ingrese el hotel que desea buscar: ",
                "5": "Ingrese la areolinea que desa buscar: ",
                "6": "Ingrese el ID que desa buscar: "
            }
            
            while True:
                criterio_opcion = input("Ingrese el numero de criterio de busqueda: ")
                
                if criterio_opcion in criterios_busqueda:
                    valor = input(mensajes_busqueda[criterio_opcion])
                    print(valor)
                    # busqueda de paquetes con diccionario de funciones
                    paquetes_buscados = criterios_busqueda[criterio_opcion](paquetes_buscados, valor)
                    mostrar_paquetes(paquetes_buscados)
                    break
                
                else:
                    print("Opcion no valida. Intente de nuevo.")
        
        while len(paquetes_buscados) > 1:
            print("\nAun hay varios paquetes disponibles. Refine su busqueda")
            print("1. Por destino")
            print("2. Por dias")
            print("3. Por precio")
            print("4. Por hotel")
            print("5. Por aerolinea")
            print("6. Por ID")
            
            while True:
                criterio_opcion = input("Ingrese el numero de criterio de busqueda: ")
                
                if criterio_opcion in criterios_busqueda:
                    valor = input(mensajes_busqueda[criterio_opcion])
                    # busqueda de paquetes con diccionario de funciones
                    paquetes_buscados = criterios_busqueda[criterio_opcion](paquetes_buscados, valor)
                    mostrar_paquetes(paquetes_buscados)
                    break
                else:
                    print("Opcion no valida. Intente de nuevo.")
  
#### MARTIN ####
  
        #Sistema de reserva
        if len(paquetes_buscados) == 1:
            print("\n--- Reserva de Paquete ---")
            reservar = input("¿Desea reservar este paquete? (si/no): ")

            if reservar == "si":
                bandera = True
                while bandera == True:
                    fecha_viaje = input("Ingrese la fecha del viaje (yyyy-mm-dd): ")
                    # splitear la fecha para convertir a enteros
                    viaje_anio, viaje_mes, viaje_dia = map(int, fecha_viaje.split('-'))
                    bandera = validar_fecha(viaje_anio, viaje_mes, viaje_dia, anio_actual, mes_actual, dia_actual)
                
                #poner la fecha en palabras
                fecha_viaje = f"{numero_a_palabras(viaje_dia)} de {nombres_meses[viaje_mes - 1]} de {viaje_anio}"
                clientes = []  # lista para almacenar los datos de los clientes
                
                for i in range(cantidad_personas):
                    print(f"Cliente {i+1}:")
                    nombre = input("Ingrese el nombre del cliente: ")
                    dni = int(input("Ingrese el DNI del cliente: "))
                    cliente = {'nombre': nombre, 'dni': dni}
                    clientes.append(cliente)
                
                # Lista para almacenar los numeros de reserva
                numero_reserva = generar_numero_reserva()
                numeros_reserva.append(numero_reserva)

                
                agregar_reserva(paquetes_buscados[0], clientes, cantidad_personas, fecha_viaje, numero_reserva)

                print("Paquete reservado con exito. Generando factura...")
                generar_factura(paquetes_buscados[0], clientes, cantidad_personas, fecha_viaje, numero_reserva)

                # actualizar disponibilidad del paquete
                paquetes_buscados[0][5] -= cantidad_personas

            else:
                print("No se realizo la reserva.")
            
    elif opcion == 3:
        mostrar_paquetes(paquetes)
        
    elif opcion == 4:
        mostrar_reservas(reservas)

    elif opcion == 5:
        print("Saliendo del sistema...")
        
    else:
        print("Opcion no valida. Por favor, intente nuevamente.")