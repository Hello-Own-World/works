#Hello_Own_World 29.09.19
while True:
    try:
        num = int(input("Enter your number:"))
        divide_num = int(input("Enter number to divide :"))
    except ValueError:
        print("Wrong input !")
        continue
    result = num % divide_num
    if result == 0 :
        print("Number is multiple")
    else:
        print("Number isn`t multiple")