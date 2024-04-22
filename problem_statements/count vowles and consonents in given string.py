sai ="saikiran rangu"
vowles ="aeiou"
consonents = 0
vowle = 0
for i in sai:
    if i not in vowles:
        consonents+=1
    else:
        vowle +=1
print("Vowles :", vowle)
print("Consonents :", consonents)
