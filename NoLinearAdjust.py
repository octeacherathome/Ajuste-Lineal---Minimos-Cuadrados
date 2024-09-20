#Ajuste No lineal para una funcion senoidal
#Programa para realizar un ajsute lineal en python
import numpy as np
import matplotlib.pyplot as plt
import fit_leastsq as f_l #libreria para ajusta los datos

#Funcion para convertir string a float, devueve un lista np
def str2float(lst):
	return np.array([float(i) for i in lst])

#Funcion para contar el numero de datos por columna
#Si encuentra espacio vacio, el programa lo ignora
def size_Num(array):
	n2 = array.size
	n3 = 0
	
	for i in range(0,n2):
	   if array[i] != '':
	      n3 += 1
	return n3

#Se pide el nombre de archivo 
print("Nombre de archivo de los datos con extension: ", end="")
#name = str(input())
name = 'CaidaLibre4.csv'
print("Delimitador de campo: ", end="")
#delimiter = str(input())
delimiter = ','
print("# de linea de inicio de datos: ", end="")
#sLine = int(input())
sLine = 1

fileData = np.loadtxt(name,dtype=float, delimiter=delimiter, skiprows = sLine)

#Linea para desplazar el eje o de los datos
#x_exp = (x_exp - x_exp[0])
n = size_Num(fileData[:,0])
x_exp = str2float(fileData[:n,0])
y_exp = str2float(fileData[:n,1])

x_teo = np.linspace(x_exp[0],x_exp[n-1],n*5)

#Definicion de funcion
"""
#Ajuste de una funcion  tipo seno o coseno
def funF(x, p0,p1,p2, p3):
	return p0*np.sin(2*np.pi*p1*x+p2)+p3
def funFF(x, p):
	return funF(x,*p)
"""

def funF(x, p2,p1,p0):
	return p2*x**2 + p1*x + p0
def funFF(x, p):
	return funF(x,*p)

#Si se utiliza otra funcion se debe modificar la
#lista de parametros
print("Parametros de ajuste iniciales: ")
print("Coeficiente P2: ", end="")
A = float(input())
print("Coeficiente P1: ", end="")
B = float(input())
print("Coeficiente P0: ", end="")
C = float(input())

#Lista inicial de los parametros del ajuste
p_start = [A,B,C]

pfit_ls, perr_ls = f_l.fit_leastsq(p_start, x_exp, y_exp, funFF)
chi_sq = sum((funFF(x_exp, pfit_ls) - y_exp)**2/funFF(x_exp, pfit_ls))
print("\n# Fit parameters and parameter errors from lestsq method :")
print("pfit = ", pfit_ls)
print("perr = ", perr_ls)
print("Chi_2 = ", chi_sq)

#Grafica de la funcion con los parametros de ajuste iniciales y
#con la funcion con los parametros ajustados
plt.figure()
plt.plot(x_exp,y_exp, "bo", label = "Exp.Data")
plt.plot(x_teo,funFF(x_teo, pfit_ls), "r--", label = "No Linear Adj.")
plt.plot(x_teo,funFF(x_teo, p_start), "g--", label = "St. Param.")
plt.xlabel("x_data(Unit)")
plt.ylabel("y_data(Unit)")
plt.title("Title1")
plt.legend()

#Grafica de la funcion con los parametros de ajustados
plt.figure()
plt.plot(x_exp,y_exp, "bo", label = "Exp.Data")
plt.plot(x_teo,funFF(x_teo, pfit_ls), "r--", label = "No Linear Adj.")
plt.xlabel("x_data (Unit)")
plt.ylabel("y_data (Unit)")
plt.title("Title2")
plt.legend()
plt.savefig("noLinearAdjust.png")
plt.show()
##Ajuste lineal##
