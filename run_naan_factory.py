# Functions

def make_dough(arg1, arg2):
    #return ('dough', 'not dough')
    #given water and wheat return dough
    #not given water and wheat return not dough
    if (arg1 == 'wheat' and arg2 == 'water'):
        return  'dough'
    else:
        return 'not dough'


def wood_oven(ingredient):
    if ingredient == 'dough':
        return  'naan bread'
    else:
        return 'not naan bread'
    # if the argument is 'dough'
    # return naan bread
    #else
    #return 'not bread'
    #pass

def run_naan_factory(arg1, arg2):
    dough_r = (arg1, arg2)
    result_bread = wood_oven(dough_r)
    return result_bread
#Calling of functions
print(run_naan_factory('wheat', 'water'))

# Tests TDD
#As a user I can pass 'wheat' and 'water' to the function make_dough, so that I can make 'dough'.
print('Testing make_dough, with wheat and water --> dough to come out')
print(make_dough('wheat', 'water') == 'dough') # Evaluation that results in a bool (True or False)

print('Testing make_dough, with sand and cement --> not dough')
print(make_dough('cement', 'sand') == 'not dough')

#As a user I can pass 'dough' to the function wood_oven, so that I can make 'Naan bread'
print('Testing wood_oven, with dough --> naan bread to come out')
print(wood_oven('dough') == 'naan bread')

#One more test for the oven - working and on github
print('Testing wood_oven, if it works --> naan bread hot and fresh')
print(wood_oven('naan bread') == 'hot')