from datetime import datetime

""" 
1. Ingresar una fecha
2. Ingresar una hora
3. Ingresar la placa de carro

- Ingresa la fecha y obtiene el dia, a ese dia se le asigna un numero, 
ese numero se compara con el ultimo numero de la placa para saber que
dias pueden circular

- La hora ingresada debe ser comparada entre las franjas horarias cuando
funciona el pico y placa para saber si puede circular o no

- La respuesta debe ser:
    - El vehículo SI puede circular
    - El vehículo NO puede circular
"""

# Convertimos un string con el formato deseado: día/mes/año y hora:minutos en datetime
fecha = input('Ingresa la fecha (día/mes/año): ')
hora = input('Ingresa la hora (12:00): ')
fecha_ = datetime.strptime(fecha,'%d/%m/%Y')
hora_ = datetime.strptime(hora,'%H:%M')

#Obtengo un número que correspode al día de la semana de acuerdo a la fecha ingresada, lunes-->1, martes -->2, miercoles -->3, etc... gracias a .isoweekday
digitoDeSemana = fecha_.isoweekday()

#transformo la hora ingresada en valores flotantes para poder comparar, obteniendo la hora con .hour y los minutos con.minute
horaIngresada = (hora_.hour)
minIngresados = (hora_.minute)
min_a_horas = float( minIngresados/60)

#Se crea una función para comparar si la hora ingresada está dentro de la franja del Pico y Placa
def horaCalculada(horas,minutos):
    horaTransformada = float(horas + minutos)
    if horaTransformada >= 7 and horaTransformada <= 9.5 or horaTransformada >= 16 and horaTransformada <= 19.5:
        print ("Tu vehículo NO puede circular")
    else:
        print ("Puedes circular pero RECUERDA que hoy tu vehículo tiene 'Pico y Placa'")

#Comparo con la franja de circulación de "Pico y Placa: 7:00 - 9:30 / 16:00 - 19:30"

#Ingresa la placa del auto y toma el ultimo elemento del string
placa = input("Ingrese placa de vehiculo (ej. PBC4567): ")
ultimoDigito = (placa[-1])

#Realiza la comparación entre día de la semana y el último dígito llamando a la función
if digitoDeSemana == 1 and ultimoDigito == "1" or digitoDeSemana ==1 and ultimoDigito == "2" :
    horaCalculada (horaIngresada, min_a_horas)
elif digitoDeSemana == 2 and ultimoDigito == "3" or digitoDeSemana == 2 and ultimoDigito == "4" :
    horaCalculada (horaIngresada, min_a_horas)
elif digitoDeSemana == 3 and ultimoDigito == "5" or digitoDeSemana == 3 and ultimoDigito == "6" :
    horaCalculada (horaIngresada, min_a_horas)
elif digitoDeSemana == 4 and ultimoDigito == "7" or digitoDeSemana == 4 and ultimoDigito == "8" :
    horaCalculada (horaIngresada, min_a_horas)
elif digitoDeSemana == 5 and ultimoDigito == "9" or digitoDeSemana == 5 and ultimoDigito == "0" :
    horaCalculada (horaIngresada, min_a_horas)
else:
    print ("El vehículo SI puede circular el día de hoy")