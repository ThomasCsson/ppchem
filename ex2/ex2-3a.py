'''initial c is 50 g/l, we want a concentration of 3 g/l'''

c = 50
dc = 0
while c > 3.2 :
    c = c/2
    dc = dc+1
print(f'The substance was diluted {dc} times to reach a final concentration of {c} g/l.')

print(c//1)

elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine"]

for element in reversed(elements):
    print(element)

