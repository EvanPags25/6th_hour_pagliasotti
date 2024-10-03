#Name: Evan Pagliasotti
#Hour: HR6
#Assignment: HW6
#assist from:https://www.toppr.com/guides/python-guide/examples/python-examples/functions/number-divisible/python-program-find-numbers-divisible-another-number/#:~:text=In%20Python%2C%20the%20remainder%20operator,then%20it%20will%20be%20divisible.

print("hello world")


#if a number can be divisbale by another number
# or not
num=100

if num%2==0:
    if num%3==0:
        print(num/2),
        print(num/3),
    else:
        print("not divisible by 3"),
        print(num/2),
else:
    if num%3==0:
        print("not divisible by 2"),
        print(num/3),
    else:
        print("neither is divisible by 2 or 3")