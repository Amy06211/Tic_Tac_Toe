from tkinter import *
import tkinter.messagebox

board=Tk()
frame=Frame(board, bg='black', width=225, height=225)
frame.pack(padx=2, pady=2)
board.configure(bg='#00BFA5')

bclick=True
flag=0

def disablebutton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)
def btn_click(button):
    global bclick, flag
    if button['text']=="" and bclick==True:
        button['text']='X'
        button['fg']='#F50057'
        bclick=False
        check_for_win()
        flag+=1
    elif button['text']=="" and bclick==False:
        button['text']='O'
        bclick=True
        check_for_win()
        flag+=1 
    else:
        tkinter.messagebox.showinfo('Tic_Tac_Toe', "Button already clicked")           
def check_for_win():
    if(button1['text']=='X' and button2['text']=='X' and button3['text']=='X' or
        button4['text']=='X' and button5['text']=='X' and button6['text']=='X' or
        button7['text']=='X' and button8['text']=='X' and button9['text']=='X' or
        button1['text']=='X' and button4['text']=='X' and button7['text']=='X' or
        button2['text']=='X' and button5['text']=='X' and button8['text']=='X' or
        button3['text']=='X' and button6['text']=='X' and button9['text']=='X' or
        button1['text']=='X' and button5['text']=='X' and button9['text']=='X' or
        button3['text']=='X' and button5['text']=='X' and button7['text']=='X'):
        disablebutton()
        tkinter.messagebox.showinfo("Tic_Tac_Toe","player1_win!")

    elif(button1['text']=='O' and button2['text']=='O' and button3['text']=='O' or
        button4['text']=='O' and button5['text']=='O' and button6['text']=='O' or
        button7['text']=='O' and button8['text']=='O' and button9['text']=='O' or
        button1['text']=='O' and button4['text']=='O' and button7['text']=='O' or
        button2['text']=='O' and button5['text']=='O' and button8['text']=='O' or
        button3['text']=='O' and button6['text']=='O' and button9['text']=='O' or
        button1['text']=='O' and button5['text']=='O' and button9['text']=='O' or
        button3['text']=='O' and button5['text']=='O' and button7['text']=='O'):
        disablebutton()
        tkinter.messagebox.showinfo("Tic_Tac_Toe","player2_win!")
    elif flag==8:
        tkinter.messagebox.showinfo("Tic_Tac_Toe", "It is a tie")



button1=Button(frame, text='', font='Times 20 bold', bg='black', fg='#00BFA5', height=4, width=8, command=lambda: btn_click(button1))
button1.grid(row=0, column=0)
button2=Button(frame, text='', font='Times 20 bold', bg='black', fg='#00BFA5', height=4, width=8, command=lambda: btn_click(button2))
button2.grid(row=0, column=1)
button3=Button(frame, text='', font='Times 20 bold', bg='black', fg='#00BFA5', height=4, width=8, command=lambda: btn_click(button3))
button3.grid(row=0, column=2)
button4=Button(frame, text='', font='Times 20 bold', bg='black', fg='#00BFA5', height=4, width=8, command=lambda: btn_click(button4))
button4.grid(row=1, column=0)
button5=Button(frame, text='', font='Times 20 bold', bg='black', fg='#00BFA5', height=4, width=8, command=lambda: btn_click(button5))
button5.grid(row=1, column=1)
button6=Button(frame, text='', font='Times 20 bold', bg='black', fg='#00BFA5', height=4, width=8, command=lambda: btn_click(button6))
button6.grid(row=1, column=2)
button7=Button(frame, text='', font='Times 20 bold', bg='black', fg='#00BFA5', height=4, width=8, command=lambda: btn_click(button7))
button7.grid(row=2, column=0)
button8=Button(frame, text='', font='Times 20 bold', bg='black', fg='#00BFA5', height=4, width=8, command=lambda: btn_click(button8))
button8.grid(row=2, column=1)
button9=Button(frame, text='', font='Times 20 bold', bg='black', fg='#00BFA5', height=4, width=8, command=lambda: btn_click(button9))
button9.grid(row=2, column=2)


board.mainloop()
