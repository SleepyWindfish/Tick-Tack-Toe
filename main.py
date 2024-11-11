from tkinter import *
from tkinter import messagebox
count=0
board=[["","",""],["","",""],["","",""]]

global root
root=Tk()
root.title("TIC TACK TOE")
root.configure(bg="white")

"""l1=Label(root,text="Player: 1(X)",height=3,font=("Cosmic Sans MS",10,"bold"))
exitButton.grid(row=0,column=0)"""


def safety_net():
  fwd=messagebox.askquestion("Quit","Are you Sure You want to quit?")
  if(fwd=="yes"):
    destruct()


def destruct():
  global root
  root.destroy

def displayWinner(winner):
  wt=messagebox.showinfo("Results",winner)
  if(wt=="okay"):
    gone()
  
  
  



def cheack_Winner():
  global count,board
  if(board==[0][0]==board[0][1]==board[0][2]=="X" or board[1][0]==board[1][1]==board[1][2]=="X" or
     board[2][0]==board[2][1]==board[2][2]=="X" or
        board[0][0]==board[1][0]==board[2][0]=="X" or board[0][1]==board[1][1]==board[2][1]=="X" or 
        board[0][2]==board[1][2]==board[2][2]=="X" or
        board[0][0]==board[1][1]==board[2][2]=="X" or board[0][2]==board[1][1]==board[2][0]=="X"):
            displayWinner("Congradulations to Player X")
  elif (board[0][0]==board[0][1]==board[0][2]=="O" or board[1][0]==board[1][1]==board[1][2]=="O" or board[2][0]==board[2][1]==board[2][2]=="O" or board[0][0]==board[1][0]==board[2][0]=="O" or board[0][1]==board[1][1]==board[2][1]=="O" or board[0][2]==board[1][2]==board[2][2]=="O" or board[0][0]==board[1][1]==board[2][2]=="O" or board[0][2]==board[1][1]==board[2][0]=="O"):
      displayWinner("Congradulations to Player O")
  else:
    displayWinner("Its a Tie!")
  



def change_val(button,BoardValRow,BoardValColumn):
  global count
  if(button["text"]=="Place"):
    if(count%2==0):
      button["text"]="X"
      board[BoardValRow][BoardValColumn]="X"
    else:
      button["text"]="O"
      board[BoardValRow][BoardValColumn]="O"
    count=count+1
    if(count>=5):
      cheack_Winner()
  else:
    messagebox.showerror("Value_Taken","Choose a box not already taken!")
    
    

def ins():
  messagebox.showinfo("Instructions","Welcome To Tic Tack Toe player 1 is X and Player 2 is O get Letters in a row Verticaly,Horozontaly, or Diagonaly to Win!")
  
ins()  



#Row one
r1_c1=Button(root,text="Place",bg="grey",activeforeground="orange",command=lambda:change_val(r1_c1,0,0))

r1_c2=Button(root,text="Place",bg="grey",activeforeground="orange",command=lambda:change_val(r1_c2,0,1))

r1_c3=Button(root,text="Place",bg="grey",activeforeground="orange",command=lambda:change_val(r1_c3,0,2))


#Row two
r2_c1=Button(root,text="Place",bg="grey",activeforeground="orange",command=lambda:change_val(r2_c1,1,0))

r2_c2=Button(root,text="Place",bg="grey",activeforeground="orange",command=lambda:change_val(r2_c2,1,1))

r2_c3=Button(root,text="Place",bg="grey",activeforeground="orange",command=lambda:change_val(r2_c3,1,2))


#Row three
r3_c1=Button(root,text="Place",bg="grey",activeforeground="orange",command=lambda:change_val(r3_c1,2,0))

r3_c2=Button(root,text="Place",bg="grey",activeforeground="orange",command=lambda:change_val(r3_c2,2,1))

r3_c3=Button(root,text="Place",bg="grey",activeforeground="orange",command=lambda:change_val(r3_c3,2,2))

quit=Button(root,text="Quit",bg="white",activebackground="red",command=safety_net)




r1_c1.grid(row=1,column=1)
r1_c2.grid(row=1,column=2)
r1_c3.grid(row=1,column=3)
r2_c1.grid(row=2,column=1)
r2_c2.grid(row=2,column=2)
r2_c3.grid(row=2,column=3)
r3_c1.grid(row=3,column=1)
r3_c2.grid(row=3,column=2)
r3_c3.grid(row=3,column=3)
quit.grid(row=4,column=4)

root.mainloop()