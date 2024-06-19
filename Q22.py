list=[1,2,3,4,5]
min=list[0]
max=list[0]
for i in range(1,len(list)):
    if(list[i] < min):
        min=list[i]
    if(list[i] > max):
        max=list[i]
print("The minimum value in list is:",min)
print("The maximum value in list is:",max)
