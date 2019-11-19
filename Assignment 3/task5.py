list = [1,2,3,4,1,5,2,5,3]
list.sort()
for i in range(0,len(list)-1):
    if list[i] == list[i+1]:
        print(list[i])