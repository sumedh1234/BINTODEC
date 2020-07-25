import math
def enter():
    global b
    b = int(input("Enter any binary number\n"))                        #take the input from the user
    global l
    l = len(str(b))                                                    #calculate the length of string

    a = [int(i) for i in str(b)]                                       #to split the number into list

    #print(a)
    global v
    v = a[::-1]                                                        #to print list in reverse order

    #v = []                                                            #to create blank list
    #for i in reversed(a):
       # v.append(i)                                                   #to print list in reverse order

    #print(v)

    #print(l)

def repeat():                                                          #this function is for repeated working of this programme till the user enters 'n'
    n = input("Do you want to continue dear..[y/n]\n")
    if n == "y":
        enter()
        calculate()
        repeat()
    else:
        print("\nThank you so much for using me dear..!")
        exit()    

def calculate():
    s = 0
    f = 0
    for i in range(0, l):                                              #this loop checks if the entered number is binary or not
        if v[i] != 0 and v[i] != 1:                                    #if number is not binary then it will go out of the loop 
            f = 1
            break
        else:
            s = s + ( math.pow(2,( i ) )* v[i] )                       #if it is binary then it will perform the calculation

    if f == 1:
        print("\nI am Sorry honey..!\nYou entered {} and this is not a Binary number \nSo please Enter correct binary number\n".format(b))
        repeat()
    else:
        print("\nThe decimal number for {} is {}.\n".format(b, int(s)))

enter()
calculate()
repeat()


# input("Press Enter to exit...")


