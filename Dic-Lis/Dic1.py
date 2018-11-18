x=open("coordenadas.txt","r")
i=0
x1=[]
for i in range(23):
    x1.append(x.readline().split())
    i+=1
print(x1)
s=open("coordenada.txt","w")
s.write(str(x1))
