countries = ['Paris', 'Lagos', 'China', 'Peru', 'India']
countries.insert(0 ,'Benin')
countries.append('Nice')
countries.remove('China')
countries.pop(3)
for country in countries:
    print(country,'has',len(country), 'letters')
