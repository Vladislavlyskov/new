# # zadanie 10.6
count = 0
eq = True
with open("test.txt", "r", encoding = "utf-8") as my_file, open("out.txt", "r", encoding = "utf-8") as new_file:
    for a1, a2 in zip(my_file, new_file):
        count += 1
        if a1 != a2:
            eq = False
            break
print(f"Нет отличий") if eq else print(f"Отличается строка {count}")
#
# # zadanie 10.1
my_file = open('test.txt')
print(my_file.readline())
while True:
    line = my_file.readline()
    if not line:
        break

    print(line)
#
#
# my_file.close()
#
with open('test.txt') as my_file:
    lines = my_file.readlines()
    print(lines[4])

#zadanie 10.3
with open('test.txt', 'a') as my_file:
    my_file.writelines([input('enter ') + '\n' for i in range(3)])

# zadanie 10.5
with open('test.txt') as my_file, open('out.txt', 'w') as new_file, open('out1.txt', 'w') as new_file1:
    lines = my_file.readlines()
    new_file.writelines(lines[::2])
    new_file1.writelines(lines[1::2])
