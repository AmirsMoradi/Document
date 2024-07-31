from tkinter import messagebox

from sanad.sanad import session, User, Role, FinancialRecord
import tkinter as tk


def login():
    username = username_entry.get()
    password = password_entry.get()
    user = session.query(User).filter_by(username=username, password=password).first()
    if user:
        if user.role == Role.ADMIN:
            messagebox.showinfo("Login Successful", "Welcome Admin!")
            show_all_records()
        else:
            messagebox.showinfo("Login Successful", "Welcome Customer!")
            show_records(user)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# تابع برای نمایش تمامی اسناد (برای ادمین)
def show_all_records():
    records_window = tk.Toplevel(root)
    records_window.title("All Financial Records")

    tk.Label(records_window, text="First Name").grid(row=0, column=0)
    tk.Label(records_window, text="Last Name").grid(row=0, column=1)
    tk.Label(records_window, text="Description").grid(row=0, column=2)
    tk.Label(records_window, text="Amount").grid(row=0, column=3)
    tk.Label(records_window, text="Username").grid(row=0, column=4)

    records = session.query(FinancialRecord).all()
    for i, record in enumerate(records):
        tk.Label(records_window, text=record.first_name).grid(row=i+1, column=0)
        tk.Label(records_window, text=record.last_name).grid(row=i+1, column=1)
        tk.Label(records_window, text=record.description).grid(row=i+1, column=2)
        tk.Label(records_window, text=record.amount).grid(row=i+1, column=3)
        tk.Label(records_window, text=record.user.username).grid(row=i+1, column=4)

# تابع برای نمایش اسناد کاربر (برای مشتری)
def show_records(user):
    records_window = tk.Toplevel(root)
    records_window.title("Your Financial Records")

    tk.Label(records_window, text="First Name").grid(row=0, column=0)
    tk.Label(records_window, text="Last Name").grid(row=0, column=1)
    tk.Label(records_window, text="Description").grid(row=0, column=2)
    tk.Label(records_window, text="Amount").grid(row=0, column=3)

    for i, record in enumerate(user.records):
        tk.Label(records_window, text=record.first_name).grid(row=i+1, column=0)
        tk.Label(records_window, text=record.last_name).grid(row=i+1, column=1)
        tk.Label(records_window, text=record.description).grid(row=i+1, column=2)
        tk.Label(records_window, text=record.amount).grid(row=i+1, column=3)

root = tk.Tk()
root.title("Login")

tk.Label(root, text="Username").grid(row=0, column=0)
tk.Label(root, text="Password").grid(row=1, column=0)

username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)

tk.Button(root, text="Login", command=login).grid(row=2, column=1)