dummy_set_test = ["guy" , "thongtrachoo" , "23"]

explain = ["first" , "lastname" , "age"]

dummy_set_test[1:2] = ["walker" , "40"]



###########################################################

old_data = ["1985","1998","1999"]
print(old_data)
old_data[0:2] = ["2016","2018"]
print(old_data)

old_data_index3 = old_data.index("1999")
old_data_index2 = old_data.index("2018")
old_data_index1 = old_data.index("2016")

old_data[old_data_index1],old_data[old_data_index2],old_data[old_data_index3] = old_data[old_data_index3],old_data[old_data_index1],old_data[old_data_index2]

print(old_data)

###########################################################


a_list = ["a", "b", "c"]
index1 = a_list. index("a")
index2 = a_list. index("c")
a_list[index1], a_list[index2] = a_list[index2], a_list[index1]
print(a_list)
