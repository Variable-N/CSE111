string = input()
if len(string) <4 :
    print(string)
elif string[-3].lower() == 'f' and string[-2].lower() == 'u' and string[-1].lower() == 'l' :
    print(string , "ly" , sep="")
else :
    print(string , "ful" , sep = "")