for i in range(5,0,-1):
    for j in range(5-i):
        print(' ', end='') # printing space and staying in same line
    
    for j in range(2*i-1):
        print('*',end='') # printing * and staying in same line
    print()