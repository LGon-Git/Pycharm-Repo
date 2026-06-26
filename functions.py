def get_age():
    age = int(input('What is your age?' ))

age = get_age()
print(age)

def get_age():
    return int(input('What is your age?' ))
age = get_age()
print(age)

def get_number():
    return int(input('What is your number?' ))
number = get_number()
print(number * 5)
if number > 18:
    print('is an adult or Gardian present?')
else:
    print('Welcome,you can proceed ')


def get_temperature():
    return int(input('What is the temperature?' ))

def weather_message(temp):
    if temp >= 30 :
        print("It's not to hot today")

temperature = get_temperature()
weather_message(temperature)

