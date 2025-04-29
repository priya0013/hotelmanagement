import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

def login():
    username = entry_username.get()
    password = entry_password.get()

    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_mysql_password",  # Change this
            database="hotel_management"       # Change this
        )
        cursor = mydb.cursor()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            root.destroy()
            # Open main dashboard here
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
        
        mydb.close()

    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# Main window
root = tk.Tk()
root.title("Hotel Management System - Login")
root.geometry("1295x550+230+220")
root.resizable(False, False)

# Load Background Image
bg_image = Image.open("hotel_bg.jpg")  # Your hotel image file
bg_image = bg_image.resize((600, 400), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a Label to hold the background image
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Transparent frame on top
frame = tk.Frame(root, bg="#ffffff", bd=5)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title
tk.Label(frame, text="Hotel Paradise", font=("Arial", 20, "bold"), bg="#ffffff", fg="#2d3436").pack(pady=10)
tk.Label(frame, text="Login to Continue", font=("Arial", 12), bg="#ffffff").pack(pady=5)

# Username
tk.Label(frame, text="Username", font=("Arial", 10), bg="#ffffff").pack(pady=5)
entry_username = tk.Entry(frame, width=30)
entry_username.pack(pady=5)

# Password
tk.Label(frame, text="Password", font=("Arial", 10), bg="#ffffff").pack(pady=5)
entry_password = tk.Entry(frame, show="*", width=30)
entry_password.pack(pady=5)

# Login Button
tk.Button(frame, text="Login", font=("Arial", 10, "bold"), bg="#0984e3", fg="white", width=15, command=login).pack(pady=15)

root.mainloop()
