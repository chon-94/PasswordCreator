import string
import random

# caracteres a partir de los cuales se generará una contraseña
caracteres = list(string.ascii_letters + string.digits + "!@#$%^&*()-_=?+")

def generadorAleatorioCLaves():
	# longitud de la contraseña
	cc = int(input("Introduzca la cantidad de caracteres: "))

	## mesclar los caracteres
	random.shuffle(caracteres)
	
	# elegir caracteres aleatorios de la lista
	clave = []
	for i in range(cc):
		clave.append(random.choice(caracteres))

	# mesclar la contraseña resultante
	random.shuffle(clave)

	# Convertir la lista en cadena
	# printing the list
	print("".join(clave))

# invocar la función
generadorAleatorioCLaves()