#importamos los modulos necesarios
import correo
import tkinter 
import tkinter.ttk as ttk

def fijar(*args):
    """función que crea la segunda ventana, lee los datos de la primera y da pie a crear la tercera
    en la segunda ventana se introducen el cuerpo y la cabecera del mensaje"""
    lista = []
    contador = 0
    #lectura de las checkbox de la primera ventana
    if c0.get():
        lista.append(departamentos[0])
        contador += 1
    if c1.get():
        lista.append(departamentos[1])
        contador += 1
    if c2.get():
        lista.append(departamentos[2])
        contador += 1
    if c3.get():
        lista.append(departamentos[3])
        contador += 1
    if c4.get():
        lista.append(departamentos[4])
        contador += 1
    if c5.get():
        lista.append(departamentos[5])
        contador += 1
    if c6.get():
        lista.append(departamentos[6])
        contador += 1
    if c7.get():
        lista.append(departamentos[7])
        contador += 1
    #proceso de cerrado de la primera ventana y creación de la segunda
    root0.destroy()
    root1 = tkinter.Tk()
    root1.title("Mensaje y asunto")
    mainframe1 = ttk.Frame(root1, padding = "5 5 5 5")
    mainframe1.grid(row = 0, column = 0, sticky = tkinter.W)
    asuntoframe1 = ttk.Frame(root1, padding = "5 5 5 5")
    asuntoframe1.grid(row = 0, column = 0, sticky = tkinter.W)
    mensajeframe1 = ttk.Frame(root1, padding = "5 5 5 5")
    mensajeframe1.grid(row = 1, column = 0, sticky = tkinter.W)

    ttk.Label(asuntoframe1, text = "Asunto del mensaje:").grid(row = 0, column = 0, sticky = tkinter.W)
    asunto = tkinter.StringVar()
    asuntoEntry1 = ttk.Entry(asuntoframe1, width = 83, textvariable = asunto)
    asuntoEntry1.grid(row = 0, column = 1, sticky = tkinter.W)

    ttk.Label(mensajeframe1, text = "Mensaje:").grid(row = 0, column = 0, sticky = tkinter.W)
    texto1 = tkinter.Text(mensajeframe1, width = 80, height = 26)
    texto1.grid(column = 0, row = 1, sticky = tkinter.W)


    def enviar(*args):
        """Función que destruye la 2 pantalla y crea la tercera, en esta informa de los correos enviados"""
        mensaje = texto1.get(1.0, tkinter.END)
        asunto = asuntoEntry1.get()
        root1.destroy()
        root2 = tkinter.Tk()
        root2.title("Se estan enviando los correos")
        mainframe2 = ttk.Frame(root2, padding = "5 5 5 5")
        mainframe2.grid(row = 0, column = 0, sticky = tkinter.W)
        barra2 = ttk.Progressbar(mainframe2, orient = tkinter.HORIZONTAL,length = 500, mode = 'determinate')
        barra2.grid(row = 0, column = 0)
        c = 1
        for a in lista:
            barra2['value'] += 500/contador
            b = "listasDeCorreo/"
            try:
                a += ".txt"
                b += a
                correo.enviarCorreo(b,"Credenciales.txt",mensaje,asunto)
                ttk.Label(mainframe2, text = "Correos enviados al departamento" + a.replace(".txt","")).grid(column = 0, row = c)
                
            except FileNotFoundError:
                ttk.Label(mainframe2, text = "Error, el archivo " + a + " no existe o esta mal ubicado").grid(column = 0, row = c)
        c += 1
        ttk.Label(mainframe2, text = "Correos enviados").grid(column = 0, row = contador + 1)

    #boton que causa el cambio a la tercera pantalla
    boton1 = ttk.Button(mensajeframe1, text = "Pulsa para enviar el mensaje", command = enviar)
    boton1.grid(row = 2, column = 0, sticky = tkinter.W)
    

    


##PRIMERA PANTALLA
root0 = tkinter.Tk()
root0.title("Elección de los departamentos que reciben el mensaje")
mainframe0 = ttk.Frame(root0, padding="5 5 5 5")
mainframe0.grid(column = 0, row = 0, sticky = tkinter.W)
departamentos = ["Comunicación y empresas","Estructural y dinámica y suspensiones","CFD","Power train petrol","Power train electric","IT","Proyectos","Producción"]
#botones
c0 = tkinter.BooleanVar()
c1 = tkinter.BooleanVar()
c2 = tkinter.BooleanVar()
c3 = tkinter.BooleanVar()
c4 = tkinter.BooleanVar()
c5 = tkinter.BooleanVar()
c6 = tkinter.BooleanVar()
c7 = tkinter.BooleanVar()
C0 = tkinter.Checkbutton(mainframe0, text = departamentos[0], variable = c0)
C0.pack() 
C0.deselect()
C1 = tkinter.Checkbutton(mainframe0, text = departamentos[1], variable = c1)
C1.pack() 
C1.deselect()
C2 = tkinter.Checkbutton(mainframe0, text = departamentos[2], variable = c2)
C2.pack() 
C2.deselect()
C3 = tkinter.Checkbutton(mainframe0, text = departamentos[3], variable = c3)
C3.pack() 
C3.deselect()
C4 = tkinter.Checkbutton(mainframe0, text = departamentos[4], variable = c4)
C4.pack() 
C4.deselect()
C5 = tkinter.Checkbutton(mainframe0, text = departamentos[5], variable = c5)
C5.pack() 
C5.deselect()
C6 = tkinter.Checkbutton(mainframe0, text = departamentos[6], variable = c6)
C6.pack() 
C6.deselect()
C7 = tkinter.Checkbutton(mainframe0, text = departamentos[7], variable = c7)
C7.pack() 
C7.deselect()
#botón que causa el cambio a la segunda pantalla
boton0 = ttk.Button(mainframe0, text = "Fijar elección", command = fijar)
boton0.pack()
root0.resizable(width = True, height = True)
root0.mainloop() #se lanza la interfaz