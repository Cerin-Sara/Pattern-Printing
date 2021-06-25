#right top triangle with
for i in range(1, 5+1):
    for j in range(1, 5+1):
        if(j < i):
            print(' ', end = '  ')
        else:
            print('*', end = '  ')
    print()