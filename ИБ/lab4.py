# шифрование методом контрольных сумм 
def KSumm(P, MaxVal):
    v=0
    for i in P:
        v+=i
        if v>MaxVal:
            v-=MaxVal
            v-=1
    return v

# шифрование методом хеширования с применением гаммирования
def SummKodBukvOtkr(P, MaxVal, a, b, c, t):
    p=[]
    for i in P:
        t=(a*t+b)%c
        p.append(i^t)
    return KSumm(p, MaxVal)


# функция выводит в консоль контрольные суммы
# для нескольких сообщений методом контрольных сумм (KSumm) 
# и методом хеширования с применением гаммирования (SummKodBukvOtkr)
# для варианта 1
class glob:
    a=17
    b=11
    c=256
    t_0=172
    maxVal=255
def echo(m):
    b=[ord(i) for i in m]
    print('P='+repr(m)+', KSumm='+str(KSumm(b, glob.maxVal))+
    ', SummKodBukvOtkr='+str(SummKodBukvOtkr(b, glob.maxVal, glob.a, glob.b, glob.c, glob.t_0)))
echo('0123456789')
echo('9876543210')
echo('1000005')
echo('1500000')

