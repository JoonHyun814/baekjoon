answer = []

def gcd(x, y):
   while y:
       x, y = y, x % y
   return x

def is_possible(a,b,c):
    if c%gcd(a,b) == 0:
        return True
    else: False


for _ in range(int(input())):
    a,b,c = map(lambda x:int(x),input().split(' '))
    if a < c and b < c:
        answer.append('No')
        continue
    a,b = sorted([a,b])

    if is_possible(a,b,c):
        answer.append('Yes')
    else:
        answer.append('No')

for a in answer:
    print(a)