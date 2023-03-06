#385916 -> yes
#123456 -> no

n = int(input('Enter number of ticket: '))
firstPurtOfNumber = n//1000
secondPurtOfNumber = n%1000
answer = 'yes' if (firstPurtOfNumber//100 + firstPurtOfNumber//10%10 + firstPurtOfNumber%10) == (secondPurtOfNumber//100 + secondPurtOfNumber//10%10 + secondPurtOfNumber%10) else 'no'
print(answer)