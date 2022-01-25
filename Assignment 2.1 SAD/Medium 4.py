def palindrome_finder (input_name) :
    name=""
    for i in input_name :
        if i != " " :
            name += i

    temp_name = ""
    for i in range (len(name)-1, -1, -1) :
        temp_name += name[i]
    if temp_name == name :
        print("Palindrome")
    else :
        print("Not a palindrome")
        
name = input()
palindrome_finder(name.lower())