#Writing the Sepolicy
file = open("denials.txt", "r")
lines = file.readlines()
res = []
c=0
for a in lines: 
    perm = [x for x in a.split(" ")]
    for i in range(len(perm)):
        if(perm[i] == '{'):
            per = perm[i+1]
        if('scontext=' in perm[i]):
            scon = (perm[i].split('r:')[1]).split(':s0')[0]
        if('tcontext=' in perm[i]):
            tcon = (perm[i].split('r:')[1]).split(':s0')[0]
        if('tclass=' in perm[i]):
            tcl = perm[i].split('tclass=')[1]
    b = "allow " + scon + " " + tcon + ":" + tcl + " { " + per + " };"
    if b not in res: #Checking if denial resolution already exists or not
        res.append(b) #Adds the resolution to list
file.close()
res.sort()

#Adding multiple permissions to same line
for i in range(1,len(res)):
    c=i
    while(res[c].split(' ')[2]==res[i-1].split(' ')[2] and res[c].split(' ')[1]==res[i-1].split(' ')[1]):
        res[i-1] = res[i-1][:-2] + ' ' + res[c].split(' ')[4] + ' ' + res[0][-2:]
        res[c]='0 0 0 0 0'
        c += 1
        if(c==len(res)):
            break
    i=c

for i in res:
    if '0 0 0 0' in i:
        res.remove(i)

#Writes all the resolutions in the respective files
for i in res:
    fn = "sepolicy/"+i.split(' ')[1]+".txt" #Here Goes the location of your sepolicy folder"
    file = open(fn, 'a')
    file.write(i+"\n")
    file.close
 
