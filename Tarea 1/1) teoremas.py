
from cmath import exp, sqrt


co = float(input("Digite el cateto opuesto: "))
cd = float(input("Digite el cateto adyasente: "))

formula = ((co * co) + (cd * cd)) 

# la raiz se puede sacar de varias maneras pero podria usar dos
 
# raiz = (formula ** 0.5)

#raiz = sqrt(formula)

raiz = (formula ** 0.5)

print(f"la hipotenusa del triangulo con cateto opuesto {co}cm y cateto adyasente {cd}cm es de {raiz}cm")
