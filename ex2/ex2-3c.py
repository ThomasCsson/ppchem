'''Q3c'''
numa = 11
while numa > 2.5:
    numa = numa - 1
    print(numa)
print('')

'''Q3d'''
numb = 2.5
for i in range(0, 10, 2):
    pass
    print(i/numb)
print('')

'''Q3e'''
numc = 10.2 
while True:
    if numc < 6.2:
        break
    print(numc)
    numc = (numc-1)
print('')

'''Q3f'''
collected_strings = []

for i in range(1, 5):
    if i % 2 == 0:  
        for j in range(5):
            if j == 3:
                break
                collected_strings.append(str(j))
        collected_strings.append(str('F'))
    else:  
        for j in range(5):
            if j == 3:
                continue
            elif j == 4:
                pass
            collected_strings.append(str(j))

for i in range(3):
    if i == 1:
        collected_strings.append("!")
        continue
    collected_strings.append("?")

collect_str = "".join(collected_strings)
print(f'Collected string is {collect_str}')

print('')

'''Q3g'''
n = 10 
i = 10
while i > 0:

    if i % 2 == 0:
        i=i/2
    else: 
        i=i-1