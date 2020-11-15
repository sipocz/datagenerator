import pickle
rec={"vevo_vezetekneve":15,"vevo_keresztneve":15,"elerhetoseg":15,"tipus":20,"rendszam":10,"vizsga_ervenyesseg":12,"aktiv":2}
recpos={"vevo_vezetekneve":0,"vevo_keresztneve":15,"elerhetoseg":30,"tipus":45,"rendszam":65,"vizsga_ervenyesseg":75,"aktiv":87}
poslist=[0,15,30,45,65,75,87]

def insertchars(str,rec,pos):
    out=""
    #print(str,rec,pos)
    for i in range(len(str)):
        if i<pos or i>=pos+len(rec):
            
            out=out+str[i]
        else:
            out=out+rec[i-pos]
        #print(out)        
    return(out)

def  writearec(rec,lista):
    out=rec
    ind=0
    #print(lista)
    for i in lista:
        out=insertchars(out,lista[ind],poslist[ind])
        ind=ind+1
    return(out)    

def readcsvfile(fname):
    f=open(fname,encoding="cp1250")
    out=[]
    for l in f:
        rec=l.strip().split(",")
        out.append(rec)
    f.close()
    return(out)



record="#"*89
print(record)

o=insertchars(record,"alma",4)
print(record)
o=insertchars(o,"bala",12)
print(o)

adatlista=["Kis","Bőla","06204443331","Ford","LLL001","2021.11.01",'1' ]
poslist=[0,15,30,45,65,75,87]
writearec(record,adatlista)
records=readcsvfile("./nagyhazi_db_ansi.csv")
print(records)

outrec=""
for rec in records:
    baserec="\0"*89
    outrec=outrec+writearec(baserec,rec)

print(outrec)

f=open("binfile.txt","w")
for i in outrec:
    print(i,sep="",end="",file=f)

f.close()
#----------------------------------------------------------------------------------------------
'''
ypedef struct auto_adatai{
    char tipus[20];
    char rendszam[8];
    char javitas[30];
    char datum[12];
    char ar[11];
    char vizsga_ervenyesseg[12];
}auto_adatai;

'''
record="#"*93
print(record)



poslist=[0,20,28,58,70,81]

records=readcsvfile("./javitasok.csv")
print(records)

outrec=""
for rec in records:
    baserec="\0"*93
    outrec=outrec+writearec(baserec,rec)

print(outrec)

f=open("javfile.txt","w")
for i in outrec:
    print(i,sep="",end="",file=f)

f.close()
