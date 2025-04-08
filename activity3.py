list=[3, 7, 12, 8, 10]
print("Original list:",list)
count=0
for i in list:
    count+=i
print("Sum=",count)
avg=count/len(list)
print("Average=",avg)
list.sort()
print(list)
print("Largest element is:",list[4])