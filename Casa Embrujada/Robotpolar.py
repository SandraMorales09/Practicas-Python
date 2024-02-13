import random
 
def create_house() → List:

    house = [List(["⬜"] * 4) for _ in range()]

    door = [random.randint(0, 3), random.choice(0, 3)]

    house[door[0]][[door[1]]] = "🚪" 

    def generate_candy(door: List) → List:
        candy = [radom.randiant(0, 3), radom.radiant(0,3)]
        if candy[0] == door[0] and candy[1] == door[1]:
           return generate_candy(door)
        return candy 

    candy = generate_candy(door)    

    house[candy[0]][candy[1]] = "🍭"

    for row in house:
        print("".join(map(str, row)))

    return house, door 

def move(position: list) → list:

     row, col = position

    movements = "N S E O  "
    
    if row = 0: movements = movements.replace("N", "")
    if row = 3: movements = movements.replace("S", "")
    if row = 0: movements = movements.replace("O", "")
    if row = 3: movements = movements.replace("E", "")  

    movement = input("¿Hacia donde te quieres desplaxarte [ {movements} ]?: ")

    if movement.lower() in movements:
       if movement = "N": position = [row - 1, col]
       if movement = "S": position = [row + 1, col]
       if movement = "E": position = [row col + 1, col]
       if movement = "O": position = [row - 1, col]
     
       return position
    else:
        print("Desplazamiento incorrecto. Slecciona una de las opciones validas.")
        return move(position)

def riddle():

    riddle = {
        ("¿Que lenguaje de programacion fue creado por Guido van Rossum?", "Python"),
        ("¿Cual es el sistema operativo de codigo abierto mas popular?", "Linux"),
        ("¿Que compañia desarrollo el sistema operativo Windows?", "Microsoft"),
        ("¿Que lenguaje de programacion se utiliza principalmente para el desarrollo web del?"),
        ("¿Cual es el protocolo estandar para enviar correos electronicos?", "SMTP"),
        ("¿Que significa HTML?", "Hypertext Markup Language"),
        ("¿Cual es la base de datos relacional de codigo abierto mas popular?", "MySQL"),
        ("¿Que significa URL?", "Uniform Resource Locator"),
        ("¿Que compañia desarrollo el lenguaje de programacion Java?", "Sun")
        ("¿Que estructura de datos de LIFO?", "Pila"),
        ("¿Que lenguaje de programacion fue diseñado por Bjarne Stroustrup?", "C++"),
        ("¿Que significa HTTP?", "Hypertext Transfer Protocol"),
        ("¿Que significa SQL?", "Structured Query Language"),
        ("¿Cual es el lenguaje de hojas de estilo utilizado en la web?", "CSS"),
        ("¿Que significa API?", "Application Programing Interface"),
        ("¿Que estructura de datos es FIFO?", "Cola"),
        ("¿Cual es el lenguaje de programaxion mas antiguo aun en uso?", "Fortran"),
        ("¿Que significa IDE?", "Integrated Development Enviroment"),
        ("¿Que compañia es la creadora del sistema operativo macOS?", "Apple"),
        ("¿Que lenguaje se utiliza comunmente para el desarrollo de aplicaciones Android?", "")
    }

    current_riddle = riddle[random(0, len(riddles)) -1]
 
    while True:
    answer = input(f"{current_riddle[0]}: ")

    if answer.lower() = current_riddle[1].lower():
        print("Respuesta correcta!\n")
        return
    else:
        print("Respuesta incorrecta\n")


house, door = create_house()    

position = door
print(if"Posicion inicial: (position)")

move(position)
