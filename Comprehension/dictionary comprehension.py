keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]
my_dict = dict(zip(keys, values))
print(my_dict)

tmp_string = "abrhdasd"
my_dict = {char: tmp_string.count(char) for char in tmp_string}
print(my_dict)

my_dict = {x: x ** 2 for x in range(5)}
print(my_dict)

my_dict = {'odd': [x for x in values if x % 2]}
print(my_dict)
