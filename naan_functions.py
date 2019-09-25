
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