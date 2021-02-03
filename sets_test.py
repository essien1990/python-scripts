print('========================Sets {elements}===============================')

list_of_numbers = [1, 2, 3, 4, 4, 5, 1, 7, 8, 9, 9, 10]

no_duplicate_sets = set(list_of_numbers)

list_of_numbers = no_duplicate_sets

no_duplicate_list = list(list_of_numbers)

print(no_duplicate_list)

print('**********************************************************************************************************')

library1 = {'Hunger Games', 'Thor', 'Avengers', 'The Flash'}
library2 = {'Hunger Games', 'Lord of the Rings', 'Hulk'}

# union
all_book = library1.union(library2)
print(all_book)
print()

# both set
both_book = library1.intersection(library2)
print(both_book)
print()

# difference
diff_book = library1.difference(library2)
print(diff_book)
print()
