from naan_functions import *
# Tests TDD
#As a user I can pass 'wheat' and 'water' to the function make_dough, so that I can make 'dough'.
print('Testing make_dough, with wheat and water --> dough to come out')
print(make_dough('wheat', 'water') == 'dough') # Evaluation that results in a bool (True or False)

print('Testing make_dough, with sand and cement --> not dough')
print(make_dough('cement', 'sand') == 'not dough')

#As a user I can pass 'dough' to the function wood_oven, so that I can make 'Naan bread'
print('Testing wood_oven, with dough --> naan bread to come out')
print(wood_oven('dough') == 'naan bread')