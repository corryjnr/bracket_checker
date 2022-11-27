from tkinter import *
from tkinter import messagebox
from bracket_checker import balance
from tkinter.filedialog import askopenfilename

def open_file():
    """Open a file for checking."""
    filepath = askopenfilename(initialdir="/", filetypes=[("Java Files", "*.java")]
        )
    txt_edit.delete("1.0", END)
    
    with open(filepath, mode="r") as input_file:
        global content
        content = input_file.read()
        txt_edit.insert(END, content)
    
    
def check():
    program = content
    global status
    status = balance(program)
    messagebox.showinfo("Check complete", status)
    
window = Tk()
window.title("Check nesting")
window.grid_columnconfigure(1, weight=1)

txt_edit = Text(window)

frm_buttons = Frame(window, relief=RAISED, bd=1)
btn_open = Button(frm_buttons, text="Select file", command=open_file)
btn_check = Button(
    frm_buttons, text="Check brackets", command=check)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_check.grid(row=0, column=1, sticky="ew", padx=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=1, column=0, sticky="ns")

txt_edit.configure(fg="black", background='white')

window.mainloop()