arr = [55,10,12,15]
n = len(arr)
if n == 0:
    print("not found")

for i in range(1,n-1):
    if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
        print(arr[i])
if arr[0]>=arr[1]:
    print(arr[0])
elif arr[n-1]>=arr[n-2]:
    print(arr[n-1])