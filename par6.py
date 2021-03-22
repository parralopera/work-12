# Escuela de Natacion
solicitud=input("Desea presentarse a un curso de Natacion (si/no): ")
edad=input("Igrese su Edad: ")
basico=120000
experto=250000
profecional=280000

while(solicitud=="si"):
	nivel=input("Por Favor nivel de intencidad(basico-exp-pro): ")

	if(nivel=="basico"):
		basico=basico
	elif(nivel=="exp"):
		experto=experto
	elif(nivel=="pro"):
		profecional=profecional
	else:
		print("Procesando Informacion...")

tiquete=input("Imprimir Tiquete... (si/no): ")
if("si"):
        print("Tiquete: ",edad+nivel)