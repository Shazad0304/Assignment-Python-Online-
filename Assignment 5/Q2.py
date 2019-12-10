def fun(strng):
    small = 0
    cap = 0
    for i in range(0,len(strng),1):
        if strng[i].islower():
            small = small +1
        else:
            cap = cap+1
    print(small,cap)

fun('ShAzad')


