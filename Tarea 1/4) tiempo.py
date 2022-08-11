
# Convertir horas y minutos a segundos totales

# pedimos la hora

print("\nporfavor inserte el tiempo en hh/mm")

hora = int(input("Inserte la hora :" ))

# Convercion de horas a segundos 

h = ((hora * 60) * 60)

# Pedimos los minutos

minuto = int(input("Inserte los minutos :" ))

# Convercion de minutos a segundos

m = (minuto * 60)

# suma de los dos resultados anteriores

s = (m + h)

#resultado

print(f"los segundos totales de la hora {hora}:{minuto}  es : {s} segundos")
