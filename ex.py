def merge_sort(sai):
    if len(sai) > 1:
        mid = len(sai) // 2
        l = sai[:mid]
        r = sai[mid:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                sai[k] = l[i]
                i += 1
            else:
                sai[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            sai[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            sai[k] = r[j]
            j += 1
            k += 1


def printer(sai):
    for i in range(len(sai)):
        print(sai[i], end=" ")
    print()


if __name__ == '__main__':
    sai = [2,4,6,3,0,4,6,8,9,4,2,4,98,-3,-4,7,65]
    merge_sort(sai)
    printer(sai)
