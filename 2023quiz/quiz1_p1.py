a = int(input())
b = int(input())
if not a % b:
    print(2)
elif not b % a:
    print(1)
else:
    print(3)

