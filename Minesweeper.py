import tkinter as tk
import random
import time


root=tk.Tk()
root.title("Minesweeper")
buttons={}

def start():
    global turn_count
    turn_count=0
    for row in range(8):
        for col in range(8):
            btn=tk.Button(
                root,
                width=4,
                height=2,
                command=lambda r=row, c=col: on_button_click(r, c),
                

            )
            btn.touch=0
            btn.grid(row=row, column=col)
            buttons[(row, col)] = btn
    btn=tk.Button(root, text="Restart", command=start)
    btn.grid(row=8, column=1, columnspan=4)
    btn=tk.Button(root, text="Exit", command=root.destroy)
    btn.grid(row=8, column=2, columnspan=4)


def random_bomb():
    global bomb_coords
    bomb_coords = []

    count=0
    while count<15:
        BombXcoord=random.randint(0,7)
        BombYcoord=random.randint(0,7)
        
        if buttons[(BombXcoord,BombYcoord)].cget("command") != str(bomb):
            buttons[(BombXcoord,BombYcoord)].config(command=bomb)
            bomb_coords.append((BombXcoord, BombYcoord))
            count+=1

def bomb():
    for (BombXcoord, BombYcoord) in bomb_coords:
        buttons[(BombXcoord, BombYcoord)].config(text="💣",bg="red")


def AssignNumbers():
    touch=0
    for i in range(8):
        for j in range(8):
            if (i,j) not in bomb_coords:
                if (i+1,j) in bomb_coords:
                    touch+=1
                if (i-1,j) in bomb_coords:
                    touch+=1
                if (i,j+1) in bomb_coords:
                    touch+=1
                if (i,j-1) in bomb_coords:
                    touch+=1
                if (i+1,j+1) in bomb_coords:
                    touch+=1
                if (i-1,j-1) in bomb_coords:
                    touch+=1
                if (i+1,j-1) in bomb_coords:
                    touch+=1
                if (i-1,j+1) in bomb_coords:
                    touch+=1
                buttons[(i,j)].touch=touch
                touch=0

def on_button_click(row, col):
    global turn_count
    turn_count += 1
    if turn_count == 1:
        random_bomb()
        AssignNumbers()


    if (row, col) not in bomb_coords:
        buttons[(row, col)].config(bg="green",text=str(buttons[(row, col)].touch))
        if buttons[(row, col)].touch == 0:
            try:
                if buttons[(row+1,col)].touch == 0:
                    buttons[(row+1, col)].config(bg="green",text="0")
            except KeyError:
                pass
            try:
                if buttons[(row-1,col)].touch == 0:
                    buttons[(row-1, col)].config(bg="green",text="0")
            except KeyError:
                pass
            try:
                if buttons[(row,col+1)].touch == 0:
                    buttons[(row, col+1)].config(bg="green",text="0")
            except KeyError:
                pass
            try:
                if buttons[(row,col-1)].touch == 0:
                    buttons[(row, col-1)].config(bg="green",text="0")
            except KeyError:
                pass
            try:
                if buttons[(row+1,col+1)].touch == 0:
                    buttons[(row+1, col+1)].config(bg="green",text="0")
            except KeyError:
                pass
            try:
                if buttons[(row-1,col-1)].touch == 0:
                    buttons[(row-1, col-1)].config(bg="green",text="0")
            except KeyError:
                pass
            try:
                if buttons[(row+1,col-1)].touch == 0:
                    buttons[(row+1, col-1)].config(bg="green",text="0")
            except KeyError:
                pass
            try:
                if buttons[(row-1,col+1)].touch == 0:
                    buttons[(row-1, col+1)].config(bg="green",text="0")
            except KeyError:
                pass


start()
root.mainloop()