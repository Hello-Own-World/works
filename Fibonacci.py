lst = [0, 1]
def fibonacci (value = int(input("Enter number of numbers in sequence: "))):
    for i in range(value-2):
        lst.append( lst[len(lst)-1] + lst[len(lst)-2])
fibonacci()
print(lst)

