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

def move (position: list) → list:

     row, col = position

    movements = "N S E O  "
    
    if row = 0:
        movements = movements.replace("N", "")
    if row = 3:
        movements = movements.replace("N", "")
    if row = 0:
        movements = movements.replace("N", "")
    if row = 3:
        movements = movements.replace("N", "")  

    movement = input("¿Hacia donde te quieres desplaxarte [ {movements} ]?: ")

    if movement.lower() in movements:
       if movement = "n": position = [row - 1, col]
       if movement = "s": position = [row - 1, col]
       if movement = "e": position = [row - 1, col]
       if movement = "o": position = [row - 1, col]
     
       return position
    else:
        print("Desplazamiento incorrecto. Slecciona una de las opciones validas.")
        return move(position)

house, door = create_house()    

position = door
print(if"Posicion inicial: (position)")

move(position)
