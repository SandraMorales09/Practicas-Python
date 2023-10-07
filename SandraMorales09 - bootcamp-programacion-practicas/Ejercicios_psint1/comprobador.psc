//Comprobador de mayoria de edad
//Comprobador que una persona sea mayor de  18 años 
// Comprobar que la persona no tenga mas de 130 años
// Comprobar que la persona exista, es decir, que tenga mas de  0 años

Proceso comprobador
	     Escribir "Ingresa tu edad"
	     Leer edad
	     Si edad >= 18 y edad <= 130
		         Entonces
		                  Escribir "Pasale al manitas"
		         SiNo
			              Si edad < 0 o edad >130
								  Entonces
							               Escribir "No deberia existir"
					              Sino
						                   Si edad < 18 Entonces 
							                       Escribir  "las muuuuy chikitho"
						                   FinSi
				          FinSi		
         FinSi
FinProceso
