print('========================Tuple===============================')

credit_card1 = (23456798453, 'Felix Essienne', '10/20', 345)

credit_card2 = (23456798453, 'Rosina Essienne', '11/19', 236)

credit_cards = [credit_card1, credit_card2]

for i in credit_cards:
    print(i)
print()

# unpacking
person = ('Nana Yaw', 29, 'Pizza')
person1 = ('Rosina E', 28, 'Ampesi')

people = [person, person1]

for name, age, food in people:
    print(name)
    print(age)
    print(food)
    print()
