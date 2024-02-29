pH = 2  # Assume we start the pH at 2 (which is acidic)

while pH != 7:  # while the pH is not neutral
    print(f"Current pH: {pH}")
    if pH < 7:  # if the environment is acidic
        print("Solution is too acidic. Adding a base to increase pH.")
        pH += 1  # add a base to increase the pH
    elif pH > 7:  # if the environment is basic
        print("Solution is too basic. Adding an acid to decrease pH.")
        pH -= 1  # add an acid to reduce the pH
        
print("Solution is now neutral.")

counter = 0
max_count = 9

# Here is the list of the first nine chemical elements:
elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine"]

while counter < max_count:
    # Here we print the element at the current index
    # Note the adjustment for 0-based indexing
    print(f"Element {counter + 1}: {elements[counter]}")
    counter += 1
