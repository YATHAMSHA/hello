"""RUN ON PYTHON 3"""
n = int(input("input n"))
for i in range(0,n,1):
    for j in range(0,n,1):
        if i <= j:
            print("*", end = "")
        else:
            print(" ", end = "")
    print("")
