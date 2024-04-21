sai = " Sai kiran rangu is cool"
sai = sai.lower()
dic_tionary = {}
for i in sai:
    if i in dic_tionary:
        dic_tionary[i] +=1
    else:
        dic_tionary[i] = 1
print(dic_tionary)

# another way

new_list_key = []
second_list_used_to_count_values = []
for i in sai:
    if i not in new_list_key:
        new_list_key.append(i)
        second_list_used_to_count_values.append(1)
    else:
        ind_ex = new_list_key.index(i)
        second_list_used_to_count_values[ind_ex] +=1
result = dict(zip(new_list_key,second_list_used_to_count_values))
print(result)