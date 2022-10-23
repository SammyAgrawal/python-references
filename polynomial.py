degree = (int(input("whats the degree ")))+1
total = 0
poly = []
for i in range(degree):
    coeff= int(input("Enter coefficient for degree "+ str(i) + " "))
    poly.append(coeff)
x= int(input("What are u plugging into function, bakayaro, konayaro "))       
for i in range(degree):
    total += poly[i] * x**i
    
print(total)
