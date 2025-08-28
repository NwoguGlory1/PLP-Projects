my_list = []
a = [10, 20, 30, 40]
for i in a:
    my_list.append(i)
my_list.insert(1, 15)
my_list.extend([50, 60, 70])
my_list.remove(70)
my_list.sort()
position = my_list.index(30)
print(position)
#index(self, value, start=0, stop=9223372036854775807, /) unbound builtins.list method
    # Return first index of value.