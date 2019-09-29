while True :
    try:
        num = int(input("Enter number:"))
    except ValueError:
        continue
    print([i for i in range(1,num+1) if num % i == 0 ])
