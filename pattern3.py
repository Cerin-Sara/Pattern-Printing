#left top triangle

#alternatively
# for i in range(5):
#     for j in range(5,0,-1):
#         if(i<j):
#             print("* ", end=' ')
#     print("\n")

for i in range(5):
    for j in range(i,5,1):
        print("* ", end=" ")
    print("\n")