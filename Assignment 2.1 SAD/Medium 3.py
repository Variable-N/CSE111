vowel = 'aeiou'
def vowel_counter (name) :
    count = 0
    first = True;
    for i in range (len(name)) :
        for j in range (len(vowel)) :
            if name[i] == vowel[j] :
                if not first:
                    print(', ', end="")
                print (vowel[j], end = "")
                count += 1
                first = False
    if count == 0 :
        print('No vowels in the name')
    else :
        print ('. Total number of vowels:',count)

name = input()
vowel_counter(name)