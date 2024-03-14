import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

def obtener_funcion():
    fn = input("Ingrese su funcion\n")
    return lambda x: eval(fn)

def obtener_puntos():
    a = float(input("Punto inicial\n"))
    b = float(input("Punto final\n"))
    return a, b

def obtener_punto():
    x = float(input("Ingrese un punto para calcular la pendiente\n"))
    return x

def obtener_error_maximo():
    es = float(input("Error maximo\n"))
    return es

def obtener_error_maximo_fp():
    es1 = float(input("Error maximo2\n"))
    return es1

def bisec(f, a, b, es):
    xl = a
    xu = b
    pm = (xl + xu) / 2
    xrv = []
    ea = 2 * es
    eav = []
    count = 0
    countV = []
    xlV = []
    xuV = []
    bisec_table = []

    fxl = f(xl)
    fxu = f(xu)
    fpm = f(pm)
    xlV.append(fxl)
    xuV.append(fxu)

    bisec_table.append(["I", "a", "f(a)", "pm", "f(pm)", "b", "f(b)", "Error"])

    while ea >= es:
        xrv.append(pm)
        count += 1
        countV.append(count)
        if fxl * fpm < 0:
            xu = pm
        elif fxl * fpm > 0:
            xl = pm
        else:
            ea = 0
        xrOld = pm
        pm = (xl + xu) / 2

        if pm != 0:
            ea = abs((pm - xrOld)/pm)*100
            eav.append(ea)

        fxl = f(xl)
        fxu = f(xu)
        fpm = f(pm)
        xlV.append(fxl)
        xuV.append(fxu)
        bisec_table.append([count, xl, fxl, pm, fpm, xu, fxu, ea])
        
    print("\nMétodo de la Bisección:")
    print(tabulate(bisec_table, headers="firstrow", tablefmt="fancy_grid"))# Metodo de falsa posicion
    
def falsa_posicion(f, a, b, es1):
    xl1 = a
    xu1 = b
    xr = xu1 - (f(xu1) * (xl1 - xu1)) / (f(xl1) - f(xu1))
    xrv = []
    ea = 2 * es1
    eav = []
    count = 0
    countV = []
    xl1V = []
    xu1V = []
    falp_table = []
    
    fxl1 = f(xl1)
    fxu1 = f(xu1)
    fxr = f(xr)
    xl1V.append(fxl1)
    xu1V.append(fxu1)
        
    falp_table.append(["I", "xl", "f(xl)", "xu", "f(xu)", "xr", "f(xr)", "error"])
    
    while ea >= es1:
        xrv.append(xu1)
        count += 1
        countV.append(count)
        if fxl1 * fxr > 0:
            xl1 = xr
        elif fxl1 * fxr < 0:
            xu1 = xr
        else:
            ea = 0
        xrOld = xrv[-1]
        xr = xu1 - (f(xu1) * (xl1 - xu1)) / (f(xl1) - f(xu1))

        if xr != 0:
            ea = abs((xu1 - xrOld) / xu1) * 100
            eav.append(ea)

        fxl1 = f(xl1)
        fxu1 = f(xu1)
        fxr = f(xr)
        xl1V.append(fxl1)
        xu1V.append(fxu1)
        falp_table.append([count, xl1, fxl1, xu1, fxu1, xr, fxr, ea])
        
    print("\nMétodo de la Falsa Posición:")
    print(tabulate(falp_table, headers="firstrow", tablefmt="fancy_grid"))

    
    # Imprimir los puntos de la función utilizados para graficar
    puntos_funcion = []
    for point in np.linspace(a, b, 100):
        puntos_funcion.append([point, f(point)])
    print("\n")
    print("Puntos de la función utilizados para graficar:")
    print(tabulate(puntos_funcion, headers=["x", "f(x)"], tablefmt="fancy_grid"))
    
    # Graficar los puntos iniciales y finales de la función
    plt.scatter([a], [f(a)], color='g', label='Punto inicial (a)')
    plt.scatter([b], [f(b)], color='m', label='Punto final (b)')
    plt.plot(np.linspace(a, b, 100), f(np.linspace(a, b, 100)), label='Función')
    plt.axhline(0, color='r')
    plt.title("Gráfica Método de Bisección")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

def pendiente(f, x, es):
    h = 0.01  # Tamaño del paso
    xr = x
    eav = []
    count = 0
    countV = []
    xrV = []
    pendiente_table = []

    while True:
        xr_old = xr
        xr = xr - (f(xr) / ((f(xr + h) - f(xr)) / h))  # Método de la pendiente
        count += 1
        countV.append(count)
        e = abs((xr - xr_old) / xr) * 100
        eav.append(e)
        xrV.append(xr)
        pendiente_table.append([count, xr, e])
        if e < es:
            break
    
    print("\nMétodo de la Pendiente:")
    print(tabulate(pendiente_table, headers=["Iteración", "xr", "Error"], tablefmt="fancy_grid"))
    
    # Graficar la función y la tangente en el punto xr
    x_vals = np.linspace(x - 2, x + 2, 100)
    y_vals = f(x_vals)
    tangente = f(xr) + (x_vals - xr) * (f(xr + h) - f(xr)) / h
    plt.plot(x_vals, y_vals, label='Función')
    plt.plot(x_vals, tangente, label='Tangente en xr', linestyle='--')
    plt.scatter([xr], [f(xr)], color='r', label='Punto xr')
    plt.title("Gráfica Método de la Pendiente")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

f = obtener_funcion()
a, b = obtener_puntos()
x = obtener_punto()
emax = obtener_error_maximo()
emaxi = obtener_error_maximo_fp()

bisec(f, a, b, emax)
pendiente(f, x, emax)
falsa_posicion(f, a, b, emaxi)
