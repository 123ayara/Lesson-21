lower=int(input("Enter the lower range of the square values:"))
upper=int(input("Enter the upper range of the square values:"))
square=[]
elements=0
for i in range(lower,upper+1):
    elements=i*i
    square.append(elements)
print(square)