def sai(kiran):
    if kiran <= 1:
        return False
    elif kiran == 2:
        return True
    else:
        for i in range(2, kiran):
            if kiran % i == 0:
                return False
        return True

result = sai(7)
print(result)
