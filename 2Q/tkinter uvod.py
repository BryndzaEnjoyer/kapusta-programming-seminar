import tkinter as tk
import random as rd





def karta(platno, c, b):
    x=210*c
    y=b*310
    platno.pack()
    platno.create_rectangle (10+x, 10+y, 210+x, 310+y, fill='white', outline='black', width=3)
    platno.create_oval (20+x, 20+y, 80+x, 80+y, fill=color)
    platno.create_oval (140+x, 240+y, 200+x, 300+y, fill=color)
    platno.create_text (50+x, 50+y, text=num, font='arial 25', fill='black')
    platno.create_text (170+x, 270+y, text=num, font='arial 25', fill='black')
    platno.create_rectangle (35+x,125+y,185+x,195+y, fill='black')
    platno.create_text (110+x, 160+y, text='BILGYM', font='arial 25', fill=color)

def karty():
    colors=["blue","red","yellow","purple","pink","green"] 
    platno = tk.Canvas(width = 5000, height = 5000, bg = 'gray')   
    for c in range(5):
        color = rd.choice(colors)
        num = rd.randint(2,10)
        karta(platno, c, 0)

    for c in range(5):
        color = input("color")
        num = int(input("num"))
        karta(platno, c, 1)

    platno.mainloop ()
def nič():
    platno = tk.Canvas (width = 1000, height = 400, bg='silver')
    platno.pack()
    platno.create_polygon (100, 100, 200, 100, 100, 200, width=3, fill='red')
    platno.create_polygon (200, 100, 300, 100, 200, 200, width=3, fill='green')
    farby = ['red', 'yellow', 'green', 'blue', 'cyan', 'purple', 'white', 'black']
    for i in range (10):
        r=("%02x"%rd.randint(0,255))
        g=("%02x"%rd.randint(0,255))
        b=("%02x"%rd.randint(0,255))
        predpona="#"
        #moja_farba=predpona+r+g+b;
        moja_farba = rd.choice (farby)
        platno.create_polygon (i*100, 250, i*100+100, 250, i*100, 350, width=3, fill=moja_farba)
    platno.mainloop () 

def clear(root):
    root.create_rectangle(0,0,500,800, fill='white',)
    
import tkinter as tk
import random as rd

def clear(root):
    root.create_rectangle(0, 0, 500, 600, fill='white')
    gen(root)

def baloon(root, farby):
    s = rd.randint(30, 60)
    y = rd.randint(0, 600)
    x = rd.randint(0, 500)
    color = rd.choice(farby)

    root.create_oval(x, y, x+s, y+s*3/2, fill=color)
    root.create_rectangle(x+s/2-1,  y+s*3/2, x+s/2+1, y+4*s, fill="black")
    
    gen(root)



def sviecka(root, farby):
    # náhodné rozmery sviečky
    w = rd.randint(20, 50)   # šírka
    h = rd.randint(30, 70)   # výška

    # náhodná pozícia
    x = rd.randint(0, 500 - w)
    y = rd.randint(0, 800 - h)

    # náhodná farba sviečky
    
    color = rd.choice(farby)

    # nakreslenie tela sviečky
    root.create_rectangle(x, y, x + w, y + h, fill=color, outline='black')

    # veľkosť plameňa
    flame_h = w                    # výška plameňa = šírka sviečky
    flame_w = w * 0.6              # šírka plameňa (môžeš meniť)

    # stred sviečky
    mid = x + w/2

    # plameň
    root.create_oval(mid - flame_w/2,
                     y - flame_h,
                     mid + flame_w/2,
                     y,
                     fill="orange",
                     outline="red")

    # knôt (tretina plameňa)
    knot_h = flame_h / 3

    root.create_line(mid, y, mid, y - knot_h, fill="black", width=2)
    gen(root)



def gen(root):
    farby = ['red', 'yellow', 'green', 'blue', 'cyan', 'purple', 'white', 'black']

    root.create_rectangle(0, 800, 500, 600, fill='Grey')

    button1 = tk.Button(text="Clear", command=lambda: clear(root))
    button1.place(x=10, y=610)

    button2 = tk.Button(text="Baloon", command=lambda: baloon(root, farby))
    button2.place(x=10, y=660)
    button3 = tk.Button(text="Sviečka", command=lambda: sviecka(root, farby))
    button3.place(x=10, y=710)

 

def pozdrav():
    root = tk.Canvas(width=500, height=800)
    root.pack()

    gen(root)
    root.mainloop()

pozdrav()
