def most_frequent(string):
    dd = dict()
    for counter in string:
        if counter in dd:
            dd[counter]+=1
        else:
            dd[counter]=1
    return (dd)

in_=input("Please enter a string: ")
print(most_frequent(in_))
