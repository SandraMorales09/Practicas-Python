Proceso Calculadora_Trucharte
	Repetir
		Limpiar Pantalla;
		
		//MOSTRAR EL MENU DE OPCIONES
		Escribir "MENU DE PROGRAMA"
		Escribir "  1. Suma";
		Escribir "  2. Resta";
		Escribir "  3. Multiplicacion";
		Escribir "  4. Division";
		Escribir "  5. Perimetro circulo";
		Escribir "  6. Area del circulo";
		Escribir "  7. Perimetro del triangulo";
		Escribir "  8. Area del triangulo";
		Escribir " 9. Salir";
		
		Escribir "Elige una opcion: ";
		
		Definir opcion como Entero;
		Leer opcion;
		
		//SI LA OPCION ELEGIDA FUE 1,2,3 o 4 ENTONCES SE PIDEN LOS NUMEROS QUE SE VAN OPERAR
		Si opcion>0 Y opcion<5 Entonces
			Escribir "Ingresa un numero valor:";

			
		Fin Si
		
		
		//IMPLEMENTAR EL MENU DE PROGRAMA
		Segun opcion Hacer
			1://SUMA 
				secuencia_de_acciones_1
			2://RESTA
				secuencia_de_acciones_2
			3://MULTIPLICACION
				secuencia_de_acciones_3
			4://DIVISION
			5:
			6:
			7:
		    8:
			9:
				
			De Otro Modo:
				Escribir "OPCION NO VALIDA";
		Fin Segun
		
	