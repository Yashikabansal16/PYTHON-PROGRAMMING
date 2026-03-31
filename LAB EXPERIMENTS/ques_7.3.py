total_area = 0

with open("city.txt") as f:
    for line in f:
        name, pop, area = line.split()
        pop = float(pop)
        area = float(area)

        # (a) display all details
        print(name, pop, area)

        # (b) population > 10 lakhs
        if pop > 10:
            print("High population city:", name)

        # (c) sum of areas
        total_area += area

print("Total area =", total_area)