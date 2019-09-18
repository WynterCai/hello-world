# n = input("Input a number: ")
# sum = 0
# for i in range(1,n+1):
#    sum = sum+i*i
# print("The result is:",sum)

data = ["Born on:", "July", 2, 2005]
for d in data:
    print(d)

data = ["Born on:", "July", 2, 2005]
for i in range(len(data)):
    print(data[i])

data = ["Born on:", "July", 2, 2005]
for i in range(0, len(data), 3):
    print(data[i])

data = [1, 2, 3, 4, 5]
for i in range(len(data)):
    data[i] = data[i] + 1
print(data)
print(i)

for c in "Hello World":
    print(c)

for i in (1, 2, 3):
    print(i)

# while True:
#    x = eval(input("Please input a positive number: "))
#    if x >0: break

# while True:
#    x = int(input("Please input a positive number: "))
#    if x <= 0:
#        break

for i in range(10):
    print("烦")
    if i > 4: break

#a = [23, 28, 39, 44, 50, 67, 99]
#sum = 0
#for i in a:
#    if a % 2 == 0: continue
#    sum = sum + i
# print(sum)
a = [1,2,3,4,5]
sum = 0
for i in a:
    sum = sum+i
print(sum)

a = [[11,12,13,14],[21,22,23,24],[31,32,33,34]]
sum = 0
for i in a:
    for j in i:
        sum = sum+j

print(sum)