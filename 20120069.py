def DFS(v, z, chk):
    chk[v] = 1
    ans = str(v)+' '
    for i in z[v]:
        if(chk[i]==0):
            ans = ans + DFS(i, z, chk)
    return ans

s = input()
s = s.split()
n = int(s[0])
m = int(s[1])
v = int(s[2])

z = []
for i in range(n+1):
    z.append([])
    
for i in range(m):
    s = input()
    s = s.split()
    a = int(s[0])
    b = int(s[1])
    z[a].append(b)
    z[b].append(a)

for i in range(n+1):
    z[i].sort()

chk = []
for i in range(n+1):
    chk.append(0)

print(DFS(v, z, chk))

for i in range(n+1):
    chk[i] = 0
ans = ''
x = [v]
chk[v] = 1
while(len(x)>0):
    v = x[0]
    x = x[1:]
    ans = ans + str(v) + ' '
    for i in z[v]:
        if(chk[i]==0):
            chk[i] = 1
            x.append(i)

print(ans)
