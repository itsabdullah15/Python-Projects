def getdate():
    import datetime
    return datetime.datetime.now()

import datetime
def gettime():
    return datetime.datetime.now()



def take(z): # Take input from user
    if z==1:
        c = int(input("Enter 1 for Exercise and 2 for Food "))
        if(c == 1)
        value=input("Type Here\n ")
        with open("Abdullah-kasrat.txt","a") as op:
            op.write(str([str(gettime())])+": " +value+ "\n")
        print("Successfully written ")    
        if(c == 2)
        value=input("Type Here\n ")
        with open("Abdullah-Khana.txt","a") as op:
            op.write(str([str(gettime())])+": " +value+ "\n")
        print("Successfully written ")
    if z==2:
        c = int(input("Enter 1 for Exercise and 2 for Food "))
        if(c == 1)
        value=input("Type Here\n ")
        with open("Rohan-kasrat.txt","a") as op:
            op.write(str([str(gettime())])+": " +value+ "\n")
        print("Successfully written ")    
        if(c == 2)
        value=input("Type Here\n ")
        with open("Rohan-Khana.txt","a") as op:
            op.write(str([str(gettime())])+": " +value+ "\n")
        print("Successfully written ")
    if z==3:
        c = int(input("Enter 1 for Exercise and 2 for Food "))
        if(c == 1)
        value=input("Type Here\n ")
        with open("Hammad-kasrat.txt","a") as op:
            op.write(str([str(gettime())])+": " +value+ "\n")
        print("Successfully written ")    
        if(c == 2)
        value=input("Type Here\n ")
        with open("Hammad-Khana.txt","a") as op:
            op.write(str([str(gettime())])+": " +value+ "\n")
        print("Successfully written ")
    else:
        print("Please Enter valid input [1 for Abdullah, 2 for Rohan or 3 for Hammad ]")

def retrieve(z): # show output
    if z==1:
        c = int(input("Enter 1 for Exesise and 2 for Food "))
        if(c==1):
            with open("Abdullah-exersise.txt") as op:
                for i in op:
                    print(i,end="")
    elif(c==2):
        with open("Abdullah-Food.txt") as op:
            for i in op:
                print(i, end="")
    elif(z==2):
        c = int(input("Enter 1 for exersise and 2 for Food "))
        if(c==1):
            with open("Rohan-exersise.txt") as op:
                for i in op:
                    print(i, end="")
        elif(c==2):
            with open("Rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(z==3):
        c = int(input("Enetr 1 for Exercise and 2 for Food "))
        if(c==1):
            with open("Hammad-exersise.txt") as op:
                for i in op:
                    print(i, end="")
        elif(c==2):
            with open("Hammad-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Please Enter valid input (Abdullah, Rohan , Hammad)")


print("     Health Management System        ")
a = int(input("Press 1 for log the value and 2 for retrive "))

if a == 1:
    b =  int(input("Press 1 for Abdullah 2 for Rohan 3 for Hammad "))
    take(b)
else:
    b = int(input("Press 1 for Abdullah 2 for Rohan 3 for Hammad "))
    retrieve(b)