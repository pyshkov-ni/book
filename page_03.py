# Программа для обработки переменной s
# s содержит номер телефона в виде str. В новый new_s добавляются только цифры.

s = '8 (912) 651-23-56'
new_s = ''

for i in s:
    if i.isdigit() is True:
        new_s += i
    else:
        pass

print(new_s)
