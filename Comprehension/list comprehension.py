# Syntax: newList = [ expression(element) for element in oldList if condition ]

numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
print(doubled)

numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]
print(squared)

tmp_str = [char for char in 'Hello World!']
print(tmp_str)

lst = [x for x in range(10) if x % 2]
print(lst)

# nested loop in comprehension
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)

tmp_str.clear()
[tmp_str.append(char) for char in 'Hello World!']
print(tmp_str)

# lambda in list comprehension
lst = list(map((lambda i: i ** 3), [i for i in range(1, 4)]))
print(lst)

# if else in list comprehension
lst = ["Odd number" if x % 2 == 0 else "Even number" for x in range(1, 6)]
print(lst)

lst = [num for num in range(100) if num % 5 == 0 if num % 10 == 0]
print(lst)

matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
trans = [[i[j] for i in matrix] for j in range(len(matrix[0]))]
print(trans)

# lst = [367, 111, 562, 945, 6726, 873]
# ans = 0
# for n in str(123):
# 	ans += int(n)
# [(ans + int(n)) for n in str(123)]
# print(ans)


lst = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
tmp = [[x for x in lst if x == 0] + [x for x in lst if x == 1]]
print(tmp)
