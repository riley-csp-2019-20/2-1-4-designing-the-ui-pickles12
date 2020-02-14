##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

# main window
root = tk.Tk()
frame_login = tk.Frame(root)
root.title("Authentication")
root.wm_geometry("2000x1000")
frame_login.grid()
tk.Label(frame_login,text="Password:",font="Courier")

def test_my_button():
    print("clicked")
    frame_auth.tkraise()
    password = ent_password.get()
    print(password)
    frame_authe.config(text = password)




lbl_username = tk.Label(frame_login, text='Username:',font="Arial")
lbl_username.pack(padx=15, pady=15)

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(padx=5)

lbl_password = tk.Label(frame_login, text='Password:',font="Arial")
lbl_password.pack(padx=15, pady=15)

ent_password = tk.Entry(frame_login, bd=3,show="*")
ent_password.pack(padx=5)

btn_enter = tk.Button(frame_login, text='Login:',font="Arial", command=test_my_button)
btn_enter.pack(padx=15, pady=15)

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")

frame_authe = tk.Label(frame_auth, text="test", font="ComicSans")
frame_authe.pack(padx=15, pady=15)

frame_login.tkraise()

root.mainloop()