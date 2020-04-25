degree = (int(input("whats the degree ")))+1
total = 0
x= int(input("What are u plugging into function, bakayaro, konayaro "))
for i in range(degree):
    coeff= int(input("Enter coefficient for degree "+ str(i) + " "))
    total += coeff*(x**i)
print(total)