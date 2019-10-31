import random

small_lett = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n','m']
big_lett = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B','N', 'M']
numb = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symb = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '[', ']', '{', '}', ';', ':' , '|', '/', '.', ',', '<', '>', '?']
lst2 = []
password = []

parametrs_pass = input("What use to create password, type number ( 1)small_letters, 2)big_letters, 3)numbers, 4)symbols, 5)all ) :")
parametrs_pass.split()

if "1" in parametrs_pass :
    lst2.extend(small_lett)
if "2" in parametrs_pass :
    lst2.extend(big_lett)
if "3" in parametrs_pass :
    lst2.extend(numb)
if "4" in parametrs_pass :
    lst2.extend(symb)
if "5" in parametrs_pass :
    lst2 = small_lett + big_lett + numb + symb

pass_lenth = int(input("Enter pass lenth:"))
for x in range (pass_lenth):
    password.append(lst2[random.randint(0,len(lst2)-1)])
password = "".join(password)
print(password)

# Simple version (update later)cfh