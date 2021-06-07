from tkinter import *
import tkinter.font as tkFont
import sudokuSolver as suSo
import copy

root = Tk()
root.title("Sudoku Solver")
root.geometry("800x700")
root.maxsize(800,700)
root.minsize(800,700)

# The first window just initializing with title and buttons to solve or exit.

# Title: Sudoku Solver

fontStyleTitle = tkFont.Font(family="Sans-serif",size=110)
mainTitle = Label(root, text="Sudoku Solver", font=fontStyleTitle,fg="#83EDF2")

mainTitle.place(anchor="nw", relx=0.1,rely=0.1)

# Start Button

def start():
    global entry1_1,entry1_2,entry1_3,entry1_4,entry1_5,entry1_6,entry1_7,entry1_8,entry1_9
    global entry2_1,entry2_2,entry2_3,entry2_4,entry2_5,entry2_6,entry2_7,entry2_8,entry2_9
    global entry3_1,entry3_2,entry3_3,entry3_4,entry3_5,entry3_6,entry3_7,entry3_8,entry3_9
    global entry4_1,entry4_2,entry4_3,entry4_4,entry4_5,entry4_6,entry4_7,entry4_8,entry4_9
    global entry5_1,entry5_2,entry5_3,entry5_4,entry5_5,entry5_6,entry5_7,entry5_8,entry5_9
    global entry6_1,entry6_2,entry6_3,entry6_4,entry6_5,entry6_6,entry6_7,entry6_8,entry6_9
    global entry7_1,entry7_2,entry7_3,entry7_4,entry7_5,entry7_6,entry7_7,entry7_8,entry7_9
    global entry8_1,entry8_2,entry8_3,entry8_4,entry8_5,entry8_6,entry8_7,entry8_8,entry8_9
    global entry9_1,entry9_2,entry9_3,entry9_4,entry9_5,entry9_6,entry9_7,entry9_8,entry9_9
    global board


    # Second Window for the solver

    top = Toplevel()
    top.geometry("800x700")
    top.maxsize(800,700)
    top.minsize(800,700)

    canvas = Canvas(top)
    canvas.place(relheight=1.0,relwidth=1.0)

    # Rectangle
    rect = canvas.create_rectangle(50,50,750,600,width=5)

    # Creando el board (son 8 lineas de columnas y 8 lineas de fila)

    # Column Lines
    colLine1 = canvas.create_line((50 + (700/9)*1),50,(50 + (700/9)*1),600)
    colLine2 = canvas.create_line((50 + (700/9)*2),50,(50 + (700/9)*2),600)
    colLine3 = canvas.create_line((50 + (700/9)*3),50,(50 + (700/9)*3),600,width=5)
    colLine4 = canvas.create_line((50 + (700/9)*4),50,(50 + (700/9)*4),600)
    colLine5 = canvas.create_line((50 + (700/9)*5),50,(50 + (700/9)*5),600)
    colLine6 = canvas.create_line((50 + (700/9)*6),50,(50 + (700/9)*6),600,width=5)
    colLine7 = canvas.create_line((50 + (700/9)*7),50,(50 + (700/9)*7),600)
    colLine8 = canvas.create_line((50 + (700/9)*8),50,(50 + (700/9)*8),600)
    colLine9 = canvas.create_line((50 + (700/9)*9),50,(50 + (700/9)*9),600)

    # Row Lines

    rowLine1 = canvas.create_line(50,(50 + (550/9)*1),750,(50 + (550/9)*1))
    rowLine2 = canvas.create_line(50,(50 + (550/9)*2),750,(50 + (550/9)*2))
    rowLine3 = canvas.create_line(50,(50 + (550/9)*3),750,(50 + (550/9)*3),width=5)
    rowLine4 = canvas.create_line(50,(50 + (550/9)*4),750,(50 + (550/9)*4))
    rowLine5 = canvas.create_line(50,(50 + (550/9)*5),750,(50 + (550/9)*5))
    rowLine6 = canvas.create_line(50,(50 + (550/9)*6),750,(50 + (550/9)*6),width=5)
    rowLine7 = canvas.create_line(50,(50 + (550/9)*7),750,(50 + (550/9)*7))
    rowLine8 = canvas.create_line(50,(50 + (550/9)*8),750,(50 + (550/9)*8))
    rowLine9 = canvas.create_line(50,(50 + (550/9)*9),750,(50 + (550/9)*9))

    # Creating the entry for each part of the board

    fontBoardNums = tkFont.Font(family="Sans-serif", size=40)

    # First Row
    entry1_1 = Entry(top,font=fontBoardNums,justify="center")
    entry1_2 = Entry(top,font=fontBoardNums,justify="center")
    entry1_3 = Entry(top,font=fontBoardNums,justify="center")
    entry1_4 = Entry(top,font=fontBoardNums,justify="center")
    entry1_5 = Entry(top,font=fontBoardNums,justify="center")
    entry1_6 = Entry(top,font=fontBoardNums,justify="center")
    entry1_7 = Entry(top,font=fontBoardNums,justify="center")
    entry1_8 = Entry(top,font=fontBoardNums,justify="center")
    entry1_9 = Entry(top,font=fontBoardNums,justify="center")

    entry1_1.place(x=53,y=52,width=((700/9)-3),height=((550/9)-2))
    entry1_2.place(x=51+((700/9)*1),y=52,width=((700/9)-1),height=((550/9)-2))
    entry1_3.place(x=51+((700/9)*2),y=52,width=((700/9)-4),height=((550/9)-2))
    entry1_4.place(x=53+((700/9)*3),y=52,width=((700/9)-3),height=((550/9)-2))
    entry1_5.place(x=51+((700/9)*4),y=52,width=((700/9)-1),height=((550/9)-2))
    entry1_6.place(x=51+((700/9)*5),y=52,width=((700/9)-4),height=((550/9)-2))
    entry1_7.place(x=53+((700/9)*6),y=52,width=((700/9)-5),height=((550/9)-2))
    entry1_8.place(x=53+((700/9)*7),y=52,width=((700/9)-3),height=((550/9)-2))
    entry1_9.place(x=51+((700/9)*8),y=52,width=((700/9)-4),height=((550/9)-2))

    # Row 2

    entry2_1 = Entry(top,font=fontBoardNums,justify="center")
    entry2_2 = Entry(top,font=fontBoardNums,justify="center")
    entry2_3 = Entry(top,font=fontBoardNums,justify="center")
    entry2_4 = Entry(top,font=fontBoardNums,justify="center")
    entry2_5 = Entry(top,font=fontBoardNums,justify="center")
    entry2_6 = Entry(top,font=fontBoardNums,justify="center")
    entry2_7 = Entry(top,font=fontBoardNums,justify="center")
    entry2_8 = Entry(top,font=fontBoardNums,justify="center")
    entry2_9 = Entry(top,font=fontBoardNums,justify="center")

    entry2_1.place(x=53,y=52+((550/9)*1),width=((700/9)-3),height=((550/9)-2))
    entry2_2.place(x=51+((700/9)*1),y=52+((550/9)*1),width=((700/9)-1),height=((550/9)-2))
    entry2_3.place(x=51+((700/9)*2),y=52+((550/9)*1),width=((700/9)-4),height=((550/9)-2))
    entry2_4.place(x=53+((700/9)*3),y=52+((550/9)*1),width=((700/9)-3),height=((550/9)-2))
    entry2_5.place(x=51+((700/9)*4),y=52+((550/9)*1),width=((700/9)-1),height=((550/9)-2))
    entry2_6.place(x=51+((700/9)*5),y=52+((550/9)*1),width=((700/9)-4),height=((550/9)-2))
    entry2_7.place(x=53+((700/9)*6),y=52+((550/9)*1),width=((700/9)-5),height=((550/9)-2))
    entry2_8.place(x=53+((700/9)*7),y=52+((550/9)*1),width=((700/9)-3),height=((550/9)-2))
    entry2_9.place(x=51+((700/9)*8),y=52+((550/9)*1),width=((700/9)-4),height=((550/9)-2))

    # Row 3

    entry3_1 = Entry(top,font=fontBoardNums,justify="center")
    entry3_2 = Entry(top,font=fontBoardNums,justify="center")
    entry3_3 = Entry(top,font=fontBoardNums,justify="center")
    entry3_4 = Entry(top,font=fontBoardNums,justify="center")
    entry3_5 = Entry(top,font=fontBoardNums,justify="center")
    entry3_6 = Entry(top,font=fontBoardNums,justify="center")
    entry3_7 = Entry(top,font=fontBoardNums,justify="center")
    entry3_8 = Entry(top,font=fontBoardNums,justify="center")
    entry3_9 = Entry(top,font=fontBoardNums,justify="center")

    entry3_1.place(x=53,y=52+((550/9)*2),width=((700/9)-3),height=((550/9)-4))
    entry3_2.place(x=51+((700/9)*1),y=52+((550/9)*2),width=((700/9)-1),height=((550/9)-4))
    entry3_3.place(x=51+((700/9)*2),y=52+((550/9)*2),width=((700/9)-4),height=((550/9)-4))
    entry3_4.place(x=53+((700/9)*3),y=52+((550/9)*2),width=((700/9)-3),height=((550/9)-4))
    entry3_5.place(x=51+((700/9)*4),y=52+((550/9)*2),width=((700/9)-1),height=((550/9)-4))
    entry3_6.place(x=51+((700/9)*5),y=52+((550/9)*2),width=((700/9)-4),height=((550/9)-4))
    entry3_7.place(x=53+((700/9)*6),y=52+((550/9)*2),width=((700/9)-5),height=((550/9)-4))
    entry3_8.place(x=53+((700/9)*7),y=52+((550/9)*2),width=((700/9)-3),height=((550/9)-4))
    entry3_9.place(x=51+((700/9)*8),y=52+((550/9)*2),width=((700/9)-4),height=((550/9)-4))

    # Row 4

    entry4_1 = Entry(top,font=fontBoardNums,justify="center")
    entry4_2 = Entry(top,font=fontBoardNums,justify="center")
    entry4_3 = Entry(top,font=fontBoardNums,justify="center")
    entry4_4 = Entry(top,font=fontBoardNums,justify="center")
    entry4_5 = Entry(top,font=fontBoardNums,justify="center")
    entry4_6 = Entry(top,font=fontBoardNums,justify="center")
    entry4_7 = Entry(top,font=fontBoardNums,justify="center")
    entry4_8 = Entry(top,font=fontBoardNums,justify="center")
    entry4_9 = Entry(top,font=fontBoardNums,justify="center")

    entry4_1.place(x=53,y=52+((550/9)*3),width=((700/9)-3),height=((550/9)-2))
    entry4_2.place(x=51+((700/9)*1),y=52+((550/9)*3),width=((700/9)-1),height=((550/9)-2))
    entry4_3.place(x=51+((700/9)*2),y=52+((550/9)*3),width=((700/9)-4),height=((550/9)-2))
    entry4_4.place(x=53+((700/9)*3),y=52+((550/9)*3),width=((700/9)-3),height=((550/9)-2))
    entry4_5.place(x=51+((700/9)*4),y=52+((550/9)*3),width=((700/9)-1),height=((550/9)-2))
    entry4_6.place(x=51+((700/9)*5),y=52+((550/9)*3),width=((700/9)-4),height=((550/9)-2))
    entry4_7.place(x=53+((700/9)*6),y=52+((550/9)*3),width=((700/9)-5),height=((550/9)-2))
    entry4_8.place(x=53+((700/9)*7),y=52+((550/9)*3),width=((700/9)-3),height=((550/9)-2))
    entry4_9.place(x=51+((700/9)*8),y=52+((550/9)*3),width=((700/9)-4),height=((550/9)-2))

    # Row 5

    entry5_1 = Entry(top,font=fontBoardNums,justify="center")
    entry5_2 = Entry(top,font=fontBoardNums,justify="center")
    entry5_3 = Entry(top,font=fontBoardNums,justify="center")
    entry5_4 = Entry(top,font=fontBoardNums,justify="center")
    entry5_5 = Entry(top,font=fontBoardNums,justify="center")
    entry5_6 = Entry(top,font=fontBoardNums,justify="center")
    entry5_7 = Entry(top,font=fontBoardNums,justify="center")
    entry5_8 = Entry(top,font=fontBoardNums,justify="center")
    entry5_9 = Entry(top,font=fontBoardNums,justify="center")

    entry5_1.place(x=53,y=52+((550/9)*4),width=((700/9)-3),height=((550/9)-2))
    entry5_2.place(x=51+((700/9)*1),y=52+((550/9)*4),width=((700/9)-1),height=((550/9)-2))
    entry5_3.place(x=51+((700/9)*2),y=52+((550/9)*4),width=((700/9)-4),height=((550/9)-2))
    entry5_4.place(x=53+((700/9)*3),y=52+((550/9)*4),width=((700/9)-3),height=((550/9)-2))
    entry5_5.place(x=51+((700/9)*4),y=52+((550/9)*4),width=((700/9)-1),height=((550/9)-2))
    entry5_6.place(x=51+((700/9)*5),y=52+((550/9)*4),width=((700/9)-4),height=((550/9)-2))
    entry5_7.place(x=53+((700/9)*6),y=52+((550/9)*4),width=((700/9)-5),height=((550/9)-2))
    entry5_8.place(x=53+((700/9)*7),y=52+((550/9)*4),width=((700/9)-3),height=((550/9)-2))
    entry5_9.place(x=51+((700/9)*8),y=52+((550/9)*4),width=((700/9)-4),height=((550/9)-2))

    # Row 6 

    entry6_1 = Entry(top,font=fontBoardNums,justify="center")
    entry6_2 = Entry(top,font=fontBoardNums,justify="center")
    entry6_3 = Entry(top,font=fontBoardNums,justify="center")
    entry6_4 = Entry(top,font=fontBoardNums,justify="center")
    entry6_5 = Entry(top,font=fontBoardNums,justify="center")
    entry6_6 = Entry(top,font=fontBoardNums,justify="center")
    entry6_7 = Entry(top,font=fontBoardNums,justify="center")
    entry6_8 = Entry(top,font=fontBoardNums,justify="center")
    entry6_9 = Entry(top,font=fontBoardNums,justify="center")

    entry6_1.place(x=53,y=52+((550/9)*5),width=((700/9)-3),height=((550/9)-4))
    entry6_2.place(x=51+((700/9)*1),y=52+((550/9)*5),width=((700/9)-1),height=((550/9)-4))
    entry6_3.place(x=51+((700/9)*2),y=52+((550/9)*5),width=((700/9)-4),height=((550/9)-4))
    entry6_4.place(x=53+((700/9)*3),y=52+((550/9)*5),width=((700/9)-3),height=((550/9)-4))
    entry6_5.place(x=51+((700/9)*4),y=52+((550/9)*5),width=((700/9)-1),height=((550/9)-4))
    entry6_6.place(x=51+((700/9)*5),y=52+((550/9)*5),width=((700/9)-4),height=((550/9)-4))
    entry6_7.place(x=53+((700/9)*6),y=52+((550/9)*5),width=((700/9)-5),height=((550/9)-4))
    entry6_8.place(x=53+((700/9)*7),y=52+((550/9)*5),width=((700/9)-3),height=((550/9)-4))
    entry6_9.place(x=51+((700/9)*8),y=52+((550/9)*5),width=((700/9)-4),height=((550/9)-4))

    # Row 7

    entry7_1 = Entry(top,font=fontBoardNums,justify="center")
    entry7_2 = Entry(top,font=fontBoardNums,justify="center")
    entry7_3 = Entry(top,font=fontBoardNums,justify="center")
    entry7_4 = Entry(top,font=fontBoardNums,justify="center")
    entry7_5 = Entry(top,font=fontBoardNums,justify="center")
    entry7_6 = Entry(top,font=fontBoardNums,justify="center")
    entry7_7 = Entry(top,font=fontBoardNums,justify="center")
    entry7_8 = Entry(top,font=fontBoardNums,justify="center")
    entry7_9 = Entry(top,font=fontBoardNums,justify="center")

    entry7_1.place(x=53,y=52+((550/9)*6),width=((700/9)-3),height=((550/9)-2))
    entry7_2.place(x=51+((700/9)*1),y=52+((550/9)*6),width=((700/9)-1),height=((550/9)-2))
    entry7_3.place(x=51+((700/9)*2),y=52+((550/9)*6),width=((700/9)-4),height=((550/9)-2))
    entry7_4.place(x=53+((700/9)*3),y=52+((550/9)*6),width=((700/9)-3),height=((550/9)-2))
    entry7_5.place(x=51+((700/9)*4),y=52+((550/9)*6),width=((700/9)-1),height=((550/9)-2))
    entry7_6.place(x=51+((700/9)*5),y=52+((550/9)*6),width=((700/9)-4),height=((550/9)-2))
    entry7_7.place(x=53+((700/9)*6),y=52+((550/9)*6),width=((700/9)-5),height=((550/9)-2))
    entry7_8.place(x=53+((700/9)*7),y=52+((550/9)*6),width=((700/9)-3),height=((550/9)-2))
    entry7_9.place(x=51+((700/9)*8),y=52+((550/9)*6),width=((700/9)-4),height=((550/9)-2))

    # Row 8

    entry8_1 = Entry(top,font=fontBoardNums,justify="center")
    entry8_2 = Entry(top,font=fontBoardNums,justify="center")
    entry8_3 = Entry(top,font=fontBoardNums,justify="center")
    entry8_4 = Entry(top,font=fontBoardNums,justify="center")
    entry8_5 = Entry(top,font=fontBoardNums,justify="center")
    entry8_6 = Entry(top,font=fontBoardNums,justify="center")
    entry8_7 = Entry(top,font=fontBoardNums,justify="center")
    entry8_8 = Entry(top,font=fontBoardNums,justify="center")
    entry8_9 = Entry(top,font=fontBoardNums,justify="center")

    entry8_1.place(x=53,y=52+((550/9)*7),width=((700/9)-3),height=((550/9)-2))
    entry8_2.place(x=51+((700/9)*1),y=52+((550/9)*7),width=((700/9)-1),height=((550/9)-2))
    entry8_3.place(x=51+((700/9)*2),y=52+((550/9)*7),width=((700/9)-4),height=((550/9)-2))
    entry8_4.place(x=53+((700/9)*3),y=52+((550/9)*7),width=((700/9)-3),height=((550/9)-2))
    entry8_5.place(x=51+((700/9)*4),y=52+((550/9)*7),width=((700/9)-1),height=((550/9)-2))
    entry8_6.place(x=51+((700/9)*5),y=52+((550/9)*7),width=((700/9)-4),height=((550/9)-2))
    entry8_7.place(x=53+((700/9)*6),y=52+((550/9)*7),width=((700/9)-5),height=((550/9)-2))
    entry8_8.place(x=53+((700/9)*7),y=52+((550/9)*7),width=((700/9)-3),height=((550/9)-2))
    entry8_9.place(x=51+((700/9)*8),y=52+((550/9)*7),width=((700/9)-4),height=((550/9)-2))

    # Row 9

    entry9_1 = Entry(top,font=fontBoardNums,justify="center")
    entry9_2 = Entry(top,font=fontBoardNums,justify="center")
    entry9_3 = Entry(top,font=fontBoardNums,justify="center")
    entry9_4 = Entry(top,font=fontBoardNums,justify="center")
    entry9_5 = Entry(top,font=fontBoardNums,justify="center")
    entry9_6 = Entry(top,font=fontBoardNums,justify="center")
    entry9_7 = Entry(top,font=fontBoardNums,justify="center")
    entry9_8 = Entry(top,font=fontBoardNums,justify="center")
    entry9_9 = Entry(top,font=fontBoardNums,justify="center")

    entry9_1.place(x=53,y=52+((550/9)*8),width=((700/9)-3),height=((550/9)-2))
    entry9_2.place(x=51+((700/9)*1),y=52+((550/9)*8),width=((700/9)-1),height=((550/9)-2))
    entry9_3.place(x=51+((700/9)*2),y=52+((550/9)*8),width=((700/9)-4),height=((550/9)-2))
    entry9_4.place(x=53+((700/9)*3),y=52+((550/9)*8),width=((700/9)-3),height=((550/9)-2))
    entry9_5.place(x=51+((700/9)*4),y=52+((550/9)*8),width=((700/9)-1),height=((550/9)-2))
    entry9_6.place(x=51+((700/9)*5),y=52+((550/9)*8),width=((700/9)-4),height=((550/9)-2))
    entry9_7.place(x=53+((700/9)*6),y=52+((550/9)*8),width=((700/9)-5),height=((550/9)-2))
    entry9_8.place(x=53+((700/9)*7),y=52+((550/9)*8),width=((700/9)-3),height=((550/9)-2))
    entry9_9.place(x=51+((700/9)*8),y=52+((550/9)*8),width=((700/9)-4),height=((550/9)-2))

    fontStyleSolve = tkFont.Font(family="Sans-serif",size=40)
    fontStyleSave = tkFont.Font(family="Sans-serif",size=25)

    saveButton = Button(top, text="Save", font=fontStyleSolve,command=saveBoard)
    saveButton.place(relx=0.08,rely=0.88,relheight=0.06,relwidth=0.14)

    solveButton = Button(top, text="Solve",font=fontStyleSolve,command=solveInterface)
    solveButton.place(relx=0.4,rely=0.88,relheight=0.08,relwidth=0.2)

    exitButtonTop = Button(top,text="Exit",font=fontStyleSave,command=top.quit)
    exitButtonTop.place(relx=0.8,rely=0.88,relheight=0.06,relwidth=0.14)


fontStyleStart = tkFont.Font(family="Sans-serif",size=40)
startButton = Button(root, text="Start",font=fontStyleStart, command=start)
startButton.place(anchor="s",relheight=0.1,relwidth=0.2,relx=0.5,rely=0.55)



# Exit Button

fontStyleExit = tkFont.Font(family="Sans-serif",size=40)
exitButton = Button(root,text="Exit", command=root.quit,font=fontStyleExit)
exitButton.place(anchor="s", relheight=0.1,relwidth=0.2,relx=0.5,rely=0.70)



board = list()

def saveBoard():
    global entry1_1,entry1_2,entry1_3,entry1_4,entry1_5,entry1_6,entry1_7,entry1_8,entry1_9
    global entry2_1,entry2_2,entry2_3,entry2_4,entry2_5,entry2_6,entry2_7,entry2_8,entry2_9
    global entry3_1,entry3_2,entry3_3,entry3_4,entry3_5,entry3_6,entry3_7,entry3_8,entry3_9
    global entry4_1,entry4_2,entry4_3,entry4_4,entry4_5,entry4_6,entry4_7,entry4_8,entry4_9
    global entry5_1,entry5_2,entry5_3,entry5_4,entry5_5,entry5_6,entry5_7,entry5_8,entry5_9
    global entry6_1,entry6_2,entry6_3,entry6_4,entry6_5,entry6_6,entry6_7,entry6_8,entry6_9
    global entry7_1,entry7_2,entry7_3,entry7_4,entry7_5,entry7_6,entry7_7,entry7_8,entry7_9
    global entry8_1,entry8_2,entry8_3,entry8_4,entry8_5,entry8_6,entry8_7,entry8_8,entry8_9
    global entry9_1,entry9_2,entry9_3,entry9_4,entry9_5,entry9_6,entry9_7,entry9_8,entry9_9
    global board

    board = [[entry1_1.get(),entry1_2.get(),entry1_3.get(),entry1_4.get(),entry1_5.get(),entry1_6.get(),entry1_7.get(),entry1_8.get(),entry1_9.get()],
             [entry2_1.get(),entry2_2.get(),entry2_3.get(),entry2_4.get(),entry2_5.get(),entry2_6.get(),entry2_7.get(),entry2_8.get(),entry2_9.get()],
             [entry3_1.get(),entry3_2.get(),entry3_3.get(),entry3_4.get(),entry3_5.get(),entry3_6.get(),entry3_7.get(),entry3_8.get(),entry3_9.get()],
             [entry4_1.get(),entry4_2.get(),entry4_3.get(),entry4_4.get(),entry4_5.get(),entry4_6.get(),entry4_7.get(),entry4_8.get(),entry4_9.get()],
             [entry5_1.get(),entry5_2.get(),entry5_3.get(),entry5_4.get(),entry5_5.get(),entry5_6.get(),entry5_7.get(),entry5_8.get(),entry5_9.get()],
             [entry6_1.get(),entry2_6.get(),entry6_3.get(),entry6_4.get(),entry6_5.get(),entry6_6.get(),entry6_7.get(),entry6_8.get(),entry6_9.get()],
             [entry7_1.get(),entry7_2.get(),entry7_3.get(),entry7_4.get(),entry7_5.get(),entry7_6.get(),entry7_7.get(),entry7_8.get(),entry7_9.get()],
             [entry8_1.get(),entry8_2.get(),entry8_3.get(),entry8_4.get(),entry8_5.get(),entry8_6.get(),entry8_7.get(),entry8_8.get(),entry8_9.get()],
             [entry9_1.get(),entry9_2.get(),entry9_3.get(),entry9_4.get(),entry9_5.get(),entry9_6.get(),entry9_7.get(),entry9_8.get(),entry9_9.get()]]

    board = fixBoard(board)

    suSo.printBoard(board)
    

def fixBoard(board):

    fixedBoard = copy.deepcopy(board)
    for i in range(9):
        for j in range(9):
            if fixedBoard[i][j] != "":
                fixedBoard[i][j] = int(fixedBoard[i][j])
            else:
                fixedBoard[i][j] = 0
    
    return fixedBoard

def possible(y,x,n):
    global board
    #check rows
    for i in range(9):
        if board[y][i] == n:
            return False
    
    #check columns
    for i in range(9):
        if board[i][x] == n:
            return False

    #check box

    Xbox = (x//3)*3
    Ybox = (y//3)*3

    for i in range(3):
        for j in range(3):
            if board[Ybox+i][Xbox+j] == n:
                return False

    return True

def Solve():

    global board
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for n in range(1,10):
                    if possible(i,j,n):
                        board[i][j] = n
                        Solve()
                        board[i][j] = 0

                return
    
    suSo.printBoard(board)

    entry1_1.delete(0,END)
    entry1_2.delete(0,END)
    entry1_3.delete(0,END)
    entry1_4.delete(0,END)
    entry1_5.delete(0,END)
    entry1_6.delete(0,END)
    entry1_7.delete(0,END)
    entry1_8.delete(0,END)
    entry1_9.delete(0,END)

    entry1_1.insert(0,str(board[0][0]))
    entry1_2.insert(0,str(board[0][1]))
    entry1_3.insert(0,str(board[0][2]))
    entry1_4.insert(0,str(board[0][3]))
    entry1_5.insert(0,str(board[0][4]))
    entry1_6.insert(0,str(board[0][5]))
    entry1_7.insert(0,str(board[0][6]))
    entry1_8.insert(0,str(board[0][7]))
    entry1_9.insert(0,str(board[0][8]))

    entry2_1.delete(0,END)
    entry2_2.delete(0,END)
    entry2_3.delete(0,END)
    entry2_4.delete(0,END)
    entry2_5.delete(0,END)
    entry2_6.delete(0,END)
    entry2_7.delete(0,END)
    entry2_8.delete(0,END)
    entry2_9.delete(0,END)

    entry2_1.insert(0,str(board[1][0]))
    entry2_2.insert(0,str(board[1][1]))
    entry2_3.insert(0,str(board[1][2]))
    entry2_4.insert(0,str(board[1][3]))
    entry2_5.insert(0,str(board[1][4]))
    entry2_6.insert(0,str(board[1][5]))
    entry2_7.insert(0,str(board[1][6]))
    entry2_8.insert(0,str(board[1][7]))
    entry2_9.insert(0,str(board[1][8]))

    entry3_1.delete(0,END)
    entry3_2.delete(0,END)
    entry3_3.delete(0,END)
    entry3_4.delete(0,END)
    entry3_5.delete(0,END)
    entry3_6.delete(0,END)
    entry3_7.delete(0,END)
    entry3_8.delete(0,END)
    entry3_9.delete(0,END)

    entry3_1.insert(0,str(board[2][0]))
    entry3_2.insert(0,str(board[2][1]))
    entry3_3.insert(0,str(board[2][2]))
    entry3_4.insert(0,str(board[2][3]))
    entry3_5.insert(0,str(board[2][4]))
    entry3_6.insert(0,str(board[2][5]))
    entry3_7.insert(0,str(board[2][6]))
    entry3_8.insert(0,str(board[2][7]))
    entry3_9.insert(0,str(board[2][8]))

    entry4_1.delete(0,END)
    entry4_2.delete(0,END)
    entry4_3.delete(0,END)
    entry4_4.delete(0,END)
    entry4_5.delete(0,END)
    entry4_6.delete(0,END)
    entry4_7.delete(0,END)
    entry4_8.delete(0,END)
    entry4_9.delete(0,END)

    entry4_1.insert(0,str(board[3][0]))
    entry4_2.insert(0,str(board[3][1]))
    entry4_3.insert(0,str(board[3][2]))
    entry4_4.insert(0,str(board[3][3]))
    entry4_5.insert(0,str(board[3][4]))
    entry4_6.insert(0,str(board[3][5]))
    entry4_7.insert(0,str(board[3][6]))
    entry4_8.insert(0,str(board[3][7]))
    entry4_9.insert(0,str(board[3][8]))

    entry5_1.delete(0,END)
    entry5_2.delete(0,END)
    entry5_3.delete(0,END)
    entry5_4.delete(0,END)
    entry5_5.delete(0,END)
    entry5_6.delete(0,END)
    entry5_7.delete(0,END)
    entry5_8.delete(0,END)
    entry5_9.delete(0,END)

    entry5_1.insert(0,str(board[4][0]))
    entry5_2.insert(0,str(board[4][1]))
    entry5_3.insert(0,str(board[4][2]))
    entry5_4.insert(0,str(board[4][3]))
    entry5_5.insert(0,str(board[4][4]))
    entry5_6.insert(0,str(board[4][5]))
    entry5_7.insert(0,str(board[4][6]))
    entry5_8.insert(0,str(board[4][7]))
    entry5_9.insert(0,str(board[4][8]))

    entry6_1.delete(0,END)
    entry6_2.delete(0,END)
    entry6_3.delete(0,END)
    entry6_4.delete(0,END)
    entry6_5.delete(0,END)
    entry6_6.delete(0,END)
    entry6_7.delete(0,END)
    entry6_8.delete(0,END)
    entry6_9.delete(0,END)

    entry6_1.insert(0,str(board[5][0]))
    entry6_2.insert(0,str(board[5][1]))
    entry6_3.insert(0,str(board[5][2]))
    entry6_4.insert(0,str(board[5][3]))
    entry6_5.insert(0,str(board[5][4]))
    entry6_6.insert(0,str(board[5][5]))
    entry6_7.insert(0,str(board[5][6]))
    entry6_8.insert(0,str(board[5][7]))
    entry6_9.insert(0,str(board[5][8]))

    entry7_1.delete(0,END)
    entry7_2.delete(0,END)
    entry7_3.delete(0,END)
    entry7_4.delete(0,END)
    entry7_5.delete(0,END)
    entry7_6.delete(0,END)
    entry7_7.delete(0,END)
    entry7_8.delete(0,END)
    entry7_9.delete(0,END)

    entry7_1.insert(0,str(board[6][0]))
    entry7_2.insert(0,str(board[6][1]))
    entry7_3.insert(0,str(board[6][2]))
    entry7_4.insert(0,str(board[6][3]))
    entry7_5.insert(0,str(board[6][4]))
    entry7_6.insert(0,str(board[6][5]))
    entry7_7.insert(0,str(board[6][6]))
    entry7_8.insert(0,str(board[6][7]))
    entry7_9.insert(0,str(board[6][8]))

    entry8_1.delete(0,END)
    entry8_2.delete(0,END)
    entry8_3.delete(0,END)
    entry8_4.delete(0,END)
    entry8_5.delete(0,END)
    entry8_6.delete(0,END)
    entry8_7.delete(0,END)
    entry8_8.delete(0,END)
    entry8_9.delete(0,END)

    entry8_1.insert(0,str(board[7][0]))
    entry8_2.insert(0,str(board[7][1]))
    entry8_3.insert(0,str(board[7][2]))
    entry8_4.insert(0,str(board[7][3]))
    entry8_5.insert(0,str(board[7][4]))
    entry8_6.insert(0,str(board[7][5]))
    entry8_7.insert(0,str(board[7][6]))
    entry8_8.insert(0,str(board[7][7]))
    entry8_9.insert(0,str(board[7][8]))

    entry9_1.delete(0,END)
    entry9_2.delete(0,END)
    entry9_3.delete(0,END)
    entry9_4.delete(0,END)
    entry9_5.delete(0,END)
    entry9_6.delete(0,END)
    entry9_7.delete(0,END)
    entry9_8.delete(0,END)
    entry9_9.delete(0,END)

    entry9_1.insert(0,str(board[8][0]))
    entry9_2.insert(0,str(board[8][1]))
    entry9_3.insert(0,str(board[8][2]))
    entry9_4.insert(0,str(board[8][3]))
    entry9_5.insert(0,str(board[8][4]))
    entry9_6.insert(0,str(board[8][5]))
    entry9_7.insert(0,str(board[8][6]))
    entry9_8.insert(0,str(board[8][7]))
    entry9_9.insert(0,str(board[8][8]))
                        
    # Insert the new values in the Board.
    entry1_1["state"] = "disabled"
    entry1_2["state"] = "disabled"
    entry1_3["state"] = "disabled"
    entry1_4["state"] = "disabled"
    entry1_5["state"] = "disabled"
    entry1_6["state"] = "disabled"
    entry1_7["state"] = "disabled"
    entry1_8["state"] = "disabled"
    entry1_9["state"] = "disabled"

    entry2_1["state"] = "disabled"
    entry2_2["state"] = "disabled"
    entry2_3["state"] = "disabled"
    entry2_4["state"] = "disabled"
    entry2_5["state"] = "disabled"
    entry2_6["state"] = "disabled"
    entry2_7["state"] = "disabled"
    entry2_8["state"] = "disabled"
    entry2_9["state"] = "disabled"

    entry3_1["state"] = "disabled"
    entry3_2["state"] = "disabled"
    entry3_3["state"] = "disabled"
    entry3_4["state"] = "disabled"
    entry3_5["state"] = "disabled"
    entry3_6["state"] = "disabled"
    entry3_7["state"] = "disabled"
    entry3_8["state"] = "disabled"
    entry3_9["state"] = "disabled"

    entry4_1["state"] = "disabled"
    entry4_2["state"] = "disabled"
    entry4_3["state"] = "disabled"
    entry4_4["state"] = "disabled"
    entry4_5["state"] = "disabled"
    entry4_6["state"] = "disabled"
    entry4_7["state"] = "disabled"
    entry4_8["state"] = "disabled"
    entry4_9["state"] = "disabled"

    entry5_1["state"] = "disabled"
    entry5_2["state"] = "disabled"
    entry5_3["state"] = "disabled"
    entry5_4["state"] = "disabled"
    entry5_5["state"] = "disabled"
    entry5_6["state"] = "disabled"
    entry5_7["state"] = "disabled"
    entry5_8["state"] = "disabled"
    entry5_9["state"] = "disabled"

    entry6_1["state"] = "disabled"
    entry6_2["state"] = "disabled"
    entry6_3["state"] = "disabled"
    entry6_4["state"] = "disabled"
    entry6_5["state"] = "disabled"
    entry6_6["state"] = "disabled"
    entry6_7["state"] = "disabled"
    entry6_8["state"] = "disabled"
    entry6_9["state"] = "disabled"

    entry7_1["state"] = "disabled"
    entry7_2["state"] = "disabled"
    entry7_3["state"] = "disabled"
    entry7_4["state"] = "disabled"
    entry7_5["state"] = "disabled"
    entry7_6["state"] = "disabled"
    entry7_7["state"] = "disabled"
    entry7_8["state"] = "disabled"
    entry7_9["state"] = "disabled"

    entry8_1["state"] = "disabled"
    entry8_2["state"] = "disabled"
    entry8_3["state"] = "disabled"
    entry8_4["state"] = "disabled"
    entry8_5["state"] = "disabled"
    entry8_6["state"] = "disabled"
    entry8_7["state"] = "disabled"
    entry8_8["state"] = "disabled"
    entry8_9["state"] = "disabled"

    entry9_1["state"] = "disabled"
    entry9_2["state"] = "disabled"
    entry9_3["state"] = "disabled"
    entry9_4["state"] = "disabled"
    entry9_5["state"] = "disabled"
    entry9_6["state"] = "disabled"
    entry9_7["state"] = "disabled"
    entry9_8["state"] = "disabled"
    entry9_9["state"] = "disabled"

def solveInterface():
    global entry1_1,entry1_2,entry1_3,entry1_4,entry1_5,entry1_6,entry1_7,entry1_8,entry1_9
    global entry2_1,entry2_2,entry2_3,entry2_4,entry2_5,entry2_6,entry2_7,entry2_8,entry2_9
    global entry3_1,entry3_2,entry3_3,entry3_4,entry3_5,entry3_6,entry3_7,entry3_8,entry3_9
    global entry4_1,entry4_2,entry4_3,entry4_4,entry4_5,entry4_6,entry4_7,entry4_8,entry4_9
    global entry5_1,entry5_2,entry5_3,entry5_4,entry5_5,entry5_6,entry5_7,entry5_8,entry5_9
    global entry6_1,entry6_2,entry6_3,entry6_4,entry6_5,entry6_6,entry6_7,entry6_8,entry6_9
    global entry7_1,entry7_2,entry7_3,entry7_4,entry7_5,entry7_6,entry7_7,entry7_8,entry7_9
    global entry8_1,entry8_2,entry8_3,entry8_4,entry8_5,entry8_6,entry8_7,entry8_8,entry8_9
    global entry9_1,entry9_2,entry9_3,entry9_4,entry9_5,entry9_6,entry9_7,entry9_8,entry9_9
    global board

    Solve()


root.mainloop()

