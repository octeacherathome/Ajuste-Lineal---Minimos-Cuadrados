#Programa para realizar un ajsute lineal en python
import numpy as np
import matplotlib.pyplot as plt
import linearAdjust as la
import random as rand
import time as tm

def str2float(lst):
	return np.array([float(i) for i in lst])

#Funcion para contar el numero de datos por columna
#Si encuentra espacio vaio, el programa lo ignora
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
name = "CaidaLibre2.csv"
print("Delimitador de campo: ", end="")
#delimiter = str(input())
delimiter = ","
print("# de linea de inicio de datos: ", end="")
#sLine = int(input())
sLine = 1
print("# de ajustes lineales a realizar: ", end="")
#numAjus = int(input())
numAjus = 2

fileData = np.loadtxt(name,dtype=str, delimiter=delimiter, skiprows = sLine, encoding=None)

plt.figure()
rand.seed(tm.time())
for i in range(0,2*numAjus-1,2):
        n = size_Num(fileData[:,i])
        x_exp = str2float(fileData[:n,i])
        y_exp = str2float(fileData[:n,i+1])
	

	##########Ajuste Lineal de los datos##########
        (pend, inter, Dm, Db, r, Dy) = la.linAdj(x_exp,y_exp,n)
	##########Ajuste Lineal de los datos##########

        print("##########Ajuste Lineal de los datos##########")
        print("Asjute lineal #: ", i)
        print("pendiente: ", pend)
        print("intercepto: ", inter)
        print("maximo error en Dy: ", Dy)
        print("error en Pendiente: ",Dm)
        print("error en intercepto: ",Db)
        print("Coeficiente de Correlacion Lineal (R^2): ",r)
        print("##############################################")

        x_teo = np.linspace(x_exp[0], x_exp[n-1], n*100)
        y_teo = pend*x_teo + inter

	#print("Datos en x: %f", x_exp)
	#print("Datos en y: %f", y_exp)
        r = rand.random()
        b = rand.random()
        g = rand.random()
        color = (r, g, b)

        plt.plot(x_exp,y_exp,"o", label="Exp. Data - " + str(i/2+1),color = color)
        plt.plot(x_teo,y_teo,"--", label="Linear Adjust - "+str(i/2 + 1), color = color)
	
plt.xlabel("Longitud, L(m)")
plt.ylabel("Periodo, T**2(s**2)")
plt.title("Linear Adjust")
plt.legend()
plt.savefig("linearAdjust.png")
plt.show()

#Se leen los datos en el archivo de texto
