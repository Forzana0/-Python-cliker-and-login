from tkinter import *
from tkinter import messagebox
import pickle

def registration():
    label_error = None
    frame = Frame(root, bd=10)
    frame.place(relx=0.5, rely=0.2, relwidth=0.7, relheight=0.6, anchor="n")
    
    label = Label(frame, text="Sign Up", font='16')
    label.place(relwidth=1, relheight=0.1)
    
    label_login = Label(frame, text="Login : ")
    label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)
    
    login_register = Entry(frame)
    login_register.place(rely=0.2, relwidth=0.55, relheight=0.1, relx=0.4)
    
    label_password1 = Label(frame, text="Password : ")
    label_password1.place(rely=0.4, relwidth=0.35, relheight=0.1)
    
    password1 = Entry(frame, show="*")
    password1.place(rely=0.4, relwidth=0.55, relheight=0.1, relx=0.4)
    
    label_password2 = Label(frame, text="Confirm Password : ")
    label_password2.place(rely=0.6, relwidth=0.35, relheight=0.1)
    
    password2 = Entry(frame, show="*")
    password2.place(rely=0.6, relwidth=0.55, relheight=0.1, relx=0.4)
    
    button = Button(frame, text="Sign Up", command=lambda: signup(login_register, password1))
    button.place(relx=0.3, rely=0.8, relwidth=0.5, relheight=0.15)

    def signup(login_register, password1):
        nonlocal label_error
        error = ""
        
        if label_error:
            label_error.destroy()
            
        if len(login_register.get()) == 0:
            error = "*login error"
        elif len(password1.get()) < 5:
            error = "*your password needs to be at least 5 characters"
        elif not password1.get() == password2.get():
            error = "*your password needs to be the same"
        else:
            save(login_register, password1)
            
        label_error = Label(frame, text=error, fg='red')
        label_error.place(rely=0.7)

    def save(login_register, password1):
        data = dict()
        data[login_register.get()] = password1.get()
        with open("login.txt", 'wb') as f:
            pickle.dump(data, f)
        login_form()

def login_form():
    frame = Frame(root, bd=10)
    frame.place(relx=0.5, rely=0.2, relwidth=0.7, relheight=0.6, anchor="n")

    label = Label(frame, text="Sign In", font='16')
    label.place(relwidth=1, relheight=0.1)

    label_login = Label(frame, text="Login : ")
    label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)

    login_register = Entry(frame)
    login_register.place(rely=0.2, relwidth=0.55, relheight=0.1, relx=0.4)

    label_password1 = Label(frame, text="Password : ")
    label_password1.place(rely=0.4, relwidth=0.35, relheight=0.1)

    password1 = Entry(frame, show="*")
    password1.place(rely=0.4, relwidth=0.55, relheight=0.1, relx=0.4)

    button = Button(frame, text="Sign Up", command=lambda: login_pass(login_register, password1))
    button.place(relx=0.3, rely=0.8, relwidth=0.5, relheight=0.15)

def login_pass(login_register, password1):
    try:
        with open('login.txt', 'rb') as f:
            a = pickle.load(f)
            if login_register.get() in a and password1.get() == a[login_register.get()]:
                messagebox.showinfo("Welcome", "Welcome to our world!")
            else:
                messagebox.showerror("Error!", "Invalid Password or login")
    except Exception as e:
        messagebox.showerror("Error!", f"An error occurred: {e}")

root = Tk()
root.title("Login Form")
root.geometry("550x550")
root.resizable(False, False)
root.option_add("*Font", "Calibri")
root.option_add("*Background", "yellowgreen")

img = PhotoImage(file="bg3.gif")
background_label = Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

button_signup = Button(root, text="Sign Up", command=registration)
button_signup.place(relx=0.15, rely=0.1, relwidth=0.3)

button_signin = Button(root, text="Sign In", command=login_form)
button_signin.place(relx=0.5, rely=0.1, relwidth=0.3)

root.mainloop()
