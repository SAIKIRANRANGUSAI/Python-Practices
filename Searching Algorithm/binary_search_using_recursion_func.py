def rec_fun(sai, n, low, high):
    if high >= low:
        mid = (low + high) // 2
        if sai[mid] == n:
            return mid
        elif sai[mid] < n:
            return rec_fun(sai, n, mid + 1, high)  # Adjust low to mid + 1
        else:
            return rec_fun(sai, n, low, mid - 1)   # Adjust high to mid - 1
    else:
        return -1

sai = [1, 2, 3, 4, 5, 6, 7, 8]
n = 4
result = rec_fun(sai, n, 0, len(sai) - 1)
if result != -1:
    print("Present at index:", result)
else:
    print("Not found")
