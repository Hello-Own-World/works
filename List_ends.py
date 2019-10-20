import random
lst = [random.randint(0,50) for x in range (10)]
print(lst)
def lst_ends ():
    return [lst[0],lst[len(lst)-1]]
print(lst_ends())
