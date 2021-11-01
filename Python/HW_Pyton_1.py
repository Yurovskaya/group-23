# переменная типа String
a = "Ada"
# переменная типа Integer
b = 320
# переменная типа Float
c = 89.67
# переменная типа Bytes
d = bytes(14)
# переменная типа List
f = ["List:\nJon\nCat\nMoon"]
# переменная типа Tuple
g = (36.6, 'Normal', False)
# переменная типа Set
s = {1, 2, 3, 4, 5, 6}
# переменная типа  Frozen set
k = ['A', 'N', 'G']
fs = frozenset(k)
# переменная типа Dict
h = {"Apple": "1",  "Banana": "2"}

# Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(type(a))

print(type(b))

print(type(c))

print(type(d))

print(type(f))

print(type(g))

print(type(s))

print(type(fs))

print(type(h))

# Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
sd = "I love"
sa = "apple"
res = "{} {}".format(sd,sa)
print(res)

# Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
name = "Dasha"
age = 28
print(name, age)

# Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)

d = "Dashs"
salary = 1000

print(name  ,+ salary)






