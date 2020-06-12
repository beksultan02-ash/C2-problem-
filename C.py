a=input()
b=bin(int(a))
c=b[2:][::-1]
d=int(c,2)
print(d)