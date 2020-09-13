import math
import random
asci=[" ","!",'"',"#","$","%","&","'","(",")","*","+",",","-",".","/","0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?","@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[","\\","]","^","_","`","","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","{","|","}","~"]
def primeGen(No):
    count = 3
    while True:
        isprime = True
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0: 
                isprime = False
                break
        if isprime and count>=No:
            return(count)
        count+=1
while True:
    i=int(input("gkey=1 encr=2 decr=3"))
    if i==1:#generate
        mowle=1
        p=primeGen(random.randint(10,20))
        while True:
          h=primeGen(random.randint(10,20))
          if h!=p:
            q=h
            break
        n=p*q
        l=(p-1)*(q-1)
        while True:
          h=primeGen(random.randint(10,20))
          if h!=p and h!=q and h<l:
            e=h
            break
        h=1
        while True:
          if (l*h+1)%e==0:
            d=(l*h+1)//e
            break
          print("current d try:"+str((l*h+1)/e))
          h+=1
        print('p='+str(p)+
        '\nq='+str(q)+
        '\nn='+str(n)+
        '\nl='+str(l)+
        '\ne='+str(e)+
        '\nd='+str(d)+
        '\n'+
        '\nopen key:'+str(e)+","+str(n)+
        '\nprivate key:'+str(d)+","+str(n)
        )#,end="")
    elif i==2:#encrypt
        i=input("public keys:").split(",")
        e=int(i[0])
        n=int(i[1])
        if input("norm=1")=="1":
            m=list(input("message:"))
            print("encripted msg:")
            for q in m:
                for w in range(len(asci)):
                    if q==asci[w]:
                        print((w**e)%n,end=",")
                        break
        else:
            m=input("encr num:")
            print((m**e)%n)
    elif i==3:#decrypt
        i=input("private keys:").split(",")
        d=int(i[0])
        n=int(i[1])
        m=list(input("message to decrypt:"))
        fm=""
        for q in m:
            print((int(q)**d)%n)
            fm+=asci[(int(q)**d)%n]
    print("\n=============================")
    #input("end\n[Enter to exit]")