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


'''Q2.d'''
el = element_list_3
print(el)
print(el[-3:])
print(el[:5:2])
'''two ways of doing this'''
print(el[::2])
print(el[0:8:2])


test1 = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Sodium"]
mid = len(test1)//2
print(mid)
fhalf = test1[:mid]
print(fhalf)
shalf=test1[mid:]
print(shalf)
test2 = test1[:len(test1)-1]
print(test2)
mid2 = len(test2)//2+1
print(mid2)
ffhalf = test2[:mid2]
sshalf = test2[mid2:]
print(ffhalf)
print(sshalf)


'''Dictionaries'''

acid_bases = {'NaBH4' : 'Base', 'H2SO4' : 'Acid', 'NaOH' : 'Base'}
print(acid_bases['NaBH4'])
acid_bases['HCl'] = 'Acid'
print(acid_bases)
del acid_bases['HCl']
print(acid_bases)

'''Loops'''

