'''
Project started on 16/05/22

'''
pswd=str(input("Enter a password: "))
print("your password is: ", pswd)

length = len(pswd)
A= []

for i in range(length):
    if ((pswd[i]>='0') and (pswd[i]<='9')):
        print("The character at position ", i, "is: ", pswd[i], " it is an integer")
        A.append(pswd[i])
    elif ((pswd[i]>='A') and (pswd[i]<='Z')):
        print("The character at position ", i, "is: ", pswd[i], " it is an uppercase string")
        A.append(pswd[i])
    elif ((pswd[i]>='a') and (pswd[i]<='z')):
        print("The character at position ", i, "is: ", pswd[i], " it is a lowercase string")
        A.append(pswd[i])
    else:
        print("The character at position ", i, "is: ", pswd[i], " it is a symbol")
        A.append(pswd[i])

print(A)