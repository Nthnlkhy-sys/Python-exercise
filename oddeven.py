num = input("Please input number: ")
check = input("Please input check number: ")
num = int(num)
check = int(check)

if num % 4 == 0:
    print (num , " is a multiple of 4")
elif num % 2 == 0:
    print (num, " is even number")
else:
    print (num, "is odd number")

if num % check == 0:
    print (num, "its evenly divided by ", check)
else:
    print (num, "its oddly divided by ", check)