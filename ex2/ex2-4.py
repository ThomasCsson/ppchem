def test_function(inp_list, tgts):
    found_tgts = []
    for tgt in tgts:
        if tgt in inp_list:
            found_tgts.append(tgt)
    return found_tgts
import random

MAX_SIZE = 10000000 # This is the maximum value of the numbers in the list
MAX_TGT_VALUE = 10000000 # This is the maximum value of the target numbers
LENGTH = 10000000 # This is the length of the list

# Here we declare a list of random numbers and a list of random target numbers
random_integers = [random.randint(0, MAX_SIZE) for i in range(LENGTH)]
target_integers = [random.randint(0, MAX_TGT_VALUE) for i in range(10)]
targets_found = []
comparison_counter = 0


for i in range (0,10):
    for j in range(0,LENGTH):
        comparison_counter = comparison_counter + 1
        if target_integers[i]==random_integers[j]:
            print(f'{target_integers[i]} was found at position {j} in the list')  
            break


print(f'It took {comparison_counter} itterations of code to find them')