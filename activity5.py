valid = False
while not valid: # using nested while loop
    try:
        n=int(input("please enter an number"))
        # enter a number 
        while n%2==0:

            print("bye")
        valid = True
    except ValueError:
        print("invalid") 
