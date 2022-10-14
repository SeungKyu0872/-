import random

a = ['웅기', '승규', '무남', '석주', '상현','채은', '윤아', '예은','성훈','기윤','승민','창영','송섭','이주','현영',
'현웅','채령','대혁','진문','하림','보영','형운']
b = random.sample(a,5)
print(b)
for i in range(5):
    if b[i] in a:
        a.remove(b[i])
b = random.sample(a,5)
print(b)
for i in range(5):
    if b[i] in a:
        a.remove(b[i])
b = random.sample(a,4)
print(b)
for i in range(4):
    if b[i] in a:
        a.remove(b[i])
b = random.sample(a,4)
print(b)
for i in range(4):
    if b[i] in a:
        a.remove(b[i])
b = random.sample(a,4)
print(b)