def fac(val):
    if val == 0:
        return 1
    else:
        return val * fac(val-1)

print(fac(5))