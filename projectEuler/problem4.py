import timeit

startTime = timeit.default_timer()
greatest = int(10001)
first = int(100)
sec = int(100)

def checkPalindrome(number):
    return str(number) == str(number)[::-1]

for firstsum in range(900):
    for secsum in range(900):
        if checkPalindrome((firstsum+first)*(secsum+sec)):
            if (firstsum+first)*(secsum+sec)> greatest:
                greatest = (firstsum+first)*(secsum+sec)     
endTime= timeit.default_timer()
print(greatest)
print(endTime-startTime)