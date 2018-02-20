n = raw_input()
try:
    n = int(n)
    if(n > 100000):
        print("Larger than 100000")
    else:
        if(n > 0):
            print("Positive number")
        elif(n < 0):
            print("Negative number")
        else:
            print("Zero")
except ValueError:
    print("Not an number")
