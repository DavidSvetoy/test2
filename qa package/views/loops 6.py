n = int(input('Enter a number : '))
reversed = 0
while(n!= 0):
    d=int(n%10)
    reversed = reversed*10 + d
    n=int(n/10)
print(reversed)
print(reversed*2)