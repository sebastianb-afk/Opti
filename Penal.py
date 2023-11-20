from tabulate import tabulate
from time import time_ns
from scipy import optimize

nombre_archivo = "penalizacion_problem_" + str(time_ns())[-4:] + ".txt"

p0 = [0, 0, 0]
e = 0.1
u = 0.1
b = 10

def f(x):
    return -(x[0]*x[1]+x[0]*x[2]+x[1]*x[2]) # funcion objetivo

def h(x):
    restr = [x[0]+x[1]+x[2]-6] # restricciones de igualdad
    result = map(lambda x: x**2,restr)
    return sum(result)

def g(x):
    restr = [0] # restricciones de desigualdad
    result = map(lambda x: max(0,x)**2,restr)
    return sum(result)


def obj(x):
    return f(x) + u*(h(x)+g(x))

i = 0
data = []
col = ["iteracion", "b", "u", "x"]

while True:
    i+=1
    data.append([i, b, u, p0])
    p0 = optimize.minimize(obj, p0,method="Nelder-Mead").x
    if u*(h(p0)+g(p0)) < e:
        break
    else:
        u = b*u

with open(nombre_archivo, "w") as archivo:
    archivo.write(tabulate(data, headers=col))
    archivo.write("\n\nSolucion: "+str(p0))
