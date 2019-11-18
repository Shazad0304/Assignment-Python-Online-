one = int(input("Please enter the marks of first Subject: "))
two = int(input("Please enter the marks of Second Subject: "))
three = int(input("Please enter the marks of Third Subject: "))
four = int(input("Please enter the marks of Fourth Subject: "))
five= int(input("Please enter the marks of Fifth Subject: "))

percen = ((one+two+three+four+five)/500)*100
if percen >= 80:
    print("A")
elif percen >= 70:
    print("B")
elif percen >= 60:
    print("C")
else:
    print("F")