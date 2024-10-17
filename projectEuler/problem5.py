number = int(1)
numbers = [None]*20
for trues in range (20):
    numbers[trues]= True

for rang in range (0,19):
    if numbers[rang+1]== True:
        number = number*(rang+1)
    for rang2 in range(0,rang+1):
        if rang*rang2<20 & rang!=rang2:
            print(rang*rang2)
            numbers[rang*rang2]=False


print(number)

