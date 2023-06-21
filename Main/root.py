import customtkinter, securePassFunc
import UserPy , AdmPy
from tkinter import *


customtkinter.set_appearance_mode("light")

with open('accs.txt', 'r') as file:
    lines = file.readlines()

root = customtkinter.CTk()
root.title("")
root.geometry("960x540")
root.resizable(False, False)

createUser = UserPy.User("", "")
createAdm = AdmPy.Adm("", "")

def login_window():
    def validate_login():
        for i in range(0, len(lines), 2):
            stored_login = lines[i].strip()
            stored_password = lines[i+1].strip()

            if entryl1.get() == stored_login and entryl2.get() == stored_password:
                main_window()
            elif entryl1.get() == "admin" and entryl2.get() == "admin":
                main_window_adm()
            else:
                label.configure(text="Invalid credentials.")

    bg = PhotoImage(file='images/Ackg.png')
    bgLabel = customtkinter.CTkLabel(master=root, image=bg, text="")
    bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

    labelLog = customtkinter.CTkLabel(root, width=0, height=25, corner_radius=8, bg_color="#f5fdff", text_color="#bdc3c7", text="Login:")
    labelLog.grid(row=4, column=1, pady=0, padx=0, sticky="w")
    entryl1 = customtkinter.CTkEntry(root, width=200, height=25, corner_radius=5)
    entryl1.grid(row=5, column=1, pady=0, padx=0, sticky="s")

    labelPass = customtkinter.CTkLabel(root, width=0, height=25, corner_radius=8, bg_color="#f5fdff", text_color="#bdc3c7", text="Password:")
    labelPass.grid(row=6, column=1, pady=0, padx=0, sticky="w")
    entryl2 = customtkinter.CTkEntry(root, width=200, height=25, corner_radius=5)
    entryl2.grid(row=7, column=1, pady=0, padx=0, sticky="n")
    loginbutton = customtkinter.CTkButton(root, width=20, height=20, fg_color=("#2ecc71"), hover_color=("#27ae60"), text="➤", command=validate_login, font=("Roboto-Bold", 8))
    loginbutton.grid(row=7, column=1, pady=2, padx=2, sticky="ne")

    label = customtkinter.CTkLabel(root, width=120, height=25, corner_radius=8, bg_color="#f5fdff", text_color="#E76161", text="")
    label.grid(row=8, column=1, pady=0, padx=0, sticky="n")

def create_acc_window():
    def create_user():
        createUser.set_login(entry1.get())
        createUser.set_password(entry3.get())
        print(createUser.get_credentials())
        credentials = createUser.get_credentials()
        if entry1.get() == entry2.get():
            with open('accs.txt', 'a') as file:
                file.write(f"{credentials}")
            login_window()
        else:
            label.configure(text="E-mails must match!") 
            
    def generate_button():
        password = securePassFunc.securePass()
        entry3.delete(0, END)  
        entry3.insert(0, password) 

    bg = PhotoImage(file='images/Ackg.png')
    bgLabel = customtkinter.CTkLabel(master=root, image=bg, text="")
    bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

    labelUser = customtkinter.CTkLabel(root, text="User:", width=0, height=25, corner_radius=8,bg_color="#f5fdff", text_color="#bdc3c7")
    labelUser.grid(row=2, column=1, pady=0, padx=0, sticky="w")
    entry1 = customtkinter.CTkEntry(root, width=200, height=25, corner_radius=5)
    entry1.grid(row=3, column=1, pady=0, padx=0, sticky="")

    labelUser = customtkinter.CTkLabel(root, text="Repeat User:", width=0, height=25, corner_radius=8,bg_color="#f5fdff", text_color="#bdc3c7")
    labelUser.grid(row=4, column=1, pady=0, padx=0, sticky="w")
    entry2 = customtkinter.CTkEntry(root, width=200, height=25, corner_radius=5)
    entry2.grid(row=5, column=1, pady=0, padx=0, sticky="")

    labelUser = customtkinter.CTkLabel(root, text="Password:", width=0, height=25, corner_radius=8,bg_color="#f5fdff", text_color="#bdc3c7")
    labelUser.grid(row=6, column=1, pady=0, padx=0, sticky="w")
    entry3 = customtkinter.CTkEntry(root, width=200, height=25, corner_radius=5)
    entry3.grid(row=7, column=1, pady=0, padx=0, sticky="")
    generatebutton = customtkinter.CTkButton(root, width=20, height=20, fg_color=("#bdc3c7"), hover_color=("#7f8c8d"), text="❂", command=generate_button, font=("Roboto-Bold", 8))
    generatebutton.grid(row=7, column=1, pady=0, padx=2, sticky="e")

    createbutton = customtkinter.CTkButton(root, width=200, height=20, fg_color=("#2ecc71"), hover_color=("#27ae60"), text="Create User", command=create_user, font=("Roboto-Bold", 15))
    createbutton.grid(row=8, column=1, pady=25, padx=0, sticky="n")
    
    error_msg = ""
    label = customtkinter.CTkLabel(root, text=error_msg, width=120, height=25, corner_radius=8,bg_color="#f5fdff", text_color="#E76161")
    label.grid(row=2, column=1, pady=0, padx=0, sticky="se")

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(8, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(3, weight=1)
    
def main_window():
    bg = PhotoImage(file='images/MaPU.png')
    bgLabel = customtkinter.CTkLabel(master=root, image=bg, text="")
    bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

def main_window_adm():   
    admView = createAdm.get_privilleges()
    bg = PhotoImage(file='images/MaP.png')
    bgLabel = customtkinter.CTkLabel(master=root, image=bg, text="")
    bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
    
    labelPriv = customtkinter.CTkLabel(root, text=admView, width=120, height=25, corner_radius=8, text_color= "#2ecc71", bg_color="#ffffff")
    labelPriv.grid(row=1, column=1, pady=0, padx=0, sticky="ew")
    label = customtkinter.CTkLabel(root, text=lines, width=120, height=25, corner_radius=8, text_color= "#2ecc71", bg_color="#ffffff")
    label.grid(row=1, column=1, pady=0, padx=0, sticky="ew")
    
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

create_acc_window()

root.mainloop()
