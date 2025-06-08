l = [4,5,1,2,9,7,10,8]

count =0

for i in l:
    count += i

avg = count/len(l)

print("Sum = ", count)
print("Average = ", avg)

l.sort()

print("Smallest element in list is ", l[0])
print("Largest element in list is ", l[-1])

