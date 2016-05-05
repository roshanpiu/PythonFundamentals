#lists stores ordered collections of items

my_list = ["a","b","c"]

print(type(my_list))
print(len(my_list))
print("a" in my_list)
print("x" in my_list)
print("x" not in my_list)

print(my_list[0])
print(my_list[1])

my_list.append("d")
print(my_list)

#find last item of list
print(my_list[len(my_list)-1])
print(my_list[-1])
print(my_list[-2])

my_name = "Roshan"
print(my_name[0])
print(my_name[-1])

print(my_name.lower())