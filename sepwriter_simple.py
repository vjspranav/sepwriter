import os

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
        if('scontext=' and 'u:object_r:' in perm[i]):
            scon = (perm[i].split('u:object_r:')[1]).split(':s0')[0]
        if('scontext=' and 'u:r:' in perm[i]):
            scon = (perm[i].split('u:r:')[1]).split(':s0')[0]
        if('tcontext=' and 'u:object_r:' in perm[i]):
            tcon = perm[i].split('u:object_r:')[1].split(':s0')[0]
        if('tcontext=' and 'u:r:' in perm[i]):
            tcon = perm[i].split('u:r:')[1].split(':s0')[0]
        if('tclass=' in perm[i]):
            tcl = perm[i].split('tclass=')[1]
    b = "allow " + scon + " " + tcon + ":" + tcl + " { " + per + " };"
    if b not in res: #Checking if denial resolution already exists or not
        res.append(b) #Adds the resolution to list
file.close()
res.sort()
count = len(res)

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

res = [i for i in res if '0 0 0 0' not in i]

#Creating the Sepolicy Directories if missing
if not os.path.exists('sepolicy'):
    os.mkdir('sepolicy')

#Writes all the resolutions in the respective files
for i in res:
    fn = i.split(' ')[1]+".te" #Here Goes the location of your sepolicy folder"
    file = open("sepolicy/"+fn, 'a')
    file.write(i+"\n")
    file.close

print(count, ' Denials resolved')

