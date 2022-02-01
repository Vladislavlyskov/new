def funk(a):
    while True:
        b = input('Enter ')
        if b == 'stop':
            break
        a = a + int(b)
        print(a)
funk(0)

def func(d):
    while True:
        c = input('Enter ')
        if c == 'stop':
            break
        d = d * int(c)
        print(d)
func(1)