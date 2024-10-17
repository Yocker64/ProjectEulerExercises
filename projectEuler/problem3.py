import timeit

startTime = timeit.default_timer()
number = int(600851475143)
div = int(3)
rest= int(0)
while div < number:
    if number%div==0:
        number = number/div
    else:
        div= div+1

print(div)
endTime = timeit.default_timer()
print((endTime - startTime))