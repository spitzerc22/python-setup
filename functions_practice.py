def hello():
    print('Welcome!')

def pack(a, b, c):
    return[a, b, c]

def eat_lunch(*args):
    #for i in args :
    #   print(f'First I eat {eat_lunch[0]}')
    #^ My attempt, had to look at solution code.
    if len(args) == 0: #comparing length to see if anything is passed through
        print('MY lunchbox is empty!')
    else:
        for i in range(len(args)): #syntax: range(stop) so range will stop at length of args
            if i == 0:
                print(f'First I eat {args[0]}')
            else: 
                print(f'Next I eat {args[i]}')


hello()
print(pack('brush', 'food', 'pillow'))
eat_lunch()
eat_lunch('brat', 'oranges', 'chips')