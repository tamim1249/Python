Marks=int(input("Enter your marks: "))
if Marks>79 and Marks<101:
    print("The Grade is A+")
elif Marks>74 and Marks<80:
    print("The Grade is A")
elif Marks>69 and Marks<75:
    print("The Grade is A-")
elif Marks>64 and Marks<70:
    print("The Grade is B+")
elif Marks>59 and Marks<65:
    print("The Grade is B")
elif Marks>=55 and Marks<=59:
    print("The Grade is B-")
elif Marks>=50 and Marks<=54:
    print("The Grade is C+")
elif Marks>=45 and Marks<=49:
    print("The Grade is C")
elif Marks>=40 and Marks<=44:
    print("The Grade is D")
elif Marks>=0 and Marks<=39:
    print("You are Faill")
else:
    print("Wrong input")
        
