element_list = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron"]

a = element_list.pop(-1)
print(a)

b = element_list.pop(1)
print(b)

print(element_list)

element_list.pop(1)

print(element_list)

element_list.clear()
print(element_list)

element_list_1 = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron"]
element_list_2= ["Nitrogen", "Oxygen", "Fluorine"]
element_list_3 = element_list_1 + element_list_2
print(element_list_3)

print(len(element_list_3))
print(element_list_3[0:6:2])