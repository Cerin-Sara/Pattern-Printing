#top left triangle
for i in range(5):
    for j in range(5,0,-1):
        if(i<j):
            print("* ", end=' ')
    print("\n")