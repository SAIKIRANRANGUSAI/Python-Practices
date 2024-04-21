sai = "saikiran rangu"
if len(sai) > 3:
    if "ing" not in sai[-3:]:

        sai = sai.replace(sai[-3:],"ing")
    else:
        sai = sai+"ly"
print(sai)


