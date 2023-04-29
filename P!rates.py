cities = {}

while True:
    data = input()
    if data == "Sail":
        break

    data_split = data.split("||")
    city = data_split[0]
    population = int(data_split[1])
    gold = int(data_split[2])

    if city not in cities:
        cities[city] = {"population": population, "gold": gold}
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold

while True:
    line = input()
    if line == "End":
        break

    line_split = line.split("=>")
    command = line_split[0]
    city = line_split[1]

    if command == "Plunder":
        people = int(line_split[2])
        gold = int(line_split[3])

        cities[city]["population"] -= people
        cities[city]["gold"] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")

        if cities[city]["population"] <= 0 or cities[city]["gold"] <= 0:
            del cities[city]
            print(f"{city} has been wiped off the map!")

    else:
        gold = int(line_split[2])

        if gold < 0:
            print(f"Gold added cannot be a negative number!")
            continue
        else:
            cities[city]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")

if not cities:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, values in cities.items():
        print(f"{city} -> Population: {cities[city]['population']} citizens, Gold: {cities[city]['gold']} kg")








