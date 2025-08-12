my_list = []
elements_to_add = [10,20,30,40]
for elements in elements_to_add:
   my_list.append(elements)
print(my_list)

my_list.insert(1,15)
print(my_list)

new_list = [50,60,70]
my_list.extend(new_list)
print(my_list)

my_list.pop()
print(my_list)

my_list.sort()
print(my_list)

element_to_find = 30
index = my_list.index(element_to_find)
print(f"The index of '{element_to_find}' is: {index}")

