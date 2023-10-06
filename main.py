Np = int(input("Np: "))
No = int(input("No: "))
T = int(input("T: "))
Ntp = int(input("Ntp: "))
M = int(input("M: "))
O = int(input("O: "))
K = int(input("K: "))
d = 52
Td = 168

D = d - O - K
t = Td - M
Ri3 = (Np*D*t)/(T*No*d*Td)
RinB = ((Np+Ntp)*D*t)/(T*No*d*Td)

print(f"D: {D}, t: {t}, Ri3: {Ri3}, RinB: {RinB}")