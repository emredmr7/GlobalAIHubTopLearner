import random
from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox

diceRoll = Tk()
diceRoll.title("Dice Rolling Simulator")
diceRoll.geometry("850x450+300+150")

def randomSelection():
    dice = ["C://Users//Emre//Desktop//Dice Rolling Simulator//img//dice1.png", "C://Users//Emre//Desktop//Dice Rolling Simulator//img//dice2.png",
            "C://Users//Emre//Desktop//Dice Rolling Simulator//img//dice3.png", "C://Users//Emre//Desktop//Dice Rolling Simulator//img//dice4.png",
            "C://Users//Emre//Desktop//Dice Rolling Simulator//img//dice5.png", "C://Users//Emre//Desktop//Dice Rolling Simulator//img//dice6.png"]
    
    global takeNum
    
    takeNum = int(answer.get())

    global show, show2, show3

    if takeNum == 1:
        pics = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        show = Label(diceRoll, image = pics)
        show.pack()
        show.place(x = 300, y = 100)

        show.configure(image = pics)
        show.image = pics
        rollingButton['state'] = DISABLED

    elif takeNum == 2:
        pics = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        show = Label(diceRoll, image = pics)
        show.pack()
        show.place(x = 190, y = 100)

        show.configure(image = pics)
        show.image = pics

        pics2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        show2 = Label(diceRoll, image = pics2)
        show2.pack()
        show2.place(x = 420, y = 100)

        show2.configure(image = pics2)
        show2.image = pics2
        rollingButton['state'] = DISABLED

    elif takeNum == 3:
        pics = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        show = Label(diceRoll, image = pics)
        show.pack()
        show.place(x = 90, y = 100)

        show.configure(image = pics)
        show.image = pics

        pics2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        show2 = Label(diceRoll, image = pics2)
        show2.pack()
        show2.place(x = 320, y = 100)

        show2.configure(image = pics2)
        show2.image = pics2

        pics3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        show3 = Label(diceRoll, image = pics3)
        show3.pack()
        show3.place(x = 540, y = 100)

        show3.configure(image = pics3)
        show3.image = pics3
        rollingButton['state'] = DISABLED

def quit():
    msg = messagebox.askquestion("Exit from Dice Rolling Simulator","Are you sure you want to quit?")
    if msg == "yes":
        diceRoll.destroy()
    else:
        messagebox.showinfo("Return to Dice Rolling Simulator","You will return the simulator.")

def clearWindow():
    if takeNum == 1:
        show.destroy()
        rollingButton['state'] = NORMAL
    elif takeNum == 2:
        show.destroy()
        rollingButton['state'] = NORMAL        
        show2.destroy()
        rollingButton['state'] = NORMAL
    elif takeNum == 3:
        show.destroy()
        rollingButton['state'] = NORMAL        
        show2.destroy()
        rollingButton['state'] = NORMAL
        show3.destroy()
        rollingButton['state'] = NORMAL 
# End of the function.


question = Label(diceRoll, text = "HOW MANY DICE DO YOU WANT TO USE ? (MIN 1 AND MAX 3)",
                fg = "black",
                font = "arial 10 bold")
question.place(x = 230, y = 10)

answer = Entry(diceRoll)
answer.place(x = 350, y = 40)

# Dice Rolling Button.
rollingButton = Button(diceRoll, text = "ROLL IT !", command = randomSelection,
                bg = "green", 
                fg = "white",
                width = 20,
                height = 3
                )

rollingButton.place(x = 200, y = 350)

# Clear Button
clearButton = Button(diceRoll, text = "CLEAR", command= clearWindow,
                     bg = "blue",
                     fg = "white",
                     width = 20,
                     height = 3
                     )
clearButton.place(x = 350, y= 350)
# Button for Exit to program.

exitButton = Button(diceRoll, text = "EXIT", command = quit,
                    bg = "red",
                    fg = "white",
                    width = 20,
                    height = 3
                    )

exitButton.place(x = 500 , y = 350)

diceRoll.mainloop()
