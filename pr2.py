n = int(input("Introduce n: "))
m = int(input("Introduce m: "))
if n>m:
    def factorial(x):
        f=1
        for i in range(1,x+1):
            f=f*i
        return f
c= (factorial(n))/((factorial(m))* (factorial(n-m)))
print(c)