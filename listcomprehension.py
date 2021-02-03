names = ['james', 'Kofi', 'Ama', 'Jane']

# using for loop
l = []

for person in names:
    l.append(person)
print(l)

# using list comprehension
c = [person for person in names]
print(c)


# another comprehension of lists
print([person + ' dumped me' for person in names])
print()
print('***************************************************************')
