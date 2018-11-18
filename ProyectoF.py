from flask import Flask, request, g, redirect, url_for, render_template, flash, session
import flask
import sys
from flask import json
import random
from pathlib import Path
from os import path
import ast

# Inicializacion de variables
app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.secret_key = 'random string'
datosUsuario=[]
i=0
vuelosDic={}
usuarioL=[]
reserva=[]
reservaU={}
i=0
i1=0
cnt={}
cnt1=0
animacion=[]
@app.route('/main', methods=['GET', 'POST'])
def volverMain():
    """
    Funcion usada unicamente para retornar al html principal
    """
    global usuarioL
    entries=usuarioL
    return render_template('main2.html', entries=entries)
    
@app.route('/configuracion', methods=['GET', 'POST'])
def configuracion():
    """
    Funcion que pasa del main html al registro html
    """
    entries=[]
    if(request.method == 'POST'):
            print("hello")
            return render_template('registro.html', entries=entries)

    return render_template('main.html', entries=entries)
@app.route('/configuracion1', methods=['GET', 'POST'])
def configuracion1():
    """
    funcion que pasa del main html al login html

    """
    entries=[]
    if(request.method == 'POST'):
            print("helloll")
            return render_template('logeo.html', entries=entries)

    return render_template('main.html', entries=entries)
@app.route('/vuelos1', methods=['GET', 'POST'])
def verVuelos():
    """
    Funcion que manda al vuelo.html para poder buscar un vuelo
    """
    return render_template('vuelo.html')
@app.route('/vuelos', methods=['GET', 'POST'])
def verVuelos1():
    """
    Funcion en la que se busca si el vuelo buscado por el usuario
    existe
    """
    global animacion
    z=open("dicV.txt","r")
    z1=open("dicT.txt","r")
    o1=z1.read()
    o=z.read()
    #z.write(str(dic))
    x=ast.literal_eval(str(o))
    x1=ast.literal_eval(str(o1))
    aerolinea=str(request.form['aerolinea'])
    ciudadS=str(request.form['ciudad salida'])
    ciudadL=str(request.form['ciudad llegada'])
    codigoV=str(request.form['codigo de vuelo'])
    i=0
    vuelo=[]
    cont=0
    animacion=[]
    while cont!=4:
        cont=0
        if x["vuelo",str(i)][0]==aerolinea:
            cont+=1
            print("xd")
        if x["vuelo",str(i)][1]==ciudadS:
            cont+=1
            print("xd")
        if x["vuelo",str(i)][2]==ciudadL:
            cont+=1
            print("xd")
        if x1["vuelo",str(i)][0]==codigoV:
            cont+=1
        if cont==4:
            vuelo.append(x["vuelo",str(i)][0])
            vuelo.append(x["vuelo",str(i)][1])
            vuelo.append(x["vuelo",str(i)][2])
            vuelo.append(x1["vuelo",str(i)][0])
            vuelo.append(x1["vuelo",str(i)][1])
            vuelo.append(x1["vuelo",str(i)][2])
            entries=vuelo
            animacion.append(x["vuelo",str(i)][1])
            animacion.append(x["vuelo",str(i)][2])
        i+=1
        if i>=3867:
            flash("vuelo no encontrado o no existente")
            return redirect(url_for('verVuelos'))
    return render_template('vuelo2.html',entries=entries )


@app.route('/registrando', methods=['GET', 'POST'])
def registrando():
    """
    funcion que toma los datos del registro del usuario
    """
    global datosUsuario,i,usuarioL
    usuarioE=open("usuarios.txt","r")
    usuarioE1=usuarioE.read()
    x=ast.literal_eval((usuarioE1))
    datosUsuario=x
    print(datosUsuario)
    i=0
    while True:
        if (str(request.form['usuario']))==str(datosUsuario[i][0]):
            flash("Nombre de usuario ya existente")
            return render_template('main.html')
        #print((str(request.form['usuario'])))
        #print(str(x[i][0]))
        i+=1
        if i==len(x):
            break
    if len(usuarioL)>0:
        entries=usuarioL
        return render_template('main2.html', entries=entries)
    if len(str(request.form['usuario']))<6:
        flash("El nombre de usuario debe tener al menos de 6 caracteres")
        return render_template('main.html')
    if len(str(request.form['contrasena']))<6:
        flash("La contraseña debe tener al menos de 6 caracteres")
        return render_template('main.html')
    if(request.method == 'POST'):
            i=i+1
            indice="usuario",str(i)
            usuario=[]
            usuario.append(str(request.form['usuario']))
            usuario.append(str(request.form['contrasena']))
            usuarioL.append(str(request.form['usuario']))
            entries=usuarioL
            newU=[]
            newU.append(str(request.form['usuario']))
            newU.append(str(request.form['contrasena']))
            datosUsuario.append(newU)
            usuarioE2=open("usuarios.txt","w")
            usuarioE2.write(str(datosUsuario))                   
            print(entries)
    return render_template('main2.html', entries=entries)
@app.route('/deslogeando', methods=['GET', 'POST'])
def deslogearse():
    """
    funcion que deslogea al usuario
    """
    global usuarioL,cnt,i1,cnt1
    usuarioL=[]
    i1=0
    cnt1=0
    return render_template('main.html')
@app.route('/logeando', methods=['GET', 'POST'])
def logearse():
    """
    funcion que busca si los datos enviados por el usuario son
    verdaderos para logearse con una cuenta existente
    """
    global datosUsuario,usuarioL
    entries=[]
    usuarioE=open("usuarios.txt","r")
    usuarioE1=usuarioE.read()
    x=ast.literal_eval((usuarioE1))
    datosUsuario=x
    print(datosUsuario)
    print(len(datosUsuario))
    if len(usuarioL)>0:
        entries=usuarioL
        return render_template('main2.html', entries=entries)
    if(request.method == 'POST') and len(datosUsuario)>0:
        i=0
        x=str(request.form['usuario'])
        y=str(request.form['contrasena'])
        while i<=len(datosUsuario):
            if i==len(datosUsuario):
                flash("usuario no encontrado")
                return redirect(url_for('main'))
            if datosUsuario[i][0]==x and datosUsuario[i][1]==y:
                print("hello")
                break
            
            i+=1
        usuarioL.append(str(request.form['usuario']))
        entries=usuarioL       
        return render_template('main2.html', entries=entries)
    flash("usuario no encontrado")
    return render_template('main.html', entries=entries)

@app.route('/reservandoF1', methods=['GET', 'POST'])
def reservaF1():
    """
    funcion en la que se relaciona un usuario y la reserva que
    halla seleccionado
    """
    global usuarioL,reservaU,i1,cnt
    entries=[]
    lista=[]
    i1=0
    while i1<int(cnt[str(usuarioL)]):
        entries.append(reservaU[str(usuarioL),str(i1)][0])
        entries.append(reservaU[str(usuarioL),str(i1)][1])
        entries.append(reservaU[str(usuarioL),str(i1)][2])
        entries.append(reservaU[str(usuarioL),str(i1)][3])
        entries.append(reservaU[str(usuarioL),str(i1)][4])
        entries.append(reservaU[str(usuarioL),str(i1)][5])
        i1+=1
        
    return render_template('verReserva.html',entries=entries)
    
@app.route('/reservandoF', methods=['GET', 'POST'])
def reservaF():
    """
    funcion que revisa las reservas relacionadas con su usuario
    para mostrar todas la reservas
    """
    global reserva,reservaU,usuarioL,i,i1,cnt,cnt1
    i=0
    while True:
        if reserva[i][3]==str(request.form['Vuelo']):
            x=[]
            x.append(reserva[i][0])
            x.append(reserva[i][1])
            x.append(reserva[i][2])
            x.append(reserva[i][3])
            x.append(reserva[i][4])
            x.append(reserva[i][5])
            reservaU[str(usuarioL),str(i1)]=x
            entries=x
            reserva={}
            i1+=1
            cnt1+=1
            cnt[str(usuarioL)]=cnt1
            print(reservaU)
            break
        i+=1
    return render_template('verReserva.html',entries=entries)

@app.route('/animacion',methods=['GET', 'POST'])
def animacion():
    """
    funcion que revisa las coordenasdas de los estados que corresponden
    al viaje que el usuario busco, para luego ser mostradas en una
    animacion
    """
    global animacion
    x=open("coordenad.txt","r")
    x1=x.read()
    z=eval(x1)
    print(z[0][0])
    print(animacion[0])
    c=0
    i1=0
    for i in range(len(z)):
        if (animacion[0])==(z[c][0]):
            Latitud=z[i][2]
            Longitud=z[i][3]
            for i in range(len(z)):
                if animacion[1]==z[i1][0]:
                    Salida=z[i1][2]
                    Llegada=z[i1][3]
                    break
                i1+=1
        c+=1
    entries = {"Latitud":Latitud, "Longitud":Longitud,
               "Salida":Salida, "Llegada":Llegada}
    print(entries)
    return render_template('juego.html', entries=entries)


@app.route('/reservando1', methods=['GET', 'POST'])
def reserva1():
    """
    funcion que lleva a reserva html
    """
    return render_template('reserva.html')
@app.route('/reservando', methods=['GET', 'POST'])
def reserva():
    """
    funcion en la que se buscan vuelos para luego ser reservados
    """
    global reserva,usuarioL
    z=open("dicV.txt","r")
    z1=open("dicT.txt","r")
    o1=z1.read()
    o=z.read()
    #z.write(str(dic))
    x=ast.literal_eval(str(o))
    x1=ast.literal_eval(str(o1))
    aerolinea=str(request.form['aerolinea'])
    ciudadS=str(request.form['ciudad salida'])
    ciudadL=str(request.form['ciudad llegada'])
    i=0
    i1=0
    vuelo=[]
    r=[]
    cont=0
    entries={}
    while True:
        cont=0
        if x["vuelo",str(i)][0]==aerolinea:
            cont+=1
        if x["vuelo",str(i)][1]==ciudadS:
            cont+=1
        if x["vuelo",str(i)][2]==ciudadL:
            cont+=1
        if cont==3:
            vuelo=[]
            
            vuelo.append(x["vuelo",str(i1)][0])
            vuelo.append(x["vuelo",str(i1)][1])
            vuelo.append(x["vuelo",str(i1)][2])
            vuelo.append(x1["vuelo",str(i1)][0])
            vuelo.append(x1["vuelo",str(i1)][1])
            vuelo.append(x1["vuelo",str(i1)][2])
            r.append(vuelo)
            print(vuelo)
            reserva=r
            print(reserva)
            entries["vuelo",str(i)]=vuelo
            
        i1+=1
        i+=1
        if i>=3867:
            if len(vuelo)==0:
              return render_template('reserva.html')  
            break
    return render_template('reserva1.html', entries=entries)
@app.route('/', methods=['GET', 'POST'])
def main():
    """
    """
    entries = {}
            
    return render_template('main.html', entries=entries)



if __name__ == '__main__':
    app.run(debug=True)
