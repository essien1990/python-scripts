# Email Address Text Scrapper
import re
print('========================Regex Expression===============================')

# Example 1
text = 'A random message'

# matches entire text
pattern = re.compile('A random message')

result = pattern.search(text)

print(result)


print()

# Example 2

# match the Capitalized Letter A
pattern1 = re.compile('[ABC]')

result2 = pattern1.search(text)

print(result2)

print()


text2 = 'random message. nanaitconsult@gmail.com. some more random text.'

# Example 3
# Match small letter and big letter, + matches the entire multiple strings

pattern2 = re.compile('[a-zA-Z]+')


result2 = pattern2.search(text2)

print(result2)


print()


text3 = 'random message. nanaitconsult123@gmail.com. some more random text. felix.essienne_88-88@company.net'

# Example 4
# emails, digit and strings, [a-z]-all lower letters, A-Z-all upper-case letters, 0-9-all digits, + - 1 or more, @ - emails
# \. - for escaping special characters

pattern3 = re.compile('[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+\.[a-zA-Z]+')


result3 = pattern3.findall(text3)

print(result3)
