sai =" sai kiran rangu is cool saikiran"
kiran = sai.split()
rangu = ''
for i in kiran:
    if len(i) > len(rangu):

        rangu = i


print(rangu)