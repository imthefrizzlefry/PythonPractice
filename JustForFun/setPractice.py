my_set = set()

my_set.add("a")
if "b" not in my_set:
    my_set.add("b")
my_set.add("a")

print(len(my_set))
print(my_set)