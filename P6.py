# 20CE027 Vatsal Doshi

a = int(input())          # Test Cases
arr = []
for i in range(a):
    b = input()           # N words
    arr.append(b)

set1 = set(arr)

print(len(set1))

arr2 = []
arr3 = []

for i in arr:
    if i in arr2:
        pass
    else:
        arr2.append(i)
        arr3.append(arr.count(i))

for j in arr3:
    print(j, end=' ')  # Number of occurrences