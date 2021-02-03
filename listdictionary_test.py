print('========================List []===============================')

names = ['Felix', 'Suzzy', 'Rosina', 'Mark']

lt = []  # mutable

for person in names:
    lt.append(person)
print(lt)
print()

# comprehension of lists
print([person for person in names])
print()

# another comprehension of lists
print([person + ' dumped me' for person in names])
print()
print('***************************************************************')

print('========================Dictionary===============================')

# dictionary
movies = {'Batman': 8, 'SpiderMan': 10, 'Avengers': 29, 'Poku Hunter': 2}

movie_list = []

for movie in movies:
    if movies[movie] > 6:
        movie_list.append(movie)
print(movie_list)
print()

# dictionary to list comprehension
print([movie for movie in movies if movies[movie] > 6])
