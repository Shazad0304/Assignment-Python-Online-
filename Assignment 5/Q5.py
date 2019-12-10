def prime(num):
    out = ''
    for i in range(2,int(num),1):
        if (int(num)%i) == 0:
            out='not prime'
            break
        else:
            out='prime'
    print(out)

prime(5)