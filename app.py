from tkinter import *
from PIL import Image, ImageTk
from random import randint

#main window
root = Tk()
root.title("Rock Paper Scissors")
root.configure(background="light green")


#images
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissors_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))

rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissors_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

#insert images
user_label = Label(root,image=rock_img,bg="light green")
comp_label = Label(root,image=rock_img_comp,bg="light green")

comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

#scores
playerScore = Label(root,text=0,font=100,bg="light green",fg="white")
compScore = Label(root,text=0,font=100,bg="light green",fg="white")
compScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

#indicatiors
user_idicator = Label(root,font=50,text="USER",bg="light green").grid(row=0,column=3)
comp_idicator = Label(root,font=50,text="COMPUTER",bg="light green").grid(row=0,column=1)

#upd user score
def updUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)


#upd computer score
def updCompScore():
    score = int(compScore["text"])
    score += 1
    compScore["text"] = str(score)
    
#check winner
def checkWin(player, comp):
    if player == comp:
        pass
    elif player == "rock":
        if comp == "paper":
            updCompScore()
        else:
            updUserScore()
    elif player == "paper":
        if comp == "scissors":
            updCompScore()
        else:
            updUserScore()
    elif player == "scissors":
        if comp == "rock":
            updCompScore()
        else:
            updUserScore()

#udate choices
choices = ["rock", "paper", "sccissors"]

def updateChoice(x):
    #for comp
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissors_img_comp)

     #for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    elif x=="scissors":
        user_label.configure(image=scissors_img)
    checkWin(x, compChoice)

#buttons
rock = Button(root,width=20,height=2,text="ROCK", bg="#FF3E4D",fg="white",command=lambda:updateChoice("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="paper", bg="#FAD02E",fg="white",command=lambda:updateChoice("paper")).grid(row=2,column=2)
scissors = Button(root,width=20,height=2,text="SCISSORS", bg="#0ABDE3",fg="white",command=lambda:updateChoice("scissors")).grid(row=2,column=3)

root.mainloop()