email=input("Enter your Email:-")
k,j,d=0,0,0

if len(email)>=6:
    if email[0].isalpha():
        if("@" in email) and (email.count("@")==1):
            print(email[-4])
            print(email[-5])
            if(email[-5]==".") or (email[-4]=="."):
                # print(email[-4])
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue 
                    elif i=="_" or i=="." or i=="@":
                        continue 
                    else:
                        d=1

                if k==1 or j==1 :
                    print("Wrong Email 5") 
                else:
                    print("Right Email")
            else:
                print("Wrong Email 4")

        else:
            print("Wrong Email 3")


    else:
        print("Wrong Email 2")

else:
    print("Wrong Email 1")