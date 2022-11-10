# Вводиться два речові числа, кожне з нового рядка (наприклад i, j).
# Необхідно за допомогою тернарного умовного оператора найбільше значення присвоїти змінній d і вивести її на екран.

# Sample Input:
#  5.4
# -3.8

# Sample Output:
# 5.4

i = int(input('Enter i: '))
j = int(input('Enter j: '))
d = i if i > j else j
print(d)
# it's so hard for me
