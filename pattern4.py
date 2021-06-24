#right bottom triangle
for i in range(5+1):
    for j in range(5+1,0,-1):
        if(i<j):
            print("  ", end=' ')
        else:
            print("* ", end=' ')
    print("\n")
print()