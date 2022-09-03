import time

def numintolist(term):
    # this function will give the next term to the term which is given as an input
    digits=[]

    while term>0:
        digits.append(term%10)
        term=term//10
    digits.reverse()
    return(digits)

def seq(term):
    digits=numintolist(term)
    digits.append(digits[len(digits)-1]+1)
    ansl=[]
    i=0
    target=[]
    t=0
    ansll=[]
    while i < len(digits):

        r=0
        for j in range(i,len(digits)):
            if digits[j]==digits[i]:
                r+=1
            else:
                ansl.append([r,digits[i]])
                break
        i+=1
    l=len(ansl)
    ansl.append([0,0])
    for j in range(l):
        if ansl[j][1]!=ansl[j+1][1]:
            target.append(j+1)

    target=[0]+target
    target.remove(target[len(target)-1])

    for k in target:
        ansll.append(ansl[k])
            



    ansl.remove([0,0])
    return(ansll)


def ans(term):
    l=seq(term)
    ansl = []
    ans=0

    for i in l:
        ansl.append(i[0])
        ansl.append(i[1])

    for i in range(len(ansl)):
        ans+=ansl[i]*10**(len(ansl)-i-1)

    return ans




l=1
while True:
    print(l)
    l=ans(l)
    time.sleep(1)







