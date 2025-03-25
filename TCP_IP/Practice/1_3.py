a = 1
b = 1.1
c = "AAA"

print(type(a))
print(type(b))
print(type(c))

n = input()
print(type(n))
try:
    m = int(n)
    print(m, " ", type(m))
except:
    print("input Error")

print("test : %d, %1f, %s" %(5,5,5))