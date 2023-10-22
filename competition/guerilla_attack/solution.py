N_M_K = input().split()
spies = []
camps = []
k = int(N_M_K[2])
for n in range(int(N_M_K[0])):
    spics_1 = input().split()
    spies.append(spics_1)
for m in range(int(N_M_K[1])):
    camps_1 = input().split()
    camps.append(camps_1)

distance = []
for j in camps:
    for i in spies:
        newcods = []
        m = int(j[0]) - int(i[0])
        n = int(j[1]) - int(i[1])
        newcods.append(m)
        newcods.append(n)
        distance.append(newcods)
square_dis = []
for sublists in distance:
    square_dis.append(int(sublists[0]) ** 2 + int(sublists[1]) ** 2)
s = set(square_dis)
_l = list(s)
_l.sort()

print(_l[k - 1])
