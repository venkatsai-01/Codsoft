import tkinter as tk

text_field = ""

def update_field(inp):
    global text_field
    text_field = text_field+str(inp)
    field.delete(1.0,"end")
    field.insert(1.0,text_field)
def calculate():
    global text_field
    result = str(eval(text_field))
    field.delete(1.0,"end")
    field.insert(1.0,result)
def clear():
    global text_field
    text_field=""
    field.delete(1.0,"end")

window = tk.Tk()
window.maxsize(380,300)
window.title("Calculator")

field = tk.Text(window, height=2, width=21, font=("Aerial",24))
field.grid(row=1, column=1, columnspan=4)

btn_1 = tk.Button(window, text="1", command=lambda: update_field(1), width=5, font=("Times New Roman",14))
btn_1.grid(row=4, column=1)
btn_2 = tk.Button(window, text="2", command=lambda: update_field(2), width=5, font=("Times New Roman",14))
btn_2.grid(row=4, column=2)
btn_3 = tk.Button(window, text="3", command=lambda: update_field(3), width=5, font=("Times New Roman",14))
btn_3.grid(row=4, column=3)
btn_4 = tk.Button(window, text="4", command=lambda: update_field(4), width=5, font=("Times New Roman",14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(window, text="5", command=lambda: update_field(5), width=5, font=("Times New Roman",14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(window, text="6", command=lambda: update_field(6), width=5, font=("Times New Roman",14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(window, text="7", command=lambda: update_field(7), width=5, font=("Times New Roman",14))
btn_7.grid(row=2, column=1)
btn_8 = tk.Button(window, text="8", command=lambda: update_field(8), width=5, font=("Times New Roman",14))
btn_8.grid(row=2, column=2)
btn_9 = tk.Button(window, text="9", command=lambda: update_field(9), width=5, font=("Times New Roman",14))
btn_9.grid(row=2, column=3)
btn_0 = tk.Button(window, text="0", command=lambda: update_field(0), width=5, font=("Times New Roman",14))
btn_0.grid(row=5, column=1)

btn_div = tk.Button(window, text="/", command=lambda: update_field("/"), width=5, font=("Times New Roman",14))
btn_div.grid(row=2, column=4)
btn_mul = tk.Button(window, text="*", command=lambda: update_field("*"), width=5, font=("Times New Roman",14))
btn_mul.grid(row=3, column=4)
btn_sub = tk.Button(window, text="-", command=lambda: update_field("-"), width=5, font=("Times New Roman",14))
btn_sub.grid(row=4, column=4)
btn_add = tk.Button(window, text="+", command=lambda: update_field("+"), width=5, font=("Times New Roman",14))
btn_add.grid(row=5, column=4)

btn_par1 = tk.Button(window, text="(", command=lambda: update_field("("), width=5, font=("Times New Roman",14))
btn_par1.grid(row=5, column=2)
btn_par2 = tk.Button(window, text=")", command=lambda: update_field(")"), width=5, font=("Times New Roman",14))
btn_par2.grid(row=5, column=3)
btn_dec = tk.Button(window, text=".", command=lambda: update_field("."), width=5, font=("Times New Roman",14))
btn_dec.grid(row=6, column=2)

btn_clr = tk.Button(window, text="AC", command=lambda: clear(), width=5, font=("Times New Roman",14))
btn_clr.grid(row=6, column=1)

btn_res = tk.Button(window, text="=", command=lambda: calculate(), width=5, font=("Times New Roman",14))
btn_res.grid(row=6, column=3, columnspan=2)

window.mainloop()