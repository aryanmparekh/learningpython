m = int(input("Enter Math Score "))
p = int(input("Enter Physics Score "))
c = int(input("Enter Chemistry Score "))
average = int((m+p+c)/3)
if m>=35 and c>=35 and p>=35:
    print("Student has passed. The average of the scores are", average)
else:
    print("Student has failed")
    
if average <= 59:
        print("Student has received a C")
elif average <= 79:
        print("Student has received a B")
else:
        print("Student has received an A")
        