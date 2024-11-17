def isprime(x):
    if x==2:
        return True
    for i in range(2,x-1):
        if x%i==0:
            return False
    return True
def ishuiwen(x):
    s = str(x)
    ss = s[::-1]
    if s==ss:
        return True
    else:
        return False
if __name__ == '__main__':
    n = int(input())
    count = 0
    m = 2
    while True:
        if count==n:
            break
        if isprime(m) and ishuiwen(m):
            print(m,end=" ")
            count += 1
        m += 1
