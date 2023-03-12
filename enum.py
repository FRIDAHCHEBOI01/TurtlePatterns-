w = range(10)
print(w)
print(type(w))
sum = 0
for i in w:
    sum+=i
    
print("Sum of the numbers within given range is: ", sum)

list_1 = ['fridah','suzanne','madeline','Henry']
#
print(type(enumerate(list_1)))

obj = enumerate(list_1)

print(list(obj))

print(type(list(obj))) 
for elem in enumerate(list_1):
    print(elem)
    
for elem in enumerate(list_1, 100):#
    print(elem)
