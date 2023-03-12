#!/usr/bin/python3

import tkinter as tk
groot = tk.Tk()
#groot.geometry("800x200")
groot.title("GUI Checkbuttons")

accum = "00000000" # default starting contents for the Accumulator register
register_A = "00000000"
display_A = " 0 0 0 0 0 0 0 0 "
register_B = "00000000" 

# need to use my_bool#.set() and my_bool#.get() to
# set and get the value of these variables for the check boxes

# A_frame = tk.Frame(groot, highlightbackground="black", highlightthickness=3)
A_frame = tk.Frame(groot, highlightbackground="green", highlightthickness=3)

my_ck_A = []
for i in range(8):
    my_ck_A.append(tk.BooleanVar())

def doButt_A():
    global register_A
    global dislay_A
    #label_reg_A.configure(text = register_A)
    # make string for reg A
    register_A = ""
    display_A = ""
    for i in range(8):
        register_A =  register_A + str(int(my_ck_A[i].get()))
        display_A = display_A + " " + str(int(my_ck_A[i].get()))
    display_A = display_A + " "    
    label_reg_A.configure(text = display_A)
    
    
label_reg_A = tk.Label(A_frame, font=("Fixedsys", 16), text=display_A, borderwidth=1, relief="solid")

B2 = tk.Button(A_frame, text="-> LOAD ->", command=doButt_A)

but_frame_A = tk.Frame(A_frame)

chk_bx_A = []
col_lab_A = []
col_num = 128
for i in range(8):
    count = i+1
    name = str(count)
    chk_bx_A.append(tk.Checkbutton(but_frame_A, var=my_ck_A[i]))
    col_txt = str(int(col_num))
    col_lab_A.append(tk.Label(but_frame_A, text=col_txt))
    col_num = col_num/2                    

chk_bx_A[0].select()
                     
but_A_col = 0
but_A_row = 0
for c in range(8):
    col_lab_A[c].grid(column=c,row=0)
    chk_bx_A[c].grid(column=c,row=1)


but_frame_A.grid(column=0,row=0, padx=(30, 10), pady=(10, 10))
B2.grid(column=1,row=0)
label_reg_A.grid(column=2,row=0, padx=(10, 30))

A_frame.pack(padx=20, pady=20)

groot.mainloop()
