def new_letter (letter) :
    ascii_input = ord(letter)
    if ascii_input > 91 :
        ascii_input -=32
        return chr(ascii_input)
    else :
        return letter 

def auto_correct (text) :
    firstletter = True
    new_text = ""
    i = 0
    while i < len(text)-2 :
        if text[i] == ' ' :
            new_text += text[i]
        else :
            if firstletter :
                new_text += new_letter(text[i]) 
                firstletter = False
            elif text[i] == '.' or text[i] == '?' or text [i] == '!' :
                if text[i+1] ==" ":
                    new_text += text[i] + text[i+1] + new_letter(text[i+2])
                    i+=2
                else :
                    new_text += text[i] + new_letter(text[i+1])
                    i +=1
            elif text[i] == 'i' and text[i-1]== " " and text[i+1] == " " :
                new_text += 'I'
            else :
                new_text += text[i]
        i += 1
    new_text += text[-2] + text[-1]
    print (new_text)

text = input ()
auto_correct(text)







'''
my favourite animal is a dog. a dog has i sharp teeth so that it can eat flesh very easily. do you know my pet dog’s name? i love my pet very much.

'''