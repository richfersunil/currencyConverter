currency=["INR","US dollar","Canadian dollar","Chinese yuan","Russian rubel"]
fcurrency=["US dollar","Canadian dollar","Chinese yuan","Russian rubel"]


# type "back" in "Amount: " section to go back
# type "end" in "Which currency you want to convert: " section to stop

print(currency)
c1= input("Which currency you want to convert: ") # c1 = first currency
c1= c1.lower()
while c1!="end":
    if c1== "inr":
        r1 = input("Amount: ").lower()   # r1= amount
        while r1!= "back":
            print("Choose among these\n", fcurrency)
            c2 = input("in which currency you want to convert: ") # c2 = second currency
            c2= c2.lower()
            if c2 == "back":
                r1 = input("Amount: ").lower()
            if c2 == "us dollar":
                print(r1, "INR =", float(r1) * 0.012, "US dollar")


            if c2 == "canadian dollar":
                print(r1, "INR =", float(r1) * 0.016, "Canadian dollar")


            if c2 == "chinese yuan":
                print(r1, "INR =", float(r1) * 0.088, "Chinese yuan")


            if c2 == "russian rubel":
                print(r1, "INR =", float(r1) * 0.75, "Russian rubel")
            r1 = input("Amount: ").lower()

        c1 = input("Which currency you want to convert: ")
        c1= c1.lower()
    elif c1== "us dollar":
        r1= input("Amount: ").lower()
        while r1 != "back":
            print(r1, "US dollar =", float(r1) * 82.29, "INR")
            r1 = input("Amount: ").lower()
        c1 = input("Which currency you want to convert: ")
        c1=c1.lower()

    elif c1== "canadian dollar":
        r1= input("Amount: ").lower()
        while r1 != "back":
            print(r1, "Canadian dollar =", float(r1) * 60.29, "INR")
            r1 = input("Amount: ").lower()
        c1 = input("Which currency you want to convert: ")
        c1=c1.lower()

    elif c1== "chinese yuan":
        r1= input("Amount: ").lower()
        while r1 != "back":
            print(r1, "Chinese yuan =", float(r1) * 11.35, "INR")
            r1 = input("Amount: ").lower()
        c1 = input("Which currency you want to convert: ")
        c1= c1.lower()

    elif c1== "russian rubel":
        r1= input("Amount: ").lower()
        while r1 != "back":
            print(r1, "Russian rubel =", float(r1) * 1.34, "INR")
            r1 = input("Amount: ").lower()
        c1 = input("Which currency you want to convert: ")
        c1 = c1.lower()

    else:
        print(c1,"not in  the list")
        c1 = input("Which currency you want to convert: ")
