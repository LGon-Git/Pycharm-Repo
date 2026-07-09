countries = ['Paris', 'Lagos', 'China', 'Peru', 'India']
countries.insert(0 ,'Benin')
countries.append('Nice')
countries.remove('China')
countries.pop(3)
for country in countries:
    print(country,'has',len(country), 'letters')

skills = ['Python','Linux','Git']
for skill in skills:
     print(skill,'has', len(skill),'letters')

for number in range(4):
    print(number)

for number in range(2):
    print('Python')

for number in range(len(skills)):
    print(number)