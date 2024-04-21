sai = [1, 2, 3, 4, 5, 6, 7, 8]
n = 6

low = 0
high = len(sai) - 1

while low <= high:
    mid = (low + high) // 2

    if sai[mid] == n:
        print("Found:", n)
        break
    elif sai[mid] > n:
        high = mid - 1
    else:
        low = mid + 1
else:
    print("Not found")

print("sai:", sai)
