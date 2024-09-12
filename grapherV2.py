#Ajuste No lineal para una funcion senoidal
#Programa para series de datos con python
import numpy as np
import matplotlib.pyplot as plt
import random as rand
import time as tm

#Funcion para convertir string a float, devueve un lista np
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

#Line Style for differents graphs
linestyle_tuple = [
     #('loosely dotted',        (0, (1, 10))),
     ('dotted',                (0, (1, 1))),
     ('densely dotted',        (0, (1, 1))),
     ('long dash with offset', (5, (10, 3))),
     ('loosely dashed',        (0, (5, 10))),
     ('dashed',                (0, (5, 5))),
     ('densely dashed',        (0, (5, 1))),

     ('loosely dashdotted',    (0, (3, 10, 1, 10))),
     ('dashdotted',            (0, (3, 5, 1, 5))),
     ('densely dashdotted',    (0, (3, 1, 1, 1))),

     ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
     ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
     ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))]


#Se pide el nombre de archivo 
print("====Programa para graficar un conjunto de datos====")
print("Nombre de archivo de los datos con extension: ", end="")
#name = str(input())
name = "datos_CaidaLibre2.csv"

print("Delimitador de campo para ambos archivos: ", end="")
#delimiter = str(input())
delimiter = ','

print("# de linea de inicio de datos de ambos archivos: ", end="")
#sLine = int(input())
sLine = 1

print("Numero de conjunto de datos a graficar: ", end="")
#numAdjust = int(input())
numAdjust = 5

fileData = np.loadtxt(name,dtype=str, delimiter=delimiter, skiprows = sLine)

labels = ["Etiqueta 1", "Etiqueta 2", "...."]

plt.figure()
j = 0
rand.seed(tm.time())
lineLen = len(linestyle_tuple)# number of line style
for i in range(0,2*numAdjust-1,2):
	n = size_Num(fileData[:,i])
	x_exp = str2float(fileData[:n,i])
	y_exp = str2float(fileData[:n,i+1])
	
	#color for graphs
	r = rand.random()
	g = rand.random()
	b = rand.random()
        #Definir color para las lineas manualmente
	#color = [(r1,g1,b1), (r2,g2,b2), ...]
	
	plt.plot(x_exp,y_exp, linestyle = linestyle_tuple[int(rand.uniform(0,lineLen-1))][1] ,label = "Exp.Data_"+str(int(1+(i/2))), color=(r,g,b))

plt.xlabel("x_data(Unit)")
plt.ylabel("y_data(Unit)")
plt.title("Title1")
plt.legend()
#plt.savefig("grapher_"+str(int(rand.random()*10))+".png")
plt.savefig("grapher_0.png")
plt.show()
