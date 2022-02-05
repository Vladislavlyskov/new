list = ['доход', 'обход', 'восток']
for i in list:
    if i == i[::-1]:
        print(i,  '- Palindrome')
    else:
        print('Not Palindrome')

list1 = ['доход', 'обход', 'восток']
list2 = [i for i in list1 if i == i[::-1]]
print(i, '- Palindrome')


