def mergesort(sai):
    if len(sai)>1:
        mid = len(sai)//2
        l = sai[:mid]
        r = sai[mid:]
        mergesort(l)
        mergesort(r)
        i = j = k = 0
        while i < len(l) and j< len(r):
            if l[i] < r[j]:
                sai[k] = l[i]
                i+=1
            else:
                sai[k] = r[i]
                j+=1
            k+=1
            while i< len(l):
                sai[k] = l[i]
                i+=1
                k+=1
            while j< len(r):
                sai[k] = r[j]
                j+=1
                k+=1
def printer(sai):
    for i in range(len(sai)):
        print(sai[i],end=" ")
    print()

if __name__ == '__main__':
    sai = [3,0,4,5,3,5,7,98,909,7,5,3,2,4,56,7,8,9,-2,8,6,4]
    mergesort(sai)
    print(sai)