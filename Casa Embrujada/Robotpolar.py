def create_house() → List:

    house =[List(["⬜"] * 4) for _ in range()]

    for row in house:
        print("".join(map(str, row)))
create_house()        