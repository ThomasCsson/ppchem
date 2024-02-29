el = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine"]
len = len(el)//2
for i in range (0,len):
    a = el [i]
    el[i]=el[-i-1]
    el[-i-1]=a
print(el)
