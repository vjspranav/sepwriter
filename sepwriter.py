#Writing the Sepolicy
file = open('denials.txt', "r")
lines = file.readlines()
res = []
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
    b = "allow " + scon + " " + tcon + ":" + tcl + " {" + per + "};"
    if b not in res: #Checking if denial resolution already exists or not
        res.append(b) #Adds the resolution to list
file.close()
res.sort()
#Writes all the resolutions in the respective files
for i in res:
    fn = "sepolicy/"i.split(' ')[1]+".txt" #Here Goes the location of your sepolicy folder"
    file = open(fn, 'a')
    file.write(i+"\n")
    file.close
 
