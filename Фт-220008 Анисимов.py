def main():
    n=int(input("Введите количество критериев"))
    a=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i == j):
                a[i][j] = 1.00
            else:
                print("Введите отношение критерия", i+1 , "к критерию", j+1,"(число в десятичном формате)")
                a[i][j]=float(input())
    ves(a)

def ves(a,n):
    sum =0.0

    for i in range(n):
        for j in range(n):
            sum+=a[i][j]







if __name__ == "__main__":
        main()