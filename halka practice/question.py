
def answer(num):
    ans=0
    while (num !=0):
        ans= ans+int(num%10)
        num = int(num/10)
    return ans
num = int(input("Enter number: "))
print(answer(num))
#ans = pow(num[0],num[2])+pow(num[1],num[2])+pow(num[2],num[1])
#print("the ans is", ans)
