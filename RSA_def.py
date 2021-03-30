import math
import random as rand
class RSA:
    def __init__(self):
        print("HI")

    def P(self, p):
        self.p = p

    def Q(self, q):
        self.q = q

    def setON(self):
        self.n = self.p * self.q
        self.o = (self.p-1) * (self.q-1)
        print("your n : ", self.n)
        print("your o : ", self.o)

    def E_list(self):
        print("可輸入的互質數有 : ")
        ls = []
        while len(ls) < 6:
            y = rand.randint(1,1000)
            for i in range(2,self.o):
                if y % i == 0 and self.o % i == 0:
                    break
                else:
                    ls.append(y)
                    break
        print(ls)
            
    def E(self, e):
        for i in range(2,self.o):
            if e % i == 0 and self.o % i == 0:
                return False
        self.e = e
        return True

    def D_list(self):
        print("可輸入的數有 : ")
        ls = []
        while len(ls) < 6:
            y = rand.randint(1,1000)
            if (y*self.e)%self.o==1:
                ls.append(y)
                
        print(ls)

    def D(self, d):
        if (d*self.e)%self.o==1:
            self.d = d
            return True
        return False 

    def Encrypt(self, m):
        c = (m**self.e)%self.n
        return c

    def Decrypt(self, c):
        m = (c**self.d)%self.n
        return m

    
# if __name__ == '__main__':
