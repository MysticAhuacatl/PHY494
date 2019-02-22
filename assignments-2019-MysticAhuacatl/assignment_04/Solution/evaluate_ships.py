# bonus problem: evaluate_ships.py
#
# run with
#
#    python evaluate_ships.py
#
# Assumes that starships.csv is in the parent directory.

filename = "../starships.csv"
outfilename = "starship_costs.dat"
mincost = 100e6

vehicles = []     # list with (name, cost) entries

with open(filename) as inputfile:
    for line in inputfile:
        line = line.strip()
        if not line:
            continue
        fields = line.split(',')
        name, cost = fields[0], fields[4]
        if cost == "unknown":
            cost = 0
        cost = float(cost)
        if cost <= mincost:
            continue
        vehicles.append((name, cost))

# write output (use scientific notation for large numbers by using the
# {:g} format specifier); as a bonus we also insert the galactic
# currency symbol 'CR' (not needed for full points)
with open(outfilename, 'w') as output:
    for name, cost in vehicles:
        output.write("{0:25s}  CR {1:g}\n".format(name, cost))





