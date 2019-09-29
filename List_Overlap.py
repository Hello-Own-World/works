import random
lst1 = [random.randint(0,100) for i in range (100)]
lst2 = [random.randint(0,100) for i in range (100)]
print(lst1)
print(lst2)
print(set(el for el in lst1 if el in lst2))