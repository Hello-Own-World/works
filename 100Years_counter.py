#Hello_Own_World 21.09.2019
while True:
    try:
        current_year = int(input("Enter current year:"))
        name = str(input("Enter your name:"))
        age = int(input("Enter your age:"))
        answer = (100-age)+current_year
        print(f"Hello {name}, you will be 100 years old in {answer}\n"+"-"*40 )
    except ValueError:
        print("Wrong input! Try again.")
        continue