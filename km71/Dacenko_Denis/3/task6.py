# Програма для знаходження кількості парт у класі
# кількість учнів у кожному класі
class1 = int(input())
class2 = int(input())
class3 = int(input())
# Знаходженя кількості парт
print(class1 % 2 + class2 % 2 + class3 % 2 + class1 // 2 + class2 // 2 + class3 // 2)
input()
