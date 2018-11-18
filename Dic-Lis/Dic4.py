import ast
def verVuelos():
    vuelos=(open("viaje.txt","r"))
    i=0
    x1=[]
    lista1=[]
    
    for i in range(967):
        x1.append(vuelos.readline().split())
    for i in range(967):
        nl=[]
        nl.append(x1[i][1])
        nl.append(x1[i][3])
        nl.append(x1[i][5])
        lista1.append(nl)
        i+=1
    i=0
    x2=[]
    lista2=[]
    
    for i in range(967):
        x2.append(vuelos.readline().split())
    for i in range(967):
        nl=[]
        nl.append(x2[i][1])
        nl.append(x2[i][3])
        nl.append(x2[i][5])
        lista2.append(nl)
        i+=1
    i=0
    x3=[]
    lista3=[]
    
    for i in range(967):
        x3.append(vuelos.readline().split())
    for i in range(967):
        nl=[]
        nl.append(x3[i][1])
        nl.append(x3[i][3])
        nl.append(x3[i][5])
        lista3.append(nl)
        i+=1
    i=0
    x4=[]
    lista4=[]
    
    for i in range(967):
        x4.append(vuelos.readline().split())
    for i in range(967):
        nl=[]
        nl.append(x4[i][1])
        nl.append(x4[i][3])
        nl.append(x4[i][5])
        lista4.append(nl)
        i+=1
       
    #x1.split()
    viajes=open("horario.txt","w")
    viajes2=open("viajo22.txt","w")
    viajes3=open("viajo33.txt","w")
    viajes4=open("viajo44.txt","w")
    viajes.write(str(lista1))
    viajes2.write(str(lista2))
    viajes3.write(str(lista3))
    viajes4.write(str(lista4))
    dic={}
    i1=0
    i=0
    for i in range(967):
        dic["vuelo",str(i1)]=lista1[i]
        i+=1
        i1+=1

    i=0
    for i in range(967):
        dic["vuelo",str(i1)]=lista2[i]
        i+=1
        i1+=1

    i=0
    for i in range(967):
        dic["vuelo",str(i1)]=lista3[i]
        i+=1
        i1+=1

    i=0
    for i in range(967):
        dic["vuelo",str(i1)]=lista4[i]
        i+=1
        i1+=1
    z=open("j2.txt","w")
    #o=z.read()
    z.write(str(dic))
    #x=ast.literal_eval(str(o))
    #print(x)
    
##    while len(vuelos.readlines())>=i:
##        
##        x=vuelos.readline()
##        print(x)
##        i+=1
##    print(x)
