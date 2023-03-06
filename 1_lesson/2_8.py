#3 2 4 -> yes
#3 2 1 -> no

n = int(input('Enter N: '))
m = int(input('Enter M: '))
k = int(input('Enter K: '))
answer = 'yes' if (k%n == 0 or k%m ==0 and k <= n*m) else 'no'
print(answer)