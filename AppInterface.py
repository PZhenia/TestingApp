import tkinter as tk
from tkinter import messagebox, simpledialog
from ManagerTest import Manager
from CreateTest import CreateTest
from TestAttempt import TestAttempt
from User import User

class TestingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Testing App")
        self.geometry("500x400")
        self.manager = Manager()
        self.current_user = None
        self.main_menu()

    def main_menu(self):
        self.clear_frame()
        tk.Label(self, text="Testing App", font=("Arial", 18)).pack(pady=20)
        tk.Button(self, text="Login", command=self.login).pack(pady=10)
        tk.Button(self, text="Register", command=self.register).pack(pady=10)
        tk.Button(self, text="Continue as Guest", command=self.guest_mode).pack(pady=10)

    def login(self):
        username = simpledialog.askstring("Login", "Enter your username:")
        password = simpledialog.askstring("Login", "Enter your password:", show="*")
        user = self.manager.users.get(username)
        if user and user.password == password:
            self.current_user = user
            messagebox.showinfo("Login", f"Welcome back, {username}!")
            self.user_menu()
        else:
            messagebox.showerror("Error", "Invalid credentials.")

    def register(self):
        username = simpledialog.askstring("Register", "Enter a new username:")
        if username in self.manager.users:
            messagebox.showerror("Error", "Username already exists.")
            return
        password = simpledialog.askstring("Register", "Enter a new password:", show="*")
        user = User(username, password)
        self.manager.save_user(user)
        messagebox.showinfo("Register", "Account created successfully.")
        self.current_user = user
        self.user_menu()

    def guest_mode(self):
        self.current_user = None
        self.user_menu()

    def user_menu(self):
        self.clear_frame()
        tk.Label(self, text=f"Welcome {self.current_user.username if self.current_user else 'Guest'}", font=("Arial", 18)).pack(pady=20)

        if self.current_user:  # Доступ до створення тесту і профілю тільки для зареєстрованих користувачів
            tk.Button(self, text="Create Test", command=lambda: CreateTest(self.manager).create_test()).pack(pady=10)
            tk.Button(self, text="View Profile", command=self.view_profile).pack(pady=10)

        tk.Button(self, text="Take Test", command=lambda: TestAttempt(self.manager).take_test(self.current_user)).pack(pady=10)
        tk.Button(self, text="Logout", command=self.main_menu).pack(pady=10)

    def view_profile(self):
        if not self.current_user:
            messagebox.showinfo("Info", "Guests do not have a profile.")
            return

        progress_text = self.current_user.progress.view_progress()
        messagebox.showinfo("Profile", f"Progress:\n{progress_text}")

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
