import re
porintsInEn = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}
pointsInRu = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
s = '[а-яА-Я]'
inputText = input().upper()
if (re.search('[а-яА-Я]', inputText)):
	print(sum([sumOfLetter for i in inputText for sumOfLetter, weigthOfCh in pointsInRu.items() if i in weigthOfCh]))
else:
	print(sum([sumOfLetter for i in inputText for sumOfLetter, weigthOfCh in porintsInEn.items() if i in weigthOfCh]))