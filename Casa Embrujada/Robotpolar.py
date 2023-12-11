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

house, door = create_house()    

position = door
print(if"Posicion inicial")
