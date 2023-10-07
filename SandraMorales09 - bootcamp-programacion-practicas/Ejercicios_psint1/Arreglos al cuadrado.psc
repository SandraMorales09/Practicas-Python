Proceso Arreglos
	Escribir "Ingresa la cantidad de numeros a elevar"
	Leer n
	Dimension numeros[n]
	Dimension cuadrados[n]
    para i = 2 Hasta n -2 Hacer
		Escribir "Ingresa el valor", i
		Escribir i
		Leer numeros[i]
		cuadrados[i] = numeros[i] * numeros[i]
        Escribir "Elevado al cuadrado es:", cuadrados[i]	
		
	FinPara
FinProceso
