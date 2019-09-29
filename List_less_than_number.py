import random
list = [random.randint(0,100)for i in range (20)]
num = int(input("Enter number:"))
print(list)
print([el for el in list if el <= num])

