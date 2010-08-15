from pympler.asizeof import asizeof
import gc

def get_objects_of_type(t):
    return filter(lambda x: type(x) is t, gc.get_objects())

def get_objects_sizes(l, sizeof=asizeof):
    sum = 0
    nl = []
    for obj in l:
        size = sizeof(obj)
        nl.append((size,obj))
        sum += size
    return (sum, sorted(nl, key=lambda (x,y): x, reverse=True))
