while 1 :
    text = input("Enter word : ").lower()
    text2 = text[::-1]
    if text2 == text :
        print("This word is palindrome")
    elif text == "exit":
        break
    else :
        print("This word isn`t palindrome" )
    print(text2)
    print("For exit , type 'exit' ")
