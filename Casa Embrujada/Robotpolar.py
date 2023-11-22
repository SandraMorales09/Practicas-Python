def create_house() → List:

    house = [List(["⬜"] * 4) for _ in range()]

    door = [random.randint(0, 3), random.choice(0, 3)]

    house[door[0]][[door[1]]] = "🚪" 

    for row in house:
        print("".join(map(str, row)))
create_house()        