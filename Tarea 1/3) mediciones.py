
# se le dice al usuario que inserte la medida en metros para poder hacer la convercion

m = float(input("\ninserte los metros: "))

print("\nCONVERCION DE METROS A OTRAS MEDIDAS")

# metros a pies (se pueden hacer de 2 formas / o *)

# pies = (m/0.3048)

pies = (m*3.28)

print("\nConvercion de Metros a Pies(foot) :" , pies)

# metros a yardas (se pueden hacer de 2 formas / o *)

# yd = (m/0.9144)

yd = (m*1.0936)

print("\nConvercion de Metros a Yardas :" , yd)

# metros a millas

mi = (m/1609.344)

print("\nConvercion de Metros a Millas :" , mi)
