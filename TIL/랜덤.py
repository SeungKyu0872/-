import random

a = ['웅기', '승규', '무남', '석주', '상현', '대혁', '채은', '윤아', '예은', '형운']
b = random.sample(a,3)
print(b)
for i in range(3):
    if b[i] in a:
        a.remove(b[i])
b = random.sample(a,3)
print(b)
for i in range(3):
    if b[i] in a:
        a.remove(b[i])
b = random.sample(a,4)
print(b)