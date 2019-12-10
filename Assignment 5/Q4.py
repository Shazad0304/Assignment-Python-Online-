def palin(st):
    a=len(st)-1
    b=''
    for i in range(0,len(st),1):
        if st[i] == st[a]:
            b = 'Palindrome'
            a = a-1
        else:
            b='No Palindrome'
            break
    print(b)

palin('dad')