x = int(1)
y = int(0)
z = int(0)
sum = int(0)


while x < 4000000:
    x = x+y
    y = z
    z = x
    print(x)
    if x%2 == 0:
        sum = sum + x

print(sum)