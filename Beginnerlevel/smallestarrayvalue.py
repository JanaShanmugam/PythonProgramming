num_array = list()
t=0
num =int(input("Enter no of elements :"))
print ('Enter numbers : ')
for i in range(int(num)):
    n = int(input("num :"))
    num_array.append(int(n))
print ('ARRAY: ', num_array)
num_array.sort()
print(num_array)  
print(num_array[0])  
