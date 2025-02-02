"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 
 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 
 (three hundred and forty-two) contains 
 letters and 
 (one hundred and fifteen) contains 
 letters. The use of "and" when writing out numbers is in compliance with British usage.
 """

# First I will list all the posible single word we are gonna use
# We have: one, tow, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen
# fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty
# Twenty, Thirty, Forty, Fifty, Sixty, Seventy, Eighty, Ninety, Hundred, thousand


# Returns the number of characters of the name of a number
def number_to_english(n):
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
            "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = [None, None, "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if 0 <= n < 20:
        return ones[n]
    elif 20 <= n <= 90 and n % 10 == 0:
        return tens[n // 10]
    elif 20 < n < 100:
        return tens[n // 10] + "-" + ones[n % 10]
    elif 100 <= n <= 900 and n % 100 == 0:
        return ones[n // 100] + " hundred"
    elif 100 < n < 1000:
        return ones[n // 100] + " hundred and " + number_to_english(n % 100)
    elif 1000 < n < 10000:
        pass
    elif n == 1000:
        return "one thousand"
    else:
        raise ValueError("unexpected input")

#Initial variable that is gonna aument its value until a 1000 to compare
def solve():
    """ Compute the answer to Project Euler's problem #17 """
    target = 1000
    answer = 0
    for i in range(target):
        words = number_to_english(i + 1).replace(" ", "").replace("-", "")
        answer += len(words)
    return answer

print(solve())