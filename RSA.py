import RSA_def

rsa = RSA_def.RSA()

p = int(input("P : "))
q = int(input("Q : "))

rsa.P(p)
rsa.Q(q)
rsa.setON()
rsa.E_list()
while(1):
    e = int(input("E : "))
    if rsa.E(e):
        break
rsa.D_list()
while(1):
    d = int(input("D : "))
    if rsa.D(d):
        break


m = int(input("M : "))
print(rsa.Encrypt(m))

c = int(input("C : "))
print(rsa.Decrypt(c))