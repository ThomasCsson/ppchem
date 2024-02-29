elements = ["Iron", "Copper", "Zinc", "Gold", "Silver", "Platinum"]

for element in elements:
    if element == "Copper":
        continue
    if element == "Gold":
        break
    print(element)
