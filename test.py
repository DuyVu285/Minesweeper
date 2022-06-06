list = [2]
list2 = [1,2,3,"A"]
list.append(list2)
print(list)
for x in list:
    if(not isinstance(x,int)):
        for y in x:
            print(y)
 
print(len(list[-1]))