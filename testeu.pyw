from random import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from os import *
import os
from tkinter import simpledialog


score = 0
score_ordi = 0

def click_pierre():
    global score, score_ordi, pierre, feuille, ciseaux

    coup_label.configure(image=pierre)

    coup_list = [pierre, feuille, ciseaux]
    coup_ordi = choice(coup_list)

    if coup_ordi == pierre:
        coup_ordi_label.configure(image=pierre)
    elif coup_ordi == feuille:
        coup_ordi_label.configure(image=feuille)
    else:
        coup_ordi == ciseaux
        coup_ordi_label.configure(image=ciseaux)

    if coup_ordi == ciseaux:
        score += 1
        score_ordi += 0
    elif coup_ordi == pierre:
        score_ordi += 0
        score += 0
    else:
        score += 0
        score_ordi += 1

    score_entry.delete(0, END)
    score_entry.insert(0, score)
    score_ordi_entry.delete(0, END)
    score_ordi_entry.insert(0, score_ordi)

    if score >= 10 and score_ordi_entry == 0:
        message = messagebox.askyesno(
            title="Info message", message="Vous Avez Gagné De Plate Couture !\n Voulez Vous recommencez")
        if message == True:
            message
            restart()
        else:
            quit()
    elif score >= 10 and score_ordi < 10:
        message = messagebox.askyesno(
            title="Info message", message="Vous Avez Gagné !\n Voulez Vous recommencez")
        if message == True:
            message
            restart()
        else:
            quit()
    elif score < 10 and score_ordi >= 10:
        message = messagebox.askyesno(
            title="Info message", message="Vous Avez Perdu !\n Voulez Vous recommencez")
        if message == True:
            message
            restart()
        else:
            quit()

def click_feuille():
    global score, score_ordi, pierre, feuille, ciseaux

    coup_label.configure(image=feuille)

    coup_list = [pierre, feuille, ciseaux]
    coup_ordi = choice(coup_list)
    if coup_ordi == pierre:
        coup_ordi_label.configure(image=pierre)
    elif coup_ordi == feuille:
        coup_ordi_label.configure(image=feuille)
    else:
        coup_ordi == ciseaux
        coup_ordi_label.configure(image=ciseaux)

    if coup_ordi == pierre:
        score += 1
        score_ordi += 0
    elif coup_ordi == feuille:
        score_ordi += 0
        score += 0
    else:
        score += 0
        score_ordi += 1
    score_entry.delete(0, END)
    score_entry.insert(0, score)
    score_ordi_entry.delete(0, END)
    score_ordi_entry.insert(0, score_ordi)
    if score >= 10 and score_ordi_entry == 0:
        message = messagebox.askyesno(
            title="Info message", message="Vous Avez Gagné De Plate Couture !\n Voulez Vous recommencez")
        if message == True:
            message
            restart()
        else:
            quit()
    elif score >= 10 and score_ordi < 10:
        message = messagebox.askyesno(
            title="Info message", message="Vous Avez Gagné !\n Voulez Vous recommencez")
        if message == True:
            message
            restart()
        else:
            quit()
    elif score < 10 and score_ordi >= 10:
        message = messagebox.askyesno(
            title="Info message", message="Vous Avez Perdu !\n Voulez Vous recommencez")
        if message == True:
            message
            restart()
        else:
            quit()

def click_ciseaux():
    global score, score_ordi, pierre, feuille, ciseaux

    coup_label.configure(image=ciseaux)

    coup_list = [pierre, feuille, ciseaux]
    coup_ordi = choice(coup_list)
    if coup_ordi == pierre:
        coup_ordi_label.configure(image=pierre)
    elif coup_ordi == feuille:
        coup_ordi_label.configure(image=feuille)
    else:
        coup_ordi == ciseaux
        coup_ordi_label.configure(image=ciseaux)

    if coup_ordi == feuille:
        score += 1
        score_ordi += 0
    elif coup_ordi == ciseaux:
        score_ordi += 0
        score += 0
    else:
        score += 0
        score_ordi += 1

    score_entry.delete(0, END)
    score_entry.insert(0, score)
    score_ordi_entry.delete(0, END)
    score_ordi_entry.insert(0, score_ordi)

    if score >= 10 and score_ordi_entry == 0:
        message = messagebox.askyesno(
            title="Info message", message="Vous Avez Gagné De Plate Couture !\n Voulez Vous recommencez")
        if message == True:
            message
            restart()
        else:
            quit()
    elif score >= 10 and score_ordi < 10:
        message = messagebox.askyesno(
            title="Info message", message="Vous Avez Gagné !\n Voulez Vous recommencez")
        if message == True:
            message
            restart()
        else:
            quit()
    elif score < 10 and score_ordi >= 10:
        message = messagebox.askyesno(
            title="Info message", message="Vous Avez Perdu !\n Voulez Vous recommencez")
        if message == True:
            message
            restart()
        else:
            quit()

def quit():
    root.destroy()
    
def restart():
    global score, score_ordi
    score = 0
    score_ordi = 0
    score_entry.delete(0, END)
    score_entry.insert(0, 0)
    score_ordi_entry.delete(0, END)
    score_ordi_entry.insert(0, 0)

root = Tk()
root.title("testeuu")
root.geometry("850x650")
root.config(bg="lightblue")

# images
pierre = PhotoImage(file="images/pierre.png")
feuille = PhotoImage(file="images/feuille.png")
ciseaux = PhotoImage(file="images/ciseaux.png")
vide = PhotoImage(file="images/vide.png")

speudo = simpledialog.askstring("Speudo :", "                Quel est vôtre speudo                   ",parent=root)
if speudo is not None:
    print("Your speudo is ", speudo)

first_label = Label(root, text=speudo, font="helvetica 14", bg="lightblue")
first_label.grid(row=2, column=2)

score_label = Label(root, text="Score", font="helvetica", bg="lightblue")
score_label.grid(row=0, column=2)

score_entry = Entry(root, font="helvetica", width=2,
                    border=0, bd=0, bg="lightblue")
score_entry.grid(row=1, column=2, padx=50)
score_entry.insert(0, 0)

score_ordi_label = Label(root, text="Score", font="helvetica", bg="lightblue")
score_ordi_label.grid(row=0, column=4)

score_ordi_entry = Entry(root, font="helvetica", width=2, bd=0, bg="lightblue")
score_ordi_entry.grid(row=1, column=4)
score_ordi_entry.insert(0, 0)

coup_label = Label(root)
coup_label.configure(image=vide)
coup_label.grid(row=3, column=2, padx=50, pady=25)

second_label = Label(root, text="VS", font="helvetica", bg="lightblue")
second_label.grid(row=3, column=3)

ordi_label = Label(root, text="Ordi", font="helvetica 14", bg="lightblue")
ordi_label.grid(row=2, column=4)

coup_ordi_label = Label(root)
coup_ordi_label.configure(image=vide)
coup_ordi_label.grid(row=3, column=4, padx=50, pady=25)

p_button = Button(root, command=click_pierre)
p_button.configure(image=pierre)
p_button.grid(row=4, column=2)

f_button = Button(root, command=click_feuille)
f_button.configure(image=feuille)
f_button.grid(row=4, column=3)

c_button = Button(root, command=click_ciseaux)
c_button.configure(image=ciseaux)
c_button.grid(row=4, column=4)

restart_button = Button(root, text="Restart", font="helvetica 14",
                        bg="red", fg="white", command=restart)
restart_button.grid(row=5, column=2, pady=30)

quit_button = Button(root, text="Quit Game", font="helvetica 14",
                     bg="purple", fg="white", command=quit)
quit_button.grid(row=5, column=4, pady=30)

copyright = Label(root, text="Created by Exarven",font="helvetica 14", bg="lightblue",fg= "black")
copyright.grid(row=6, column=3, pady=30)

root.mainloop()