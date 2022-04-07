import random
def rand():
    n=random.randint(0,100)
    return n
def sumrand(a,b):
    sum=a+b
    return sum
totalmarks=0
incorrectans=0
correctans=0
for i in range(1,4):
    e=rand()
    f=rand()
    a=int(input(f"Enter the sum of {e} and {f}\n"))
    if(a==sumrand(e,f)):
        totalmarks+=10
        correctans+=110
    else:
        totalmarks-=5
        incorrectans+=1
# sum=int(n+m)

# a=int(input(f"Enter the sum of {n} and {m}\n"))
# if(a==sum):
#     totalmarks+=10
#     correctans+=1
# else:
#     totalmarks-=5
#     incorrectans+=1
print(f"Corectanswer-{correctans}")
print(f"Incorectanswer-{incorrectans}")
print(f"totalmarks-{totalmarks}")