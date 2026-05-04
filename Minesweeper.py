import tkinter as tk
import random
import time

root=tk.Tk()
root.title("Minesweeper")
buttons={}
btn_list=[]
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
            btn.bind("<Button-3>", lambda event, r=row, c=col: on_right_click(event, r, c))
            btn_list.append((row, col))
    btn=tk.Button(root, text="Restart", command=start)

    btn.grid(row=8, column=1, columnspan=4)
    btn=tk.Button(root, text="Exit", command=root.destroy)
    btn.grid(row=8, column=2, columnspan=4)


def random_bomb(exclude=None):
    global bomb_coords
    bomb_coords = []

    count=0
    while count<15:
        BombXcoord=random.randint(0,7)
        BombYcoord=random.randint(0,7)
        
        if (BombXcoord, BombYcoord) != exclude and (BombXcoord, BombYcoord) not in bomb_coords:
            bomb_coords.append((BombXcoord, BombYcoord))
            count+=1
    
    for bomb_coord in bomb_coords:
        if bomb_coord in btn_list:
            btn_list.remove(bomb_coord)

def bomb():

    for (BombXcoord, BombYcoord) in bomb_coords:
        buttons[(BombXcoord, BombYcoord)].config(text="💣",bg="red")
        global btn_list
        if (BombXcoord, BombYcoord) in btn_list:
            btn_list.remove((BombXcoord, BombYcoord))
    for row in range(8):
        for col in range(8):
            if (row, col) not in bomb_coords:
                buttons[(row, col)].config(text="DEFEAT",bg="red")

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
        random_bomb(exclude=(row, col))
        AssignNumbers()

    if (row, col) in bomb_coords:
        bomb()
        return

    if (row, col) not in bomb_coords:
        buttons[(row, col)].config(bg="green",text=str(buttons[(row, col)].touch))
        global btn_list
        if (row, col) in btn_list:
            btn_list.remove((row, col))
        if len(btn_list) == 0:
            for row in range(8):
                for col in range(8):
                    buttons[(row, col)].config(text='YOU WIN',bg="green")
        
        def reveal_adjacent(row, col):
            try:
                if buttons[(row+1,col)].touch == 0 and (row+1, col) not in bomb_coords:
                    buttons[(row+1, col)].config(bg="green",text="0")
                    if (row+1, col) in btn_list:
                        btn_list.remove((row+1, col))
                elif buttons[(row+1,col)].touch > 0 and (row+1, col) not in bomb_coords:
                    if (row+1, col) in btn_list:
                        btn_list.remove((row+1, col))
                    buttons[(row+1, col)].config(bg="green",text=str(buttons[(row+1, col)].touch))
            except KeyError:
                pass
            try:
                if buttons[(row-1,col)].touch == 0 and (row-1, col) not in bomb_coords:
                    buttons[(row-1, col)].config(bg="green",text="0")
                    if (row-1, col) in btn_list:
                        btn_list.remove((row-1, col))
                elif buttons[(row-1,col)].touch > 0 and (row-1, col) not in bomb_coords:
                    if (row-1, col) in btn_list:
                        btn_list.remove((row-1, col))
                    buttons[(row-1, col)].config(bg="green",text=str(buttons[(row-1, col)].touch))
            except KeyError:
                pass
            try:
                if buttons[(row,col+1)].touch == 0 and (row, col+1) not in bomb_coords:
                    buttons[(row, col+1)].config(bg="green",text="0")
                    if (row, col+1) in btn_list:
                        btn_list.remove((row, col+1))
                elif buttons[(row,col+1)].touch > 0 and (row, col+1) not in bomb_coords:
                    if (row, col+1) in btn_list:
                        btn_list.remove((row, col+1))
                    buttons[(row, col+1)].config(bg="green",text=str(buttons[(row, col+1)].touch))
            except KeyError:
                pass
            try:
                if buttons[(row,col-1)].touch == 0 and (row, col-1) not in bomb_coords:
                    if (row, col-1) in btn_list:
                        btn_list.remove((row, col-1))
                    buttons[(row, col-1)].config(bg="green",text="0")
                elif buttons[(row,col-1)].touch > 0 and (row, col-1) not in bomb_coords:
                    if (row, col-1) in btn_list:
                        btn_list.remove((row, col-1))
                    buttons[(row, col-1)].config(bg="green",text=str(buttons[(row, col-1)].touch))
            except KeyError:
                pass
            try:
                if buttons[(row+1,col+1)].touch == 0 and (row+1, col+1) not in bomb_coords:
                    buttons[(row+1, col+1)].config(bg="green",text="0")
                    if (row+1, col+1) in btn_list:
                        btn_list.remove((row+1, col+1))
                elif buttons[(row+1,col+1)].touch > 0 and (row+1, col+1) not in bomb_coords:
                    if (row+1, col+1) in btn_list:
                        btn_list.remove((row+1, col+1))
                    buttons[(row+1, col+1)].config(bg="green",text=str(buttons[(row+1, col+1)].touch))
            except KeyError:
                pass
            try:
                if buttons[(row-1,col-1)].touch == 0 and (row-1, col-1) not in bomb_coords:
                    if (row-1, col-1) in btn_list:
                        btn_list.remove((row-1, col-1))
                    buttons[(row-1, col-1)].config(bg="green",text="0")
                elif buttons[(row-1,col-1)].touch > 0 and (row-1, col-1) not in bomb_coords:
                    if (row-1, col-1) in btn_list:
                        btn_list.remove((row-1, col-1))
                    buttons[(row-1, col-1)].config(bg="green",text=str(buttons[(row-1, col-1)].touch))
            except KeyError:
                pass
            try:
                if buttons[(row+1,col-1)].touch == 0 and (row+1, col-1) not in bomb_coords:
                    if (row+1, col-1) in btn_list:
                        btn_list.remove((row+1, col-1))
                    buttons[(row+1, col-1)].config(bg="green",text="0")
                elif buttons[(row+1,col-1)].touch > 0 and (row+1, col-1) not in bomb_coords:
                    if (row+1, col-1) in btn_list:
                        btn_list.remove((row+1, col-1))
                    buttons[(row+1, col-1)].config(bg="green",text=str(buttons[(row+1, col-1)].touch))
            except KeyError:
                pass
            try:
                if buttons[(row-1,col+1)].touch == 0 and (row-1, col+1) not in bomb_coords:
                    if (row-1, col+1) in btn_list:
                        btn_list.remove((row-1, col+1))
                    buttons[(row-1, col+1)].config(bg="green",text="0")
                elif buttons[(row-1,col+1)].touch > 0 and (row-1, col+1) not in bomb_coords:
                    if (row-1, col+1) in btn_list:
                        btn_list.remove((row-1, col+1))
                    buttons[(row-1, col+1)].config(bg="green",text=str(buttons[(row-1, col+1)].touch))
            except KeyError:
                pass
        if buttons[(row, col)].touch == 0:
            reveal_adjacent(row, col)
            btn_list.remove((row, col))

def on_right_click(event, row, col):
    button = buttons[(row, col)]
    if button.cget("text") == "":
        button.config(text="🚩")
    elif button.cget("text") == "🚩":
        button.config(text="")


start()



root.mainloop()
