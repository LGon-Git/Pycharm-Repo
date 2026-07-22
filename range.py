from functions import languages

for number in range(5):
    print(number)

for number in range(3,8):
    print(number)

for number in range(6,1,-1):
    print(number)

for number in range(1,11,2):
    print(number)

for number in range(1,10,2):
    print(number)

for number in range(1,6,2):
    print(number*2)

for number in range(5,-1):
    print('Countdown')
    print(number)
    print('Blast off!')

for number in range(6):
    print(number,'squared is',number*number)

languages = ['Python','Linux','Git','SQL']
for language in range(len(languages)):
    print(len(languages), language)

colors = ['red','green','blue']
print(colors)
print(len(colors))

for color in range(len(colors)):
    print(color)
colors.append('yellow')
for number in range(len(colors)):
    print(number)
print(colors)

print(len(colors))
print(range(len(colors)))
for number in range(len(colors)):
    print(number, colors[number])

words = ['Python','Linux','Git']
for number in range(len(words)):
    print(words[number],'has',len(words),'letters')

    print('2nd test')

words = ['Python', 'Linux', 'Git']
for number in range(len(words)):
    print(number,words[number], len(words[number]))