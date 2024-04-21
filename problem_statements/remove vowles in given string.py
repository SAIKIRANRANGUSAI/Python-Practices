sai ="saikiranrangu"
vowles = "aeiou"
kiran = list(sai.lower())
for i in kiran:
    if i in vowles:
        kiran.remove(i)
sai = "".join(kiran)
print(sai)
